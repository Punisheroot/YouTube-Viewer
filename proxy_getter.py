import requests
import socket
import ipaddress
from time import time, sleep
from datetime import date, datetime
import sched
import proxyscrape
import os
import proxy_getter
import re
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from proxy_check import  load


def client(sc, count):
    
    proxies = []
    
    #1
    collector = proxyscrape.create_collector('my-collector{}'.format(count), 'http')  # Create a collector for http resources
    for item in collector.get_proxies():
        proxies.append('{}:{}'.format(item.host, item.port))
    
    #2 scraper
    scrapper = Scrapper(category='ALL', print_err_trace=False)
    for item in scrapper.getProxies().proxies:
        proxies.append('{}:{}'.format(item.ip, item.port))
    
    #3
    # url = "http://pubproxy.com/api/proxy?limit=10"
    
    # t_end = time() + 30
    # while time() < t_end:
    #     json = requests.get(url)
    #     print(json)
    #     for item in json['data']:
    #        proxies.append(item['ipPort'])

    #4
    url = "https://sunny9577.github.io/proxy-scraper/proxies.json"
    json = requests.get(url).json()
    for item in json['proxynova']:
        proxies.append('{}:{}'.format(item['ip'], item['port']))
    
    
    proxies = list(dict.fromkeys(proxies))
    
    file = open('pl1.txt', 'w')
    file.write("\n".join(proxies))
    file.close()
    print('Proxy inseriti con successo!\nQuantita: {}'.format(len(proxies)) , datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    load(file='pl1.txt')
    s.enter(60 * 10, 1, client, (sc,))

def valid_ip(address):
    try: 
        #socket.inet_aton(address)
        ipaddress.ip_address(address)
        return True
    except:
        return False

if __name__ == "__main__":
    s = sched.scheduler(time, sleep)
    count = 0;
    s.enter(0, 1, client, (s, count))
    s.run()
    # while True:
    #     client()
    #     sleep(60 - time() % 60)