# -*- coding: utf-8 -*
import hmac
import hashlib
import urllib
import sys
class GenerateSignUtils:
    """
    
    """
    def __init__(self,os):
        self.curr_os=os
        self.androidAppId = '3101819740'
        self.androidAppKey = 'A88HI53BJKTV'
        self.iOSAppId = '3201776428'
        self.iOSAppKey = 'IPI3G1YN69CE'
        self.methoad='GET'
    """
        genSign():
            1、
            2、
            3、
            4、
    """
    def genSign(self,url,params):
        app_key=''
        if self.curr_os == 'android':
            app_key = self.androidAppKey
        else:
            app_key = self.iOSAppKey
            
        methoad = self.methoad
        
        keys = params.keys()
        keys.sort()
        param = ''
        
        for k in keys:
            param += '&' + k + '=' + params[k]
        coded_param = urllib.quote_plus(param[1:])
        coded_url = urllib.quote_plus(url)
        
        urlString = methoad + '&' + coded_url
        signString = urlString + '&' + coded_param
        signHmac = hmac.new(app_key+'&', signString, hashlib.sha1).digest().rstrip()
        sign_md5 = hashlib.md5()
        sign_md5.update(signHmac)
        sign = sign_md5.hexdigest()
        return sign

"""
    params:
        argv[1] ： os (e:android/iOS)
        argv[2] ： idx (e:10501,10502)
        argv[3] ： err_ty (e:1)
        argv[4] ： start_date (e:2017-11-01)
        argv[5] ： end_date (e:2017-11-02)
        argv[6] ： url (e:/ctr_crash_anal/get_err_list)
"""     
if __name__ == "__main__":
    genSign = GenerateSignUtils(sys.argv[1])
    os=sys.argv[1]
    idx=sys.argv[2]
    err_ty=sys.argv[3]
    start_date=sys.argv[4]
    end_date=sys.argv[5]
    url=sys.argv[6]
    
    param_dict={'app_id':'','idx':'','err_ty':'','start_date':'','end_date':''}
    
    if os == "android":
        param_dict['app_id']=genSign.androidAppId
    else:
        param_dict['app_id']=genSign.iOSAppId
        
    param_dict['idx']=idx
    param_dict['err_ty']=err_ty
    param_dict['start_date']=start_date
    param_dict['end_date']=end_date

    sign = genSign.genSign(url,param_dict)
    print sign
