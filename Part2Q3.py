import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("Dataset/US_births_2000-2014_SSA.csv")
csvreader = csv.reader(f)

#skip the first header information line
next(csvreader)

year = np.array([])
date_of_month ={}
for i in range(1, 32):
    date_of_month[i] = 0

data = []
for row in csvreader:
    data.append(row)
    year = np.append(year, row[0])
    date_of_month[int(row[2])] = date_of_month[int(row[2])] + int(row[4])

## Finding the day with maximum birthdays
max_value = max(date_of_month.values())
max_keys = [k for k, v in date_of_month.items() if v == max_value]
print("The day with highest number of births is: %s and the birth count is %d"% (max_keys, max_value))

## Finding the day with lowest birthdays
min_value = min(date_of_month.values())
min_keys = [k for k, v in date_of_month.items() if v == min_value]
print("The day with lowest number of births is: %s and the birth count is %d"% (min_keys, min_value))

## Counting the number of birthdays on Friday the 13th

f_13 = sum(int(p[4]) for p in data if p[2] == '13' and p[3] == '5')
#print(friday13)
print("Number of Birthdays on Friday the 13th: %d" % f_13)

counter_summer = 0
counter_winter = 0

## Birthdays in Summer (May (Month 05)- August (Month 08) of every year)
counter_summer = sum(int(row[4]) for row in data if row[1] == '5' or row[1] == '6' or row[1] == '7' or row[1] == '8')

## Birthdays in Winter (November (Month 11)- February (Month 02) of every year)
counter_winter = sum(int(row[4]) for row in data if row[1] == '1' or row[1] == '2' or row[1] == '11' or row[1] == '12')

print("Number of Birthdays in Winter %d and number of Birthdays in Summers are %d. "
      "It can be concluded that winters have less births than summers." % (counter_winter, counter_summer))