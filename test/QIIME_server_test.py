import unittest
import os
import json
import time

from os import environ
from ConfigParser import ConfigParser
from pprint import pprint

from biokbase.workspace.client import Workspace
from biokbase.AbstractHandle.Client import AbstractHandle as HandleService

from QIIME.QIIMEImpl import QIIME
from QIIME.KBaseDataUtil import KBaseDataUtil

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class QIIMETest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        token = environ.get('KB_AUTH_TOKEN', None)
        cls.ctx = {'token': token, 'provenance': [{'service': 'QIIME',
            'method': 'please_never_use_it_in_production', 'method_params': []}],
            'authenticated': 1}

        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('QIIME'):
            cls.cfg[nameval[0]] = nameval[1]

        cls.wsURL = cls.cfg['workspace-url']
        cls.ws = Workspace(cls.wsURL, token=token)
        cls.qiime = QIIME(cls.cfg)

        cls.shockURL = cls.cfg['shock-url']
        cls.handleURL = cls.cfg['handle-service-url']

        cls.kbaseDataUtil = KBaseDataUtil()


    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.ws.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWs(self):
        return self.__class__.ws

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_QIIME_" + str(suffix)
        ret = self.getWs().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getQiime(self):
        return self.__class__.qiime

    def getKbaseDataUtil(self):
        return self.__class__.kbaseDataUtil

    def getContext(self):
        return self.__class__.ctx




    def test_pick_closed_reference_otus(self):

        # figure out where the test data lives
        ps_lib_info = self.getPostSplitLibInfo()
        pprint(ps_lib_info)

        # Object Info Contents
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

        # run megahit
        params = {
            'workspace': ps_lib_info[7],
            'post_split_lib': ps_lib_info[1],
            'otu_table_name' : 'OTU_Table'
        }

        result = self.getQiime().pick_closed_reference_otus(self.getContext(),params)
        print('RESULT:')
        pprint(result)

        return



    # call this method to get the WS object info of a PostSplitLibrary (will
    # upload the example data if this is the first time the method is called during tests)
    def getPostSplitLibInfo(self):
        if hasattr(self.__class__, 'postSplitLibInfo'):
            return self.__class__.postSplitLibInfo

        # 1) upload files to shock
        token = self.ctx['token']
        shock_file = self.getKbaseDataUtil().upload_file_to_shock(
            shock_service_url = self.shockURL,
            filePath = 'test_data/sequences.fasta',
            token = token
            )

        # 2) create handle
        hs = HandleService(url=self.handleURL, token=token)
        file_handle = hs.persist_handle({
                                        'id' : shock_file['id'], 
                                        'type' : 'shock',
                                        'url' : self.shockURL,
                                        'file_name': shock_file['file']['name'],
                                        'remote_md5': shock_file['file']['checksum']['md5']})

        # 3) save to WS
        post_split_library = {
            'fasta': {
                'hid':file_handle,
                'file_name': shock_file['file']['name'],
                'id': shock_file['id'],
                'url': self.shockURL,
                'remote_md5':shock_file['file']['checksum']['md5'],
                'size':shock_file['file']['size']
            }
        }

        new_obj_info = self.ws.save_objects({
                        'workspace':self.getWsName(),
                        'objects':[
                            {
                                'type':'QIIME.PostSplitLibrary-0.1',
                                'data':post_split_library,
                                'name':'sequences.fasta',
                                'meta':{},
                                'provenance':[
                                    {
                                        'service':'QIIME',
                                        'method':'test'
                                    }
                                ]
                            }]
                        })
        self.__class__.postSplitLibInfo = new_obj_info[0]
        return new_obj_info[0]





