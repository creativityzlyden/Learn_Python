import requests
import csv
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from datetime import datetime
from random import uniform
from multiprocessing import Pool
from threading import Thread

def get_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('div', class_='cmc-table--sort-by__rank').find_all('div', class_='cmc-table__column-name')
    links = []

    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1').text.strip()
    except:
        name = ' '
    try:
        price = soup.find('span', class_='cmc-details-panel-price__price').text.strip()
    except:
        price = ' '  
    data = {'name': name, 
            'price': price}
    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['price']))
        print(data['name'], data['price'], 'parsed')


def send_proxy():
    url = 'https://coinmarketcap.com/all/views/all/'

    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')

    for i in range(10):
        b = uniform(3, 6)
        sleep(b)
        proxy = {'http': 'https://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        get_html(url, proxy, useragent)


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all/'

    all_links = get_all_links(get_html(url))

    with Pool(1) as p:
        p.map(make_all, all_links)

    end = datetime.now()
    total = end - start
    print(str(total))


if __name__ == '__main__':
    main()

threadA = Thread(target=send_proxy())
threadB = Thread(target=main())
threadA.run()
threadB.run()

threadA.join()
threadB.join()