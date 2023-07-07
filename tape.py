import os
import pandas as pd
import numpy as np



DOWNLOAD = 'F:\\Data\\Zerich\\SBER\\'
name = ['Date', 'Time', 'Order', 'Price', 'Volume']

lenta = pd.read_csv(DOWNLOAD+'SBER.txt', delimiter=';', names=name)
print(lenta.head(10))
print(lenta.tail(10))