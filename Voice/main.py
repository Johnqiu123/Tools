# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:26:31 2017

@author: Administrator

App ID: 10000105
API Key: iHColMGU8Sg5ixGnL7HgtU6Q
Secret Key: 38d6dd69e17b3a0154d4d0d159c1ca88
"""

# 引入Speech SDK
from aip import AipSpeech

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__=="__main__":
    # 定义常量
    APP_ID = '10000105'
    API_KEY = 'iHColMGU8Sg5ixGnL7HgtU6Q'
    SECRET_KEY = '38d6dd69e17b3a0154d4d0d159c1ca88'
    
    filepath = "test31.wav"
    print filepath
    # 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY) 
        
    # 识别本地文件
    content = aipSpeech.asr(get_file_content(filepath), 'wav', 8000, {
        'lan': 'zh',
    })
    
    print content["result"][0]
    
