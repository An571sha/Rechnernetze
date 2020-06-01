import matplotlib.pyplot as plt

total_round_trip_time = []
s = 'Reply'


class ReadPingTXT:
    with open('result_DE.txt', encoding='utf-16') as f:
        lines = f.read().splitlines()
    for line in lines:
        if line.__contains__("Reply"):
            trimmed_string = line.split(':')[-1].strip()
            byte, round_trip, max_ttl = trimmed_string.split()
            end = round_trip.split('=')[-1].strip()
            total_round_trip_time.append(int(end.replace("ms", "").strip()))

    print(total_round_trip_time)


class Plot:
    plt.plot(total_round_trip_time)
    plt.show()
    print("end")
