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


def get_data(number):
    r = requests.post('https://allnumber.cc/get.php', data={'number': number})
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
