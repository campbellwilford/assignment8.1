import csv
from datetime import datetime 

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(header_row)

for index, col in enumerate(header_row):
    print (index,col)

highs = []
dates = []

#as an example
first_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(type(first_date))

for row in csvfile:
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)

print(highs[:5])

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates,highs, c='red')
plt.title('Daily high temperatures, July 2018', fontsize = 16)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperatures (F)', fontsize = 16)
plt.tickparams(axis = 'both', which = 'major', labelsize = 16)

fig.autofmt_xdate_xdate()

plt.show()


