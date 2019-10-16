#!/user/bin/python
#-*- coding:utf-8 -*-
import requests
import json
import time

def toDo():
    host = "http://www.ting56.com/player/tingchina.php"
    for i in range(0,499):
        try:
            postData = {'url':"yousheng/21179/play_21179_"+ str(i) +".htm"};
            re = requests.post(host,postData)
            url = json.loads(re.text)['url']
            re = open('list.txt','a')
            re.write(url + "\n")
            print('第'+ str(i) +'次执行成功')
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(3)
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
            time.sleep(3)


toDo()