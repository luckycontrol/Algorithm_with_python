import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

main_url = 'http://traders.ssg.com'
url = 'http://traders.ssg.com/category/list.ssg?dispCtgId=6000099314'
user_agent = 'Mozilla/5.0'
headers = {'User-Agent': user_agent }
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as res:
    soup = BeautifulSoup(res, 'html.parser')

    imgHrefDummy = soup.select('div.cunit_prod > div.thmb > a')

    for i, imgHref in enumerate(imgHrefDummy):
        imgSrc = imgHref.select_one('img')['src']
        urllib.request.urlretrieve(url=f'http://{imgSrc[2:]}', filename=f'./image/{i}.jpg')