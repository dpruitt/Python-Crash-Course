import csv
import matplotlib.pyplot as plot
from datetime import datetime


filename = './data/death_valley_2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plot.style.use('seaborn')
fig, ax = plot.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plot.title("Daily high and low temperatues - 2018", fontsize=24)
plot.xlabel('', fontsize=16)
fig.autofmt_xdate()
plot.ylabel("Temperature (F)", fontsize=16)
plot.tick_params(axis="both", which="major", labelsize=16)

plot.show()