# Подготовка файлов торгов <txt> в формат для загрузки в SieeraChart

import os
import time

DOWNLOAD = 'F:\\Data\\Zerich\\'


def merge(down_dir):
    ' Конвертация файлов торгов <qsh> в текстовые файлы, типа <csv>'
    name_file = dir_int + '.txt'
    new_file = down_dir + '\\' + name_file
    new = 0
    for item in os.listdir(down_dir + '\\' + 'TXT'):
        with open(down_dir + '\\' + 'TXT' + '\\' + item, 'r') as files, open(new_file, 'a', encoding='utf-8') as fw:
            for n, line in enumerate(files):
                new_line = line.replace(' ', ';')
                if len(new_line) > 70:
                    date_d = new_line.split(';')[0]
                    time_d = new_line.split(';')[1]
                    order = new_line.split(';')[5]
                    price = new_line.split(';')[6]
                    volume = new_line.split(';')[7]
                    new_lines = date_d+';'+time_d+';'+order+';'+price+';'+volume+'\n'
                    fw.writelines(new_lines)
            new = new + n
    print("Число строк во всех файлах =", new)


if __name__ == '__main__':
    dir_int = input("Введите папку для конвертации (папка = тикер):")
    tic = time.perf_counter()
    merge(DOWNLOAD + dir_int)
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")
