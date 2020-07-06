#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填
sckey = 'SCU104607T640b5c34020361870ddf16d2f813df265f0329a22511c'
cookie = '__cfduid=d759102f672690cf8527fea8014437b5c1593932142; _ga=GA1.2.1312965143.1593932149; _gid=GA1.2.848935626.1594042977; koa:sess=eyJ1c2VySWQiOjQyNjgzLCJfZXhwaXJlIjoxNjE5OTYyOTkwNDA4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=beDUK17Rp_VjRKYkIsQ0SfhUqfE'


def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
