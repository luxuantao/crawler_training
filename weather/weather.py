from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request

url = "http://www.weather.com.cn/weather/101170401.shtml"

try:
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    data = urllib.request.urlopen(req)
    data = data.read()
    dammit = UnicodeDammit(data, ['utf-8', 'gbk'])
    data = dammit.unicode_markup
    soup = BeautifulSoup(data, 'lxml')
    lis = soup.select("ul[class='t clearfix'] li")
    for li in lis:
        try:
            date = li.select('h1')[0].text
            weather = li.select('p[class="wea"]')[0].text
            temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
            print(date, weather, temp)
        except Exception as err:
            print(err)
except Exception as err:
    print(err)
