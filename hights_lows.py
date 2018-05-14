import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = r'C:\Users\doctor GONG\Desktop\kk.csv'
with open(file_name) as csv_file:
	spam_reader = csv.reader(csv_file)

	dates, highs, lows = [], [], []
	for row in spam_reader:
		try:
			current_date = datetime.strptime(
				row[0], '%Y-%m-%d'
			)
			high = int(row[1])
			low = int(row[2])
		except ValueError:
			print(current_date, 'Missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# 绘图
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 两个函数之间上色
plt.fill_between(
	dates, highs, lows,
	facecolor='blue', alpha=0.1
)
# 设置格式
plt.title('Daily high temperature, July 2014', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
