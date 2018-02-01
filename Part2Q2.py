import csv
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import us

f = open("Dataset/congress-terms.csv")
csvreader = csv.reader(f)
# Skip the header information
next(csvreader)

data = []
state_age = {}
state_age_count = {}
for row in csvreader:
    # print(row[8])
    if row[8] not in state_age:
        state_age[row[8]] = float(row[12])
        state_age_count[row[8]] = 1
    else:
        state_age[row[8]] += float(row[12])
        state_age_count[row[8]] += 1
    # if state_age[row[8]] == 0:
    #
    #     state_age[row[8]] = float(row[12])
    # else:
    #     state_age[row[8]] = state_age[row[8]] + float(row[12])

print(state_age)
print(state_age_count)

for key in state_age:
    print(key, state_age[key]/state_age_count[key])
# We will store only essential information in different arrays like
# Average age of politicians from each state

