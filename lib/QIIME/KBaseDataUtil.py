
import os
import json
import time
import requests

from requests_toolbelt import MultipartEncoder

'''
'''
class KBaseDataUtil:



    def __init__(self):
        pass



    def download_file_from_shock(self,
                                 shock_service_url = None,
                                 shock_id = None,
                                 filePath = None,
                                 token = None):

        if token is None:
            raise Exception("Authentication token required!")
        if shock_service_url is None:
            raise Exception("shock_service_url is required!")
        if shock_id is None:
            raise Exception("shock_id is required!")
        if filePath is None:
            raise Exception("filePath is required!")

        file_location = os.path.join(filePath)
        file = open(file_location, 'w', 0)
        #print('downloading reads file: '+str(forward_reads_file_location))
        headers = {'Authorization': 'OAuth ' + token }
        r = requests.get(shock_service_url+'/node/'+shock_id+'?download', stream=True, headers=headers)
        for chunk in r.iter_content(1024):
            file.write(chunk)
        file.close();


    # Helper script borrowed from the transform service, logger removed
    def upload_file_to_shock(self,
                             shock_service_url = None,
                             filePath = None,
                             ssl_verify = True,
                             token = None):
        """
        Use HTTP multi-part POST to save a file to a SHOCK instance.
        """

        if token is None:
            raise Exception("Authentication token required!")

        #build the header
        header = dict()
        header["Authorization"] = "Oauth {0}".format(token)

        if filePath is None:
            raise Exception("No file given for upload to SHOCK!")

        dataFile = open(os.path.abspath(filePath), 'rb')
        m = MultipartEncoder(fields={'upload': (os.path.split(filePath)[-1], dataFile)})
        header['Content-Type'] = m.content_type

        #logger.info("Sending {0} to {1}".format(filePath,shock_service_url))
        try:
            response = requests.post(shock_service_url + "/node", headers=header, data=m, allow_redirects=True, verify=ssl_verify)
            dataFile.close()
        except:
            dataFile.close()
            raise

        if not response.ok:
            response.raise_for_status()

        result = response.json()

        if result['error']:
            raise Exception(result['error'][0])
        else:
            return result["data"]