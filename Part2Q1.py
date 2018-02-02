import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("Dataset/1880-2017.csv")
csvreader = csv.reader(f)

#skip the first 6 header information lines
for i in range(1, 6):
    next(csvreader)

year = np.array([])
value = np.array([])
valueF = np.array([])
#start copying the data from file to arrays
for row in csvreader:
    year = np.append(year, row[0])
    value = np.append(value, row[1])

year = year.astype(int)
value = value.astype(float)

#conversion of temperature values from celsius to fahrenheit
for i in range(0, len(value)):
    valueF = np.append(valueF,1.8*value[i] + 32)

##Draw histogram using Fahrenheit (Uncomment)
plt.bar(year, valueF, align='center', width=0.8)
plt.ylim((31,34))
plt.xlabel("Year")
plt.ylabel("F +/- from the average")
plt.title("Bar plot depicting Temperature Changes through years 1880-2017")

##Draw histogram using Celsius (Uncomment)
# plt.bar(year, value, align='center', width=0.8)
# plt.xlabel("Year")
# plt.ylabel("C +/- from the average")

plt.show()