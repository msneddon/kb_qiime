#BEGIN_HEADER
# The header block is where all import statments should live
import os
import sys
import traceback
import subprocess
import uuid
from pprint import pprint, pformat
from QIIME.KBaseDataUtil import KBaseDataUtil
from biokbase.workspace.client import Workspace as workspaceService
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
            raise ValueError('workspace_name parameter is required')
        if 'post_split_lib' not in params:
            raise ValueError('post_split_lib parameter is required')
        if 'otu_table_name' not in params:
            raise ValueError('otu_table_name parameter is required')

        # get the file
        try:
            ws = workspaceService(self.workspaceURL, token=ctx['token'])
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
        params_file_path = os.path.join(self.scratch,'parameters.txt')

        self.KBaseDataUtil.download_file_from_shock(
                                 shock_service_url = data['fasta']['url'],
                                 shock_id = data['fasta']['id'],
                                 filePath = input_file_path,
                                 token = ctx['token'])


        # write the parameters file
        p_file = open(params_file_path, 'w')
        p_file.write('pick_otus:enable_rev_strand_match True\n');
        p_file.close();

        unique_id = str(hex(uuid.getnode()));
        out_dir = 'out_'+unique_id
        cmd = ['pick_closed_reference_otus.py', '-i', input_file_path, '-o', os.path.join(self.scratch,out_dir), '-p', params_file_path]

        print('running: '+' '.join(cmd))
        p = subprocess.Popen(cmd,
                        cwd = self.scratch,
                        stdout = subprocess.PIPE, 
                        stderr = subprocess.STDOUT, shell = False)

        while True:
            line = p.stdout.readline()
            if not line: break
            #report += line
            print(line.replace('\n', ''))

        p.stdout.close()
        p.wait()
        print('return code: ' + str(p.returncode))


        returnVal = {}


        #END pick_closed_reference_otus

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method pick_closed_reference_otus return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
