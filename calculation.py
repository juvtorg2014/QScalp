import pandas as pd
import time
import os

DOWNLOAD = 'F:\\Data\\Zerich\\'


def make_file(file):
    data = pd.read_csv(file, encoding='utf-8')
    pd.set_option('display.float_format', '{:,.2f}'.format)
    data['Summ'] = 0
    data['Id'] = ''
    data['Del'] = ''
    data['Summ'] = data['Summ'].astype(int)
    data.at[0, 'Summ'] = data.at[0, 'Volume']

# Установка меток для нахождения серийных сделок
    for num, row in data[1:].iterrows():
        p_time = data.at[num - 1, 'Time']
        p_deals = data.at[num - 1, 'Deals']
        p_price = data.at[num - 1, 'Price']
        if data.at[num, 'Time'] == p_time and \
                data.at[num, 'Deals'] == p_deals and \
                       data.at[num, 'Price'] == p_price:
            data.at[num, 'Summ'] = data.at[num, 'Volume'] + data.at[num - 1, 'Summ']
            data.at[num, 'Id'] = '+'
            if data.at[num - 1, 'Id'] == '-':
                data.at[num - 1, 'Id'] = '+'
        else:
            data.at[num, 'Summ'] = data.at[num, 'Volume']
            data.at[num, 'Id'] = '-'

# Установка меток для удаления серийных сделок
    for num, row in data[1:].iterrows():
        if num != len(data) - 1:
            f_time = data.at[num + 1, 'Time']
            f_deals = data.at[num + 1, 'Deals']
            f_price = data.at[num + 1, 'Price']
            if data.at[num, 'Id'] == '+':
                if data.at[num, 'Time'] == f_time and \
                        data.at[num, 'Deals'] == f_deals and \
                             data.at[num, 'Price'] == f_price:
                    data.at[num, 'Del'] = 'del'

    data = data.loc[data['Del'] != 'del']


# Удаление строк с одинаковыми сделками
    data = data.drop(['Del', 'Id', 'Volume'], axis=1)
# Переиндексация индексов в строках
    data2 = data.reset_index(drop=True, inplace=False, col_level=0, col_fill='')
    data2['Price'] = data2['Price'].astype(float)
    data2['Summ'] = data2['Summ'].astype(int)
# Вычисление средневзвешенной цены
    data2['pv'] = data2['Price'] * data2['Summ']
    data2['pv'] = data2['pv'].astype(float)
    data2['sum_pv'] = data2['pv'].rolling(min_periods=1, window=len(data2)).sum()
    data2['sum_summ'] = data2['Summ'].rolling(min_periods=1, window=len(data2)).sum()
    data2['VWAP'] = data2['sum_pv'] / data2['sum_summ']
    data2.loc[:, "VWAP"] = data2["VWAP"].map('{:.2f}'.format)
    data2 = data2.drop(['pv', 'sum_pv', 'sum_summ'], axis=1)

# Поиск разбора стакана с переходом страйка
    data2['Strike'] = ''
    for num, row in data2[1:].iterrows():
        p_time = data2.at[num - 1, 'Time']
        p_deals = data2.at[num - 1, 'Deals']
        p_price = data2.at[num - 1, 'Price']
        if data2.at[num, 'Time'] == p_time and data2.at[num, 'Deals'] == p_deals:
            if data2.at[num, 'Price'] != p_price:
                data2.at[num, 'Strike'] = '+'




# Сохранение результатов в файл
    data2['Price'] = data2['Price'].astype(float)
    data2['Summ'] = data2['Summ'].astype(int)
    data2['VWAP'] = data2['VWAP'].astype(float)
    data2.to_csv(file[:-4] + '_new.csv', index=False)



# Агрегация по идентификатору
# agr = data.groupby(['Id'])['Volume'].sum()
# Объединение с группированами данными
# data3 = data2.merge(agr, left_on='Id', right_on='Id')


if __name__ == '__main__':
    # dir_int = input("Введите папку для расчета сделок в файлах:\n")
    file_int = "SBER"
    tic = time.perf_counter()
    print('Ждем-с, господа ...')
    make_file(DOWNLOAD + file_int + '.csv')
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")