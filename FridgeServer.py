# -*- coding: UTF-8 -*-

from flask import Flask,redirect,url_for,request
import json
import time

input_info_Buf=[]


app=Flask(__name__)


@app.route('/',methods=['GET'])
def main_page():
    return redirect(url_for('static',filename='index.html'))

@app.route('/data/',methods=['POST'])
def dataprocess():
    if request.method=='POST':

        content= request.get_json()
        content['timestamp']=time.time()
        if input_info_Buf==[]:
            input_info_Buf.append(content)
        else:
            if time.time()-input_info_Buf[-1]['timestamp']>=5:
                input_info_Buf.append(content)
            else:
                return '请勿频繁操作',403
        return '正在打印',200
    else:
        return request.method



@app.route('/printer/',methods=['GET'])
def printer():
    try:
        temp=input_info_Buf[0]
        del input_info_Buf[0]
        return json.dumps(temp)
    except:
        return 'empty'
