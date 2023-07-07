import os
import time

DOWNLOAD = 'F:\\Data\\Zerich\\'


def to_sierra(down_dir):
    new_file = down_dir + '\\' + dir_int + '.csv'
    if os.path.exists(down_dir + '\\' + dir_int + '.txt'):
        with open(down_dir + '\\' + dir_int + '.txt', 'r', encoding='utf-8') as fr,  \
                                          open(new_file, 'w', encoding='utf-8') as fw:
            for line in fr:
                if 'Sell' or 'Buy' in line:
                    date_d = line.split(';')[0]
                    time_d = line.split(';')[1]
                    price = line.split(';')[3]
                    volume = line.split(';')[4]
                    volume = volume.replace('\n', '')
                    tr = '1'
                    if line.split(';')[2] == 'Sell':
                        bid = volume
                        ask = "0"
                    elif line.split(';')[2] == 'Buy':
                        bid = "0"
                        ask = volume
                    prices = price + ';' + price + ';' + price + ';' + price + ';'
                    new_line = date_d+';'+time_d+';'+prices+volume+';'+tr+';'+bid+';'+ask+'\n'
                    fw.writelines(new_line)
                    print(new_line)


if __name__ == '__main__':
    # dir_int = input("Введите папку для конвертации:")
    dir_int = "SBER"
    tic = time.perf_counter()
    to_sierra(DOWNLOAD + dir_int)
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")
