import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open('death_valley_2018_simple.csv', 'r') as infile:
    csvfile = csv.reader(infile)
    header_row = next(csvfile)

    tmin_index = header_row.index('TMIN')
    tmax_index = header_row.index('TMAX')
    station_name = header_row[1]  

    highs = []
    dates = []
    lows = []

    for row in csvfile:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.plot(dates, highs, c='red', alpha=0.5)
    ax1.set_title(f'Daily High Temperatures - 2018\n{station_name}', fontsize=16)
    ax1.set_xlabel('Date', fontsize=16)
    ax1.set_ylabel('Temperature (F)', fontsize=16)
    ax1.tick_params(axis='both', which='major', labelsize=16)
    ax1.xaxis.set_major_formatter(plt.NullFormatter())

    ax2.plot(dates, lows, c='blue', alpha=0.5)
    ax2.set_title(f'Daily Low Temperatures - 2018\n{station_name}', fontsize=16)
    ax2.set_xlabel('Date', fontsize=16)
    ax2.set_ylabel('Temperature (F)', fontsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.xaxis.set_major_formatter(plt.NullFormatter())

    fig.autofmt_xdate()  

    plt.tight_layout()  
    plt.show()
