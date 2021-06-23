import urllib.request
import urllib.response
from bs4 import BeautifulSoup

accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
host = 'm.traders.ssg.com'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'

headers = {
    'Accept': accept,
    'User-Agent': user_agent
}

url = 'http://emart.ssg.com/category/listCategoryItem.ssg?dispCtgId=6000096996&page=2'
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
soup = BeautifulSoup(res, 'html.parser')

imgDummy = soup.select('div.thmb > a > img')

for i, img in enumerate(imgDummy):
    urllib.request.urlretrieve(url=f'http:{img["src"]}', filename=f'./image/계란/1-{i}.jpg')

