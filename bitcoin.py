# import data and convert unix value to date time
import pandas as pd
bitcoin = pd.read_csv('C:/python_data/bitcoin.csv')
bitcoin['Timestamp'] = pd.to_datetime(bitcoin['Timestamp'], unit = 's')
bitcoin['Timestamp'] = pd.to_datetime(bitcoin['Timestamp']).dt.date

# subset of bitcoin which contains data from 2021 only
bitcoin21 = bitcoin[(bitcoin['Timestamp']>pd.Timestamp(2021,1,1))]


import matplotlib.pyplot as plt
# plot 1
plt.subplot(2,2,1)
plt.title("Bitcoin Open Price")
bitcoin21_daily = bitcoin21.groupby(by=["Timestamp"], dropna=False).mean()
bitcoin21_daily = bitcoin21_daily.reset_index()
plt.plot(bitcoin21_daily['Timestamp'],bitcoin21_daily['Open'])
# plot 2
plt.subplot(2,2,2)
plt.title("Bitcoin High Price")
plt.plot(bitcoin21_daily['Timestamp'], bitcoin21_daily['High'])
# plot 3
plt.subplot(2,2,3)
plt.title("Bitcoin Low Price")
plt.plot(bitcoin21_daily['Timestamp'], bitcoin21_daily['Low'])
# plot 4
plt.subplot(2,2,4)
plt.title("Bitcoin Close Price")
plt.plot(bitcoin21_daily['Timestamp'], bitcoin21_daily['Close'])

plt.show()

