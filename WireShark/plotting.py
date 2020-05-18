import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('data.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[1]))
        y.append(int(row[5]))


plt.plot(x, y, 'bo')
#ax3.margins(x=0, y=-0.25)

plt.title('Data from the CSV File: Paket size and Time')

plt.xlabel('Time')
plt.ylabel('Paket size in Bytes')

plt.show()
