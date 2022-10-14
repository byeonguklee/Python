import requests
from bs4 import BeautifulSoup #웹 크롤링 하는 법 (+셀리늄 or BeautifulSoup)

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozila/5.0', # 어떤 브라우저인지
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1, target2), headers = headers)

    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', [{'data-test': 'instrument-price-last'}])

    print(containers.text)

get_exchange_rate('usd','krw')