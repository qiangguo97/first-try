import requests
from lxml import etree
from bs4 import BeautifulSoup

def get_url():
    url = 'http://www.dili360.com/gallery/cate/4.htm'
    # headers = {}
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    print(r.status_code)
    # print(r.text)
    Soup = BeautifulSoup(r.text,'lxml')
    # all_a = Soup.find('div',class_='img').find_all('a')
    all_a = Soup.find_all('img')[3:]
    for a in all_a:
        # print(a)
        first = a.get('src')
        name = a.get('alt')
        # print(name)
        # print(first)
        img = requests.get(first)
        if name:
            f = open(name + '.jpg','ab')
            f.write(img.content)
            f.close()

if __name__ == "__main__":
    get_url()
