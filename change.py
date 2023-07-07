# Агрегация сделок с помощью Pandas
import os
import pprint
import time
import pandas as pd




DOWNLOAD = 'F:\\Data\\Zerich\\'


def change_file(new_file):
    df = pd.read_csv(new_file, encoding='utf-8')
    df['id'] = ''
    df['Summ'] = ''
    headers = df.head()

    #all_volume = df.groupby("Volume").count()
    index = 1
    print('№', '       Time', 'Deal', 'Vol', 'id')
    "Присвоение разбитым сделкам общего индекса"
    for number, row in df[1:].iterrows():
        past_time = df.at[number-1, 'Time']
        past_deals = df.at[number-1, 'Deal']
        if df.at[number, 'Time'] == past_time and df.at[number, 'Deal'] == past_deals:
            if number > 2:
                past_past_time = df.at[number - 2, 'Time']
                past_past_deals = df.at[number - 2, 'Deal']
                if df.at[number, 'Time'] != past_past_time or df.at[number, 'Deal'] != past_past_deals :
                    index += 1
            row['id'] = index
            #print(number, row['Time'], row['Deal'][0], 'Vol=' + str(row['Vol']), row['id'])

    'Метод собирания сделок в крупные объемы'
    for number, row in df.iterrows():
        summ = 0
        if number > 1:
            if df.at[number, 'id'] == df.at[number-1, 'id']:
                # groups = df['id'].groupby(df['Vol']).groups
                # for number, group in enumerate(groups):
                #     print(group[number])
                summ += df.at[number, 'Vol']
                row['Summ'] = summ
            print(number, row['Time'], row['Deal'][0], row['Vol'], row['id'], row['Summ'])

    #print(data_first.describe())



if __name__ == '__main__':
    # file_int = input("Введите файл для агрегации (без расширения):\n").upper()
    file_int = "SBER"
    tic = time.perf_counter()
    change_file(DOWNLOAD + file_int + '.csv')
    time_stop = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - tic))
    print(f"Все сделано за {time_stop} !!!")