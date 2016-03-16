#BEGIN_HEADER
# The header block is where all import statments should live
import os
import sys
import traceback
import subprocess
import uuid
import threading
import time
import fnmatch
from pprint import pprint, pformat
from QIIME.KBaseDataUtil import KBaseDataUtil
from biokbase.workspace.client import Workspace as workspaceService
from biokbase.AbstractHandle.Client import AbstractHandle as HandleService

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



class DisplayLogFileThread(threading.Thread):
    def __init__(self, log_location, stop_event):
        threading.Thread.__init__(self)
        self.log = None
        self.log_location = log_location
        self.stop_event = stop_event

    def run(self):
        while not self.log and not self.stop_event.is_set():
            # if the log file isn't there yet, keep checking
            if not self.log:
                if os.path.isdir(self.log_location):
                    for f in os.listdir(self.log_location):
                        if fnmatch.fnmatch(f, 'log_*.txt'):
                            print('Reading QIIME LOG from: ' + os.path.join(self.log_location,f))
                            self.log = open(os.path.join(self.log_location,f),'r')
            if not self.log:
                self.stop_event.wait(1)

            # if the log file is there, start reading each line
        while not self.stop_event.is_set():
            line = self.log.readline()
            if not line:
                self.stop_event.wait(0.5) # Sleep briefly
                continue
            print('QIIME LOG: '+line.replace('\n', ''))


#END_HEADER


class QIIME:
    '''
    Module Name:
    QIIME

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.shockURL = config['shock-url']
        self.handleURL = config['handle-service-url']
        self.scratch = os.path.abspath(config['scratch'])
        if not os.path.exists(self.scratch):
            os.makedirs(self.scratch)
        self.KBaseDataUtil = KBaseDataUtil()
        #END_CONSTRUCTOR
        pass

    def pick_closed_reference_otus(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN pick_closed_reference_otus

        print('Running QIIME.pick_closed_reference_otus with params=')
        print(pformat(params))

        #### do some basic checks
        objref = ''
        if 'workspace' not in params:
            raise ValueError('workspace parameter is required')
        if 'post_split_lib' not in params:
            raise ValueError('post_split_lib parameter is required')
        if 'otu_table_name' not in params:
            raise ValueError('otu_table_name parameter is required')

        # setup provenance
        provenance = [{}]
        if 'provenance' in ctx:
            provenance = ctx['provenance']
        # add additional info to provenance here, in this case the input data object reference
        provenance[0]['input_ws_objects']=[params['workspace']+'/'+params['post_split_lib']]


        # get the file
        ws = workspaceService(self.workspaceURL, token=ctx['token'])
        try:
            objects = ws.get_objects([{'ref': params['workspace']+'/'+params['post_split_lib']}])
            data = objects[0]['data']
            info = objects[0]['info']
            # Object Info Contents
            # absolute ref = info[6] + '/' + info[0] + '/' + info[4]
            # 0 - obj_id objid
            # 1 - obj_name name
            # 2 - type_string type
            # 3 - timestamp save_date
            # 4 - int version
            # 5 - username saved_by
            # 6 - ws_id wsid
            # 7 - ws_name workspace
            # 8 - string chsum
            # 9 - int size 
            # 10 - usermeta meta
            type_name = info[2].split('.')[1].split('-')[0]
        except Exception as e:
            raise ValueError('Unable to fetch read library object from workspace: ' + str(e))

        input_file_path = os.path.join(self.scratch,data['fasta']['file_name'])

        self.KBaseDataUtil.download_file_from_shock(
                                 shock_service_url = data['fasta']['url'],
                                 shock_id = data['fasta']['id'],
                                 filePath = input_file_path,
                                 token = ctx['token'])


        # create a UUID for output directory and parameter file name; not generally needed in KBase,
        # but useful for local testing in case directories already exist.
        unique_id = str(hex(uuid.getnode()));
        params_file_path = os.path.join(self.scratch,'parameters_'+unique_id+'.txt')

        # If a parameters file is specified, write it out and save in provenance
        if 'parameters_config' in params:
            if params['parameters_config']:
                try:
                    objects = ws.get_objects([{'ref': params['workspace']+'/'+params['parameters_config']}])
                except Exception as e:
                    raise ValueError('Unable to fetch parameters configuration from workspace: ' + str(e))

                p_file = open(params_file_path, 'w')
                p_lines = objects[0]['data']['lines']
                for l in p_lines:
                    p_file.write(l+'\n')
                p_file.close()

                provenance[0]['input_ws_objects'].append(params['workspace']+'/'+params['parameters_config'])


        # Write any additional parameters to the end of the configuration file
        p_file = open(params_file_path, 'a+')
        if 'rev_strand_match' in params:
            if params['rev_strand_match']:
                p_file.write('pick_otus:enable_rev_strand_match True\n');
        p_file.close()

        # be nice and print the parameters file to the log
        f = open(params_file_path, "r")
        print('\nParameters File: ')
        print(f.read())
        print('END Parameters File.\n')
        f.close()

        out_dir = os.path.join(self.scratch,'out_'+unique_id)
        cmd = ['pick_closed_reference_otus.py', '-i', input_file_path, '-o', out_dir, '-p', params_file_path]

        print('running: '+' '.join(cmd))
        p = subprocess.Popen(cmd,
                        cwd = self.scratch,
                        stdout = subprocess.PIPE, 
                        stderr = subprocess.STDOUT, shell = False)


        # capture the log as it is written
        stopLogStream= threading.Event()
        logThread = DisplayLogFileThread(out_dir,stopLogStream)
        logThread.start()

        console_messages = '';
        while True:
            # Read std out/err and print anything we get
            line = p.stdout.readline()
            if not line: break
            console_messages += line
            print(line.replace('\n', ''))

        p.stdout.close()
        p.wait()
        print('command return code: ' + str(p.returncode))
        if p.returncode != 0:
            raise ValueError('Error running pick_closed_reference_otus.py, return code: '+str(p.returncode) + ' - ' + console_messages)
        stopLogStream.set()


        # analyze stats for the output biom
        biom_file = os.path.join(out_dir,'otu_table.biom')
        print('Collecting summary of output OTU Table ('+biom_file+')')
        cmd = ['biom', 'summarize-table', '-i', biom_file]
        print('running: '+' '.join(cmd))
        p = subprocess.Popen(cmd,
                        cwd = self.scratch,
                        stdout = subprocess.PIPE, 
                        stderr = subprocess.STDOUT, shell = False)
        biom_file_summary = '';
        while True:
            # Read std out/err and print anything we get
            line = p.stdout.readline()
            if not line: break
            biom_file_summary += line
            print('SUMMARY: '+line.replace('\n', ''))

        p.stdout.close()
        p.wait()
        print('command return code: ' + str(p.returncode))
        if p.returncode != 0:
            raise ValueError('Error running biom summarize-table, return code: '+str(p.returncode) + ' - ' + biom_file_summary)




        # collect output and save the result
        print('saving BIOM output: ' + biom_file)
        # tree file: tree_file = os.path.join(out_dir,'otu_table.biom')

        # upload files to shock
        shock_file = self.KBaseDataUtil.upload_file_to_shock(
            shock_service_url = self.shockURL,
            filePath = biom_file,
            token = ctx['token']
            )
        # create handle
        hs = HandleService(url=self.handleURL, token=ctx['token'])
        file_handle = hs.persist_handle({
                                        'id' : shock_file['id'], 
                                        'type' : 'shock',
                                        'url' : self.shockURL,
                                        'file_name': shock_file['file']['name'],
                                        'remote_md5': shock_file['file']['checksum']['md5']})
        # save to WS
        otu_tbl = {
            'biom': {
                'hid':file_handle,
                'file_name': shock_file['file']['name'],
                'id': shock_file['id'],
                'url': self.shockURL,
                'remote_md5':shock_file['file']['checksum']['md5'],
                'size':shock_file['file']['size']
            },
            #'n_samples':0,
            #'n_observations':0,
            #'count':0,
            #'density':0,
            #'sample_detail':{},
            'summary':biom_file_summary
        }

        otu_tbl_info = ws.save_objects({
                        'id':info[6],
                        'objects':[
                            {
                                'type':'QIIME.OTUTable',
                                'data':otu_tbl,
                                'name':params['otu_table_name'],
                                'meta':{},
                                'provenance':provenance
                            }]
                        })[0]
        print(pformat(otu_tbl_info))



        # create the report
        report = ''
        report += 'OTU Table saved to: '+otu_tbl_info[7]+'/'+otu_tbl_info[1]+'\n'
        report += 'OTU Table Summary:\n'
        report += biom_file_summary

        reportObj = {
            'objects_created':[{'ref':otu_tbl_info[7]+'/'+otu_tbl_info[1], 'description':'The new OTU Table'}],
            'text_message':report
        }

        reportName = 'QIIME.pick_closed_reference_otus_report_'+str(hex(uuid.getnode()))
        report_obj_info = ws.save_objects({
                'id':info[6],
                'objects':[
                    {
                        'type':'KBaseReport.Report',
                        'data':reportObj,
                        'name':reportName,
                        'meta':{},
                        'hidden':1,
                        'provenance':provenance
                    }
                ]
            })[0]

        # return the result
        returnVal = { 
            'report_name': reportName,
            'report_ref': str(report_obj_info[6]) + '/' + str(report_obj_info[0]) + '/' + str(report_obj_info[4]),
            'otu_table_ref': str(otu_tbl_info[6]) + '/' + str(otu_tbl_info[0]) + '/' + str(otu_tbl_info[4]) }
        
        #END pick_closed_reference_otus

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method pick_closed_reference_otus return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def create_parameters_configuration(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN create_parameters_configuration
        print('Running QIIME.create_parameters_configuration with params=')
        print(pformat(params))

        #### do some basic checks
        objref = ''
        if 'workspace' not in params:
            raise ValueError('workspace parameter is required')
        if 'name' not in params:
            raise ValueError('name parameter is required')
        if 'content' not in params:
            raise ValueError('content parameter is required')

        # setup provenance
        provenance = [{}]
        if 'provenance' in ctx:
            provenance = ctx['provenance']

        # get the file
        ws = workspaceService(self.workspaceURL, token=ctx['token'])

        # split the parameter lines into a list
        param_lines = []
        for l in params['content'].split('\n'):
            param_lines.append(l)

        parameter_config = {
            'lines':param_lines
        }

        params_info = ws.save_objects({
                        'workspace':params['workspace'],
                        'objects':[
                            {
                                'type':'QIIME.QIIMEParameters',
                                'data':parameter_config,
                                'name':params['name'],
                                'meta':{},
                                'provenance':provenance
                            }]
                        })[0]

        # create the report
        report = 'Saved QIIME Parameters Configuration\n'
        report += '====================================\n'
        report += params['content']

        reportObj = {
            'objects_created':[{'ref':params_info[7]+'/'+params_info[1], 'description':'The new QIIME Parameters configuration.'}],
            'text_message':report
        }

        reportName = 'QIIME.create_parameters_configuration_report_'+str(hex(uuid.getnode()))
        report_obj_info = ws.save_objects({
                'id':params_info[6],
                'objects':[
                    {
                        'type':'KBaseReport.Report',
                        'data':reportObj,
                        'name':reportName,
                        'meta':{},
                        'hidden':1,
                        'provenance':provenance
                    }
                ]
            })[0]


        returnVal = { 
            'report_name': reportName,
            'report_ref': str(report_obj_info[6]) + '/' + str(report_obj_info[0]) + '/' + str(report_obj_info[4]),
            'parameters_configuration_ref': str(params_info[6]) + '/' + str(params_info[0]) + '/' + str(params_info[4]) }



        #END create_parameters_configuration

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method create_parameters_configuration return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
