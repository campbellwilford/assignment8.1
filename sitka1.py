import csv

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(header_row)

for index, col in enumerate(header_row):
    print (index,col)

highs = []

for row in csvfile:
    highs.append(int(row[5]))

print(highs[:5])

import matplotlib.pyplot as plt

plt.plot(highs, c='red')
plt.title('Daily high temperatures, July 2018', fontsize = 16)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperatures (F)', fontsize = 16)
plt.tickparams(axis = 'both', which = 'major', labelsize = 16)

plt.show()


