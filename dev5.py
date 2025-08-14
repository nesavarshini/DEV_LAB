import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seasonal_decompose
import plot_acf, plot_pacf
df =pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily- min-temperatures.csv")
df.columns = ['Date', 'Temperature']
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
plt.figure(figsize=(14,5))
plt.plot(df['Temperature'], label='Daily Min Temperature')
plt.title('Daily Minimum Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
monthly_avg = df['Temperature'].resample('ME').mean()
plt.figure(figsize=(14,5))
plt.plot(monthly_avg, color='orange', label='Monthly Average Temperature')
plt.title('Monthly Average Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()

result = seasonal_decompose(df['Temperature'], model='additive', period=365)

result.plot()
plt.show()
plot_acf(df['Temperature'], lags=50)
plt.show()
plot_pacf(df['Temperature'], lags=50)
plt.show()
df['Year'] = df.index.year
df['Month'] = df.index.month
pivot_table = df.pivot_table(values='Temperature', index='Month', columns='Year', aggfunc='mean')
plt.figure(figsize=(12,6))
sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt=".1f")
plt.title('Monthly Average Temperature Heatmap')
plt.show()
print(df.head())
