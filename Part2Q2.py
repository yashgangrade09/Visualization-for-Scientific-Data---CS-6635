import csv
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import us



def StarPlot_State_Age(avg_age, data):
    #### Work for Star Plot Starts ####
    N = len(data)

    x_as = [n / float(N) * 2 * pi for n in range(N)]

    # Because our chart will be circular we need to append a copy of the first
    # value of each list at the end of each list with data
    avg_age += avg_age[:1]
    x_as += x_as[:1]


    # Set color of axes
    plt.rc('axes', linewidth=0.5, edgecolor="#888888")


    # Create polar plot
    ax = plt.subplot(111, polar=True)


    # Set clockwise rotation. That is:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)


    # Set position of y-labels
    ax.set_rlabel_position(0)


    # Set color and linestyle of grid
    ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


    # Set number of radial axes and remove labels
    plt.xticks(x_as[:-1], [])

    # Set yticks
    plt.yticks([48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], ["48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"])


    # Plot data
    ax.plot(x_as, avg_age, linewidth=0, linestyle='solid', zorder=3)

    # Fill area
    ax.fill(x_as, avg_age, 'b', alpha=0.3)


    # Set axes limits
    plt.ylim(0, 100)


    # Draw ytick labels to make sure they fit properly
    for i in range(N):
        angle_rad = i / float(N) * 2 * pi

        if angle_rad == 0:
            ha, distance_ax = "center", 10
        elif 0 < angle_rad < pi:
            ha, distance_ax = "left", 1
        elif angle_rad == pi:
            ha, distance_ax = "center", 1
        else:
            ha, distance_ax = "right", 1

        ax.text(angle_rad, 100 + distance_ax, data[i], size=10, horizontalalignment=ha, verticalalignment="center")
    plt.title("Star plot depicting average age of politicians from each state")
    # Show polar plot
    plt.show()


### Main function starts
f = open("Dataset/congress-terms.csv")
csvreader = csv.reader(f)
# Skip the header information
next(csvreader)

data = []
avg_age = []
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

# We will store only essential information in different arrays like
# Average age of politicians from each state

for key in state_age:
    data.append(key)
    avg_age.append(state_age[key]/state_age_count[key])

StarPlot_State_Age(avg_age, data)