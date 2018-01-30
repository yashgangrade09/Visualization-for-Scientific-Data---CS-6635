import csv
import numpy as np
import matplotlib.pyplot as plt
import us

'''
f = open("Dataset/p2q4d1.csv")
csvreader = csv.reader(f)

#skip the first header information line
next(csvreader)
data = []
state = []
for row in csvreader:
    state.append(row[5])
'''

###### Dataset 1 - Total Waterborne Commerce ######

##### Plot type - Bar Plot ######
def barplot_d1():
    f = open("Dataset/total_waterborne_commerce.csv")
    csvreader = csv.reader(f)
    csvreader = csv.reader(f)
    #skip the first header information line
    next(csvreader)
    data = []
    year = np.array([])
    tot = np.array([])
    foreign = np.array([])
    dom = np.array([])
    for row in csvreader:
        data.append(row)
        year = np.append(year, row[0])
        tot = np.append(tot, row[1])
        foreign = np.append(foreign, row[2])
        dom = np.append(dom, row[3])
    year = year.astype(int)
    tot = tot.astype(float)
    dom = dom.astype(int)
    foreign = foreign.astype(int)
    
    ## Plot the bar plots
    fig = plt.figure(figsize=(80, 20))
    ax = fig.add_subplot(111)
    r1 = ax.bar(year-0.2, foreign,width=0.2,color='b',align='center')
    r2 = ax.bar(year, dom,width=0.2,color='g',align='center')
    r3 = ax.bar(year+0.2, tot,width=0.2,color='yellow',align='center')
    ax.set_xticks(year)
    ax.autoscale(tight = True)
    ax.legend((r1, r2, r3), ('Foreign', 'Domestic', 'Total'), fontsize = 'large')
    plt.xlabel("Year")
    plt.ylabel("Total Commerce ( x 10^9")
    plt.show()

def lineplot_d1():
    f = open("Dataset/total_waterborne_commerce.csv")
    csvreader = csv.reader(f)
    csvreader = csv.reader(f)
    # skip the first header information line
    next(csvreader)
    data = []
    year = np.array([])
    tot = np.array([])
    foreign = np.array([])
    dom = np.array([])
    for row in csvreader:
        data.append(row)
        year = np.append(year, row[0])
        tot = np.append(tot, row[1])
        foreign = np.append(foreign, row[2])
        dom = np.append(dom, row[3])
    year = year.astype(int)
    tot = tot.astype(float)
    dom = dom.astype(int)
    foreign = foreign.astype(int)

    r1 = plt.plot(year, foreign, 'b--')
    r2 = plt.plot(year, dom, 'r*')
    r3 = plt.plot(year, tot, 'y-')
    plt.autoscale(tight = True)
    plt.legend((r1, r2, r3), ('Foreign', 'Domestic', 'Total'), fontsize = 'large')
    plt.xlabel("Year")
    plt.ylabel("Total Commerce ( x 10^9")
    plt.grid()
    plt.show()

def histogram_d1():
    f = open("Dataset/total_waterborne_commerce.csv")
    csvreader = csv.reader(f)
    csvreader = csv.reader(f)
    # skip the first header information line
    next(csvreader)
    data = []
    year = np.array([])
    tot = np.array([])
    foreign = np.array([])
    dom = np.array([])
    for row in csvreader:
        data.append(row)
        year = np.append(year, row[0])
        tot = np.append(tot, row[1])
        foreign = np.append(foreign, row[2])
        dom = np.append(dom, row[3])
    year = year.astype(int)
    tot = tot.astype(float)
    dom = dom.astype(int)
    foreign = foreign.astype(int)

    plt.hist(tot, bins=)
lineplot_d1()
