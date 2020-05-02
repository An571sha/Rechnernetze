import threading
import datetime
from time import sleep
from Realzeitsimulation.Customer import Customer
from Realzeitsimulation.Station import Station
from Realzeitsimulation.Task import Task

DIVISOR = 10

kill = threading.Event()

baecker = Station("Bäcker", 10)
wursttheke = Station("Metzger", 30)
kaesetheke = Station("Käsetheke", 60)
kasse = Station("Kasse", 5)

baecker.start()
wursttheke.start()
kaesetheke.start()
kasse.start()

customers = []

customers_lock = threading.Lock()


def init_customers(sleep_timer, name, tasks):
    a = 1
    while not kill.isSet():
        k = Customer(f"{name}{a}", tuple(tasks))
        k.start()
        a += 1
        customers_lock.acquire()
        customers.append(k)
        customers_lock.release()
        sleep(sleep_timer // DIVISOR)


tasks_type1 = [Task(baecker, 10, 10, 10), Task(wursttheke, 30, 5, 10), Task(kaesetheke, 45, 3, 5),
               Task(kasse, 10, 30, 20)]
tasks_type2 = [Task(wursttheke, 30, 2, 5), Task(kasse, 30, 3, 20), Task(baecker, 20, 3, 20)]

customer_type1 = threading.Thread(target=init_customers, args=(200, "A", tasks_type1))
customer_type2 = threading.Thread(target=init_customers, args=(60, "B", tasks_type2))

simulationTime_start = datetime.datetime.now()

customer_type1.start()

sleep(1 // DIVISOR)

customer_type2.start()

sleep((30*60)/DIVISOR)

kill.set()

customer_type1.join()
customer_type2.join()

for k in customers:
    k.join()

simulationTime_end = datetime.datetime.now()

print(f"Simulationsende: {(simulationTime_end - simulationTime_start).total_seconds()}s")
print(f"\n\nAnzahl Kunden: {len(customers)}")
vollständige_einkäufe = len(list(filter(lambda e: len(e.skipped_tasks) == 0, customers)))
print(f"Anzahl vollständige Einkäufe: {vollständige_einkäufe}")

average_shopping_time = 0
for k in customers:
    average_shopping_time += (k.time_end - k.time_start).total_seconds()
average_shopping_time /= len(customers)
print(f"Durchschnitliche Einkaufsdauer: {average_shopping_time}s")

average_shopping_time_completed = 0
for k in list(filter(lambda e: len(e.skipped_tasks) == 0, customers)):
    average_shopping_time_completed += (k.time_end - k.time_start).total_seconds()
average_shopping_time_completed /= len(customers)
print(f"Duchschnitliche Einkaufsdauer (vollständig): {average_shopping_time_completed}s")

all_skipped_stations = []
for x in customers:
    skipped_stations = list(map(lambda e: e.station, x.skipped_tasks))
    all_skipped_stations.extend(skipped_stations)

dropped_at_Bäcker = len(list(filter(lambda e: e.name == "Bäcker", all_skipped_stations)))
dropped_at_Wursttheke = len(list(filter(lambda e: e.name == "Wursttheke", all_skipped_stations)))
dropped_at_Käsetheke = len(list(filter(lambda e: e.name == "Käsetheke", all_skipped_stations)))
dropped_at_Kasse = len(list(filter(lambda e: e.name == "Kasse", all_skipped_stations)))

if len(all_skipped_stations) > 0:
    print(f"Drop percentage at Bäcker: {dropped_at_Bäcker / len(all_skipped_stations)}")
    print(f"Drop percentage at Wursttheke: {dropped_at_Wursttheke / len(all_skipped_stations)}")
    print(f"Drop percentage at Käsetheke: {dropped_at_Käsetheke / len(all_skipped_stations)}")
    print(f"Drop percentage at Kasse: {dropped_at_Kasse / len(all_skipped_stations)}")



baecker.killEv.set()
wursttheke.killEv.set()
kaesetheke.killEv.set()
kasse.killEv.set()
