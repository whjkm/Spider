import requests
import os
from lxml import etree
import urllib.request

def parse_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    # print(response.text)
    html = etree.HTML(response.text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class != 'gif']")
    for img in imgs:
        # print(etree.tostring(img))
        img_url = img.get('data-original')
        img_url = img_url.replace("!dta", "")
        # print(img_url)
        alt = img.get('alt')      # 获取图片名字
        # print(alt)
        suffix = os.path.splitext(img_url)[1]  # 对url进行分割，得到后缀名
        filename = alt + suffix
        # print(filename)
        urllib.request.urlretrieve(img_url, r'H:/images/'+ filename)  # 保存图片

def main():
    url = "https://www.doutula.com/photo/list/?page=2"
    parse_page(url)


if __name__ == "__main__":
    main()

