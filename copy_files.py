# Копирование файлов из папки в папку - отбор по названию
import os
import shutil

PATHNAME = 'F:\\Data\\Zerich\\'

mode_files = {'DEALS': 'Deals', 'AUXINFO': 'AuxInfo', 'QUOTES': 'Quotes'}


def has_year(year_path):
    if os.path.exists(PATHNAME + year_path):
        return 1


def what_mode(number):
    if int(number) == 1:
        return "Deals"
    elif int(number) == 2:
        return "Quotes"
    elif int(number) == 3:
        return "AuxInfo"


def copy_files(path_year, tiker, regime):
    """
        Копирование файлов из папки в папку - отбор по названию
    """
    path_name = PATHNAME + tiker + '\\'
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    new_path_name = path_name + path_year + '\\'
    if not os.path.exists(new_path_name):
        os.mkdir(new_path_name)
    new_mode_path = new_path_name + regime + '\\'
    if not os.path.exists(new_mode_path):
        os.mkdir(new_mode_path)
    for root, dirs, files in os.walk(PATHNAME + path_year + '\\'):
        for filename in files:
            if (filename[:4] == tiker) & (filename[16:-4] == regime):
                file = os.path.join(root, filename)
                print(file)
                shutil.copy(file, new_mode_path)


if __name__ == "__main__":
    year = input("Введите год:\n").upper()
    if has_year(year) is not None:
        stock = input("Введите тикер инструмента:\n").upper()
        auxinfo = input("Введите режим инструмента (Сделки-1, Стакан-2, Допы - 3):\n")
    else:
        exit("Нет такого года !!!")
    mode = what_mode(auxinfo)
    if mode is None:
        print("Вы ввели несуществующий режим !!!")
    else:
        copy_files(year, stock, mode)
