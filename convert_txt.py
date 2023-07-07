# Конвертирование файлов <qsh> в файлы <txt>
import os
import subprocess
import time


DOWNLOAD = 'F:\\Data\\Zerich\\'


def convert(down_dir):
    dir_end = os.listdir(down_dir)
    for item in dir_end:
        subprocess.Popen([DOWNLOAD + 'qsh2txt.exe', down_dir + '\\' + item])
    if not os.path.exists(down_dir + '\\' + 'TXT'):
        os.mkdir(down_dir + '\\' + 'TXT')

    for item in os.listdir(down_dir):
        if item[-3:] == 'txt':
           os.replace(down_dir + '\\' + item, down_dir + '\\' + 'TXT' + '\\' + item)



if __name__ == '__main__':
    #dir_int = input("Введите папку для конвертации:")
    dir_int = "SBER"
    tic = time.perf_counter()
    convert(DOWNLOAD + dir_int)
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")