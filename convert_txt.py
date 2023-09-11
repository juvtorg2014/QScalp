# Конвертирование файлов <qsh> в файлы <txt> и копирование их в отдельные папки>
import os
import subprocess
import time
import shutil


def convert(down_dir):
    if os.path.exists(down_dir):
        cur_dir = down_dir + '\\'
    else:
        os.mkdir(down_dir)
        cur_dir = down_dir + '\\'
        
    filenames = []
    for root, dirs, files in os.walk(down_dir):
        for file in files:
            if '.qsh' in file:
                filenames.append(root + '\\' + file)

    if os.path.exists(os.getcwd() + '\\' + 'qsh2txt.exe'):
        for item in filenames:
            subprocess.Popen([os.getcwd() + '\\' + 'qsh2txt.exe', item])
            time.sleep(3)
    elif os.path.exists(cur_dir + 'qsh2txt.exe'):
        for item in filenames:
            subprocess.Popen([cur_dir + 'qsh2txt.exe', item])
            time.sleep(3)
    else:
        print(f"Нет файла 'qsh2txt.exe' в папке {os.getcwd()} и папке {cur_dir} ")
        
        
def copy_files(path_dir) -> str:
    curr_dir = path_dir + '\\TXT'
    if not os.path.exists(curr_dir):
        os.mkdir(curr_dir)
        
    for root, dirs, files in os.walk(path_dir):
        for file in files:
            if '.txt' in file:
                try:
                    shutil.move(os.path.join(root, file), curr_dir + '\\' + file)
                    print(f"Перемещен файл {file}")
                except OSError as e:
                    print(e)
    return curr_dir


def sort_files(dir_path):
    dir_AuxInfo = dir_path + '\\AuxInfo'
    dir_Deals = dir_path + '\\Deals'
    dir_Quotes = dir_path + '\\Quotes'
    
    if not os.path.exists(dir_AuxInfo):
        os.mkdir(dir_AuxInfo)
    if not os.path.exists(dir_Deals):
        os.mkdir(dir_Deals)
    if not os.path.exists(dir_Quotes):
        os.mkdir(dir_Quotes)
        
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if 'AuxInfo' in file:
                shutil.move(os.path.join(root, file), dir_AuxInfo + '\\' + file)
                print(f"Перемещен файл {file} в папку {dir_AuxInfo}")
            elif 'Deals' in file:
                shutil.move(os.path.join(root, file), dir_Deals + '\\' + file)
                print(f"Перемещен файл {file} в папку {dir_Deals}")
            elif 'Quotes' in file:
                shutil.move(os.path.join(root, file), dir_Quotes + '\\' + file)
                print(f"Перемещен файл {file} в папку {dir_Quotes}")
            else:
                print(f"Нет файлов 'txt' в папке {dir_path}")
        




if __name__ == '__main__':
    dir_int = input("Введите папку для конвертации:\n")
    tic = time.perf_counter()
    dir_path = os.getcwd() + '\\' + dir_int.upper()
    convert(dir_path)
    time.sleep(3)
    dir_txt = copy_files(dir_path)
    time.sleep(3)
    sort_files(dir_txt)
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")