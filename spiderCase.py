import requests
import os
import pymysql
from requests_html import HTMLSession

session = HTMLSession()
host = 'http://www.zhishabang.cn/'


def download(url):
    r = requests.get(host + url)
    with open(url, 'wb') as f:
        f.write(r.content)


def getUrls(imgs):
    for i in imgs:
        urls = i.attrs['src'].split('/')
        file_dir = 'uploads/allimg/' + urls[3]
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        url = file_dir + '/' + urls[4]
        download(url)

def getOneUrl(imgs):
    urls = imgs.split('/')
    file_dir = 'uploads/' + urls[2]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    url = file_dir + '/' + urls[3]
    download(url)


'''
数据库操作
'''
# 打开数据库连接
db = pymysql.connect("39.105.191.239", "fastadmin", "fastadmin", "fastadmin", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

'''
产品采集
46条信息
'''
newList = []
T = []
for i in range(46):
    try:
        id = i + 1
        url = host + '/case/' + str(id) + '.html'
        resbonContent = session.get(url).html
        thumb = resbonContent.find('.focus img', first=True).attrs['src']
        title = resbonContent.find('.pro_title h1', first=True).text
        liao = resbonContent.find('.sx_0 span', first=True).text
        power = resbonContent.find('.sx_1 span', first=True).text
        desc = resbonContent.find('.sx_2', first=True).text
        desc = desc.replace('：', '')
        product = resbonContent.find('.pro-title', first=True).html
        imgs = resbonContent.find('.pro-title img')
        # 下载图片
        # getUrls(imgs)
        # getOneUrl(thumb)
        T.append([title, thumb, liao, power, desc, product])
        print('第' + str(id) + '处理成功')
    except:
        print('第'+str(id)+'数据错误=================================')

# SQL 插入语句
sql = "INSERT INTO fa_case(title, image, jinliao, productpower, information, content) VALUES (%s,%s,%s,%s,%s,%s)"
# 一个tuple或者list
cursor.executemany(sql, T)
db.commit()  # 只要是修改了表内容的操作，后面一定要提交，否则不起作用
# 关闭数据库连接
db.close()
