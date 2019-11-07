from requests_html import HTMLSession
import requests
import pymysql
import os

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


'''
数据库操作
'''
# 打开数据库连接
db = pymysql.connect("39.105.191.239", "fastadmin", "fastadmin", "fastadmin", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

"""
新闻采集
415条信息
"""
newList = []
T = []
for i in range(415, 445):
    try:
        id = i + 1
        url = host + '/article/' + str(id) + '.html'
        resbonContent = session.get(url)
        title = resbonContent.html.find('.news_detail h1', first=True).text
        # time = resbonContent.html.find('.news_detail .news_time time', first=True).text
        content = resbonContent.html.find('.news_sub p')
        imgs = resbonContent.html.find('.news_sub img')
        getUrls(imgs)
        contentHtml = ''
        for i in range(len(content)):
            if i != 0:
                contentHtml += content[i].html
        T.append([title, contentHtml])
        print('第'+str(id)+'成功√')
    except:
        print('第'+str(id)+'条失败===================')
# SQL 插入语句
sql = "INSERT INTO fa_article(title,content) VALUES (%s,%s)"
# 一个tuple或者list
cursor.executemany(sql, T)
db.commit()  # 只要是修改了表内容的操作，后面一定要提交，否则不起作用
# 关闭数据库连接
db.close()
