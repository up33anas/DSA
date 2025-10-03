import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dailyActivity_merged.csv')

# Filter data for 12th April 2016
daily_hours = df[df['ActivityDate'] == '2016-04-12']

plt.figure(figsize=(8,8))
plt.pie(daily_hours['Steps'], labels=daily_hours['Hour'], autopct='%1.1f%%', startangle=90)
plt.title('Hourly Steps on 12th April 2016')
plt.show()
