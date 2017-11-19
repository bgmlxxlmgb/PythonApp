# -*- coding: utf-8 -*
import hmac
import hashlib
import urllib
class GenerateSignUtils:
    def __init__(self):
        #   global variable
        self.androidAppId = '3101819740'
        self.androidAppKey = 'A88HI53BJKTV'
        self.iOSAppId = '3201776428'
        self.iOSAppKey = 'IPI3G1YN69CE'
        self.methoad='GET'

    #url = '/ctr_crash_anal/get_err_list'
    #params={'app_id':app_id,'idx':'10501,10502','err_ty':'1','start_date':'2017-11-01','end_date':'2017-11-02'}
    def genSign(self,url,params):
        app_key = self.androidAppKey
        methoad = self.methoad
        #   initial variable
        keys = params.keys()
        keys.sort()
        param = ''
        #   sort keys in nature
        for k in keys:
            param += '&' + k + '=' + params[k]
        coded_param = urllib.quote_plus(param[1:])
        coded_url = urllib.quote_plus(url)
        #   concat params
        urlString = methoad + '&' + coded_url
        signString = urlString + '&' + coded_param
        signHmac = hmac.new(app_key+'&', signString, hashlib.sha1).digest().rstrip()
        sign_md5 = hashlib.md5()
        sign_md5.update(signHmac)
        sign = sign_md5.hexdigest()
        return sign

if __name__ == "__main__":
    genSign = GenerateSignUtils()
    url='/ctr_crash_anal/get_err_list'
    params={'app_id':genSign.androidAppId,'idx':'10501,10502','err_ty':'1','start_date':'2017-11-01','end_date':'2017-11-02'}
    genSign = GenerateSignUtils()
    sign = genSign.genSign(url,params)
    print sign
