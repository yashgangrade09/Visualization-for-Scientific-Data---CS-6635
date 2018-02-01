import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("Dataset/congress-terms.csv")
csvreader = csv.reader(f)
# Skip the header information
next(csvreader)

data = []
for row in csvreader:
    data.append(row)

print(data)