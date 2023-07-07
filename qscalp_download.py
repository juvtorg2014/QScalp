import urllib
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

DOWNLOAD_DIR = 'F:\\Data\\Zerich\\'
URL_DOWN = 'http://erinrv.qscalp.ru/'
#  Пример папки на сайте = 2021-05

# Поиск директорий на странице


def read_url(dir):
    url = URL_DOWN.replace(" ", "%20")
    req = Request(URL_DOWN)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    dir_list = []
    for i in x:
        file_name = i.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ", "%20")
        if (file_name[-1] == '/') and (file_name[0] != '.'):
            read_url(url_new)
        # print(url_new.split('/')[3][:7])
        if url_new.split('/')[3][:7] == dir:
            dir_list.append(url_new)
    return dir_list


def download_files(sub_dir):
    """
    Закачка данных торгов с сайта 'http://erinrv.qscalp.ru/'
    """
    url_new = URL_DOWN + sub_dir[-10:] + '/'
    year_sub = sub_dir[-10:][:4]

    down_year = DOWNLOAD_DIR + year_sub
    if not os.path.exists(down_year):
        os.mkdir(down_year)
        print('Создана папка: ' + down_year)

    down_month = down_year + '\\' + sub_dir[24:31]
    if not os.path.exists(down_month):
        os.mkdir(down_month)
        print('Создана папка: ' + down_month)

    down_day = down_month + '\\' + sub_dir[24:]
    if not os.path.exists(down_day):
        os.mkdir(down_day)
        print('Создана папка: ' + down_day)

    html_content = requests.get(url_new)
    soup = BeautifulSoup(html_content.content, 'html.parser')
    f_links = soup.findAll('a')

    for file_name in f_links:
        if file_name.text.endswith('qsh'):
            url_file = url_new + file_name.text
            if not os.path.exists(down_day + '\\' + file_name.text):
                urllib.request.urlretrieve(url_file, down_day + '\\' + file_name.text)
                print("Скачен файл " + down_day + '\\' + file_name.text)
            else:
                print("Файл", down_day + '\\' + file_name.text, "уже скачан")


if __name__ == '__main__':
    sub_dir = input("Введите папку для сайта 'http://erinrv.qscalp.ru/' типа '2020-06':\n")
    subdir = read_url(sub_dir)
    for item in subdir:
        download_files(item)
    print("Все скачано за {} месяц ".format(item[29:31]))
