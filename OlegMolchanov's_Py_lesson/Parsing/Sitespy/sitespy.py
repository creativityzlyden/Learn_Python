import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform


def get_html(url, useragent=choice, proxy=choice):
    r = requests.get(url, headers=useragent, proxies=proxy)
    print(proxy)
    return r.text


def get_ip(html):
    print('New proxy & User-Agent:')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)
    print('--------------------')


def main():
    url = 'http://sitespy.ru/my-ip'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies.txt').read().split('\n')

    for i in range(20):
        a = uniform(3, 6)
        sleep(a)
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        html = get_html(url, useragent, proxy)



if __name__ == '__main__':
    main()
