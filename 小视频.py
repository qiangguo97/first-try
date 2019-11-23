import requests
from lxml import etree
import re
def get_url():
    url = 'http://699pic.com/video-64382.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }  # 模拟浏览器
    r = requests.get(url,headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.status_code)
    all_vido = re.findall(r'<div class="video-media" id="video-media" data-video-id="64382">(.*?)</div>',r.text,re.S)[0]
    # print(all_vido)
    all_shi = re.findall(r'src="(.*?)"',all_vido,re.S)[0]
    all = "http:%s"%all_shi
    # print(all)
    ship = requests.get(all)
    name = "小视频.mp4"
    f = open(name,'ab')
    f.write(ship.content)
    f.close()



if __name__ == "__main__":
    get_url()