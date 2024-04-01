import pyshark
import numpy as np
import matplotlib.pyplot  as plt
import sys
from colorama import Fore

filename = "traces/native/startup.pcapng"

print(f"{Fore.GREEN}loading data")
cap = pyshark.FileCapture(filename)
cap.load_packets(0)

print("processing data")

length_array = np.zeros(len(cap))

for i in range(len(cap)):
    length_array[i] = int(cap[i].length)
infos_occurence = np.asarray(np.unique(length_array, return_counts=True)).T

tolerance = 5 #tolerance pour le pourcentage des catégories de taille de paquets
size_array = []
occurence_array = []

for pakcet_size, occurence in infos_occurence:
    percentage = occurence/len(cap)
    if percentage > tolerance/100:
        size_array.append(pakcet_size)
        occurence_array.append(occurence)
    else:
        size_step_label=[
            [0,100,"0-100"],
            [100,500,"100-500"],
            [500,1000,"500-1000"],
            [1000,5000, "1000-5000"],
            [5000, sys.maxsize, "5000+"]
        ]
        for step in size_step_label:
            if pakcet_size >= step[0] and pakcet_size < step[1]:
                if step[2] in size_array:
                    occurence_array[size_array.index(step[2])] += occurence
                else:
                    size_array.append(step[2])
                    occurence_array.append(occurence)
                break

print("plotting data :)")
plt.figure("Longueur des paquets")
plt.title("Pourcentage des paquets en fonction de leur taille")
plt.pie(occurence_array, labels=size_array, autopct='%1.1f%%', colors=plt.cm.tab20.colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
plt.show()