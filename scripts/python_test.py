import pyshark
import numpy as np
import matplotlib.pyplot  as plt

cap = pyshark.FileCapture("traces/transfert_1_fichier.pcapng")
cap.load_packets(0)

length_array = np.zeros(len(cap))

print("loading data")

for i in range(len(cap)):
    length_array[i] = int(cap[i].length)

print("processing data")
lenghts = np.unique(length_array, return_counts=True)

plt.figure("Longueur des paquets")
plt.pie(lenghts[1], labels=lenghts[0], autopct='%1.1f%%')
plt.show()