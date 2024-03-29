import numpy as np
import matplotlib.pyplot as plt
import pickle

## Part 1 - Question 1
x1 = np.arange(1, 101, 1) #Create an array with 100 elements in order
#print(x)
plt.figure(1)
# plt.subplot(211)
plt.boxplot(x1)
plt.ylabel("Values ")
plt.title("Boxplot of an array of size with 1 to 100 in order")

## Part 1 - Question 2
x2 = np.random.rand(1,100)
x2 = np.transpose(x2)
plt.figure(2)
# plt.subplot(212)
plt.hist(x2, bins=20)
plt.ylabel("Random Values ")
plt.xlabel("Bins (Automatic Binning)")
plt.title("Histogram of 10000 Random numbers from Uniform Distribution")

## Part 1 - Question 3
# Took reference from python documentation for injecting data into binary filesoutput_file =
output_file = open("P1Q3.bin", "wb")
plt.figure(3)
# plt.subplot(211)
x3 = np.random.uniform(1,100,100)
pickle.dump(x3, output_file) #special library pickle to ease up the process of writing and reading binary files
plt.plot(x1, x3)
plt.xlabel("Instances ranging from 1 - 100")
plt.ylabel("Values of random variables")
plt.title("Line Plot of 100 Random Numbers with values ranging from 1 to 100")
output_file.close()

## Part 1 - Question 4
input_file = open("P1Q3.bin", "rb")
x4 = pickle.load(input_file)
plt.figure(4)
# plt.subplot(212)
n, bins, patches = plt.hist(x4, bins=[0,14, 28, 42, 56, 70, 84, 100], histtype='stepfilled')
plt.ylabel("Frequency")
plt.xlabel("Different Bins")
plt.xticks([0,14, 28, 42, 56, 70, 84, 100])
plt.title("Histogram of the data read from the file and divided into 7 bins")

print("The intervals and frequencies considered here are: ")
for i in range(1, len(bins)):
    if i == 1:
        print("Interval %d : 0 - %d -> %d\n" % (1, bins[i], n[i-1]))
    elif i + 1 == len(bins):
        print("Interval %d : %d - 100 -> %d\n " % (7, bins[i-1], n[i-1]))
    else:
        print("Interval %d : %d - %d -> %d\n" % (i, bins[i-1], bins[i], n[i-1]))

input_file.close()

## Plot the figures
plt.show()

