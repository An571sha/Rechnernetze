import matplotlib.pyplot as plt
import numpy as np

total_avg_time = []
total_min_time = []
total_max_time = []
paket_size = np.arange(100, 1500, 100).tolist()


class ReadMeanTXT:
    with open('result_mean.txt', encoding='utf-8') as f:
        lines = f.read().splitlines()
    for line in lines:
        average = line.split('=')[-1].strip()
        print(average)
        total_avg_time.append(int(average.replace("ms", "").strip()))

    print(total_avg_time)


class Plot:
    plt.plot(paket_size, total_avg_time, 'ro')
    plt.show()
    print("end")
