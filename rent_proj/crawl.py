from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import time

url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

page = 0

csv_file = open("rent.csv", "w")
# 创建writer对象，指定文件与分隔符
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print('fetch:', url.format(page=page))    # 通过page设置抓取的页面
    response = requests.get(url.format(page=page))      # 抓取目标页面
    html = BeautifulSoup(response.text, "html.parser")    # 使用python内置解析器，用lxml可能会出错
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = urljoin(url, house.select("a")[0]["href"])
        # house_url = "http://bj.58.com/%s" % (house.select(("a")[0]["href"]))
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if '公寓' in house_info_list[1] or '青年社区' in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        csv_writer.writerow([house_title, house_location, house_money, house_url])

        if page % 30 == 0:
            time.sleep(3)      # 暂停执行3秒

csv_file.close()
