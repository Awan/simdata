#!/usr/bin/env python
# coding: utf-8


print('''

In the name of Allah, the most Gracious, the most Merciful.

 ▓▓▓▓▓▓▓▓▓▓
░▓ Author ▓ Abdullah <https://abdullah.today>
░▓▓▓▓▓▓▓▓▓▓
░░░░░░░░░░

░█▀█░█░█
░█▀█░█▀▄
░▀░▀░▀░▀

''')

import requests
from bs4 import BeautifulSoup


proxies = {
        'https': 'http://103.144.201.112:8080',
        'https': 'http://203.81.91.80:8080',
        'https': 'http://152.26.66.140:3128',
        'https': 'http://51.79.79.111:3128',
        'https': 'http://168.169.96.2:8080',
        'https': 'http://64.235.204.107:8080',
        'https': 'http://142.44.243.113:3128',
        'https': 'http://136.243.133.76:3128'
        }

def get_data(number):
    r = requests.post('https://allnumber.cc/get.php', data={'number': number}, proxies=proxies)
    soup = BeautifulSoup(r.content, 'html.parser')
    for data in soup.find_all('td'):
        print(data.get_text())

while True:
    try:
        number = input('Enter Mobile or CNIC: ')
        get_data(number)
        print('------------------')
    except ValueError:
        print("Not available")
