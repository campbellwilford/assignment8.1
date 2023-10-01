import csv
from datetime import datetime 

infile = open('death_valley_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(header_row)

for index, col in enumerate(header_row):
    print (index,col)

highs = []
dates = []
lows = []

#as an example
first_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(type(first_date))

for row in csvfile:
    try:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(current_date)

print(highs[:5])

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates,highs, c='red', alpha = 0.5)
plt.plot(dates,lows, c='blue', alpha = 0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperatures - 2018\nDeath Valley', fontsize = 16)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperatures (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

fig.autofmt_xdate()

plt.show()

plt.subplot(2,1,1)
plt.plot(dates,highs,color='red')
plt.title('Highs')

plt.subplot(2,1,2)
plt.plot(dates,lows,color='blue')
plt.title('Lows')

plt.suptitle('Highs and Lows of Sitka, Alaska 2018')

plt.show()
