# 抓取身份证上前六位对应的行政区划代码
# 接口貌似被屏蔽了，备用

import urllib.request
import os
from bs4 import BeautifulSoup
import config as c

catch_url = "http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html"
file_path = c.outputs_documents_path
file_name = 'id_card_area_code.txt'

headers = {
    'Referer': 'http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/',
    'Host': 'www.stats.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36 '
}


def catch_city_code():
    code_list = []
    city_list = []
    req = urllib.request.Request(catch_url, headers=headers)
    resp = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(resp, 'html.parser')
    p = soup.findAll('p', attrs={'class': 'MsoNormal'})
    for i in p:
        spans = i.findAll('span', attrs={'lang': 'EN-US'})
        for span in spans:
            code_list.append(span.get_text().strip())
        spans = i.findAll('span', attrs={'style': 'font-family: 宋体'})
        for span in spans:
            city = span.get_text().strip()
            if len(city) > 0:
                city_list.append(city)
    save_to_file(code_list, city_list)


def save_to_file(code_list, city_list):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    try:
        with open(file_path + file_name, "w+", encoding='utf-8') as f:
            for i in range(len(code_list)):
                f.write(code_list[i] + ":" + city_list[i] + "\n")
    except OSError as reason:
        print(str(reason))
    else:
        print("文件写入完毕！")


if __name__ == '__main__':
    catch_city_code()
