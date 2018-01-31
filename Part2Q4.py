import csv
import numpy as np
import matplotlib.pyplot as plt
import us

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

##### Plot type - Line Plot ######
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

##### Plot type - Pie Graph ######
def piechart_d1():
    f = open("Dataset/total_waterborne_commerce.csv")
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

    # plt.hist(tot)
    # fig1, ax1 = plt.subplots()
    plt.pie(tot, labels=year, autopct='%1.1f%%',startangle=90)
    plt.axis('equal')
    plt.title("Pie Chart depicting total sales every year from 1974 - 2013")
    plt.show()

###### Dataset 2 - Total Waterborne Commerce ######
def barplot_d2():
    f = open("Dataset/FSIS-Recall-Summary-2014.csv")
    csvreader = csv.reader(f)

    for i in range(8):
        next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)
    # print(data)

    pounds = []
    recallclass = {'0': 0, '1': 0, '2': 0}
    c1 = 0
    c2 = 0
    c3 = 0
    for row in data:
       #print(row[5].replace(",",""))
        if row[2] == 'I':
            c1 += int(row[5].replace(",",""))
            recallclass['0'] = c1
        if row[2] == "II":
            c2 += int(row[5].replace(",",""))
            recallclass['1'] = c2
        else:
            c3 += int(row[5].replace(",",""))
            recallclass['2'] = c3
    print(recallclass)
    plt.bar(range(len(recallclass)), list(recallclass.values()), align='center')
    plt.xticks(range(len(recallclass)), list(recallclass.keys()))
    plt.show()

def pieplot_d2():
    f = open("Dataset/FSIS-Recall-Summary-2014.csv")
    csvreader = csv.reader(f)

    for i in range(8):
        next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)
    # print(data)

    pounds = []
    recallclass = {'0': 0, '1': 0, '2': 0}
    c1 = 0
    c2 = 0
    c3 = 0
    for row in data:
        # print(row[5].replace(",",""))
        if row[2] == 'I':
            c1 += int(row[5].replace(",", ""))
            recallclass['0'] = c1
        if row[2] == "II":
            c2 += int(row[5].replace(",", ""))
            recallclass['1'] = c2
        else:
            c3 += int(row[5].replace(",", ""))
            recallclass['2'] = c3
        counter = True
        if counter == True:
            plt.pie([float(v) for v in recallclass.values()], labels = [k for k in recallclass.keys()], autopct='%1.1f%%',startangle=90 )
            plt.axis('equal')
            counter = False
        plt.show()

# Run for Dataset 1
# lineplot_d1()
# piechart_d1()
# barplot_d1()

# Run for Dataset 2
# barplot_d2()
pieplot_d2()

