import matplotlib.pyplot as plt
import numpy as np

datas_4g_time, datas_4g_error = np.loadtxt('./plots/datas/tcp_retransmission_4g.csv', delimiter=',', unpack=True, skiprows=1)
datas_ethernet_time, datas_ethernet_error = np.loadtxt('./plots/datas/tcp_retransmission_ethernet.csv', delimiter=',', unpack=True, skiprows=1)
datas_wifi_time, datas_wifi_error = np.loadtxt('./plots/datas/tcp_retransmission_wifi.csv', delimiter=',', unpack=True, skiprows=1)

file_size = 49 #mb

print("Ethernet stats :")
print("Mean : {} retransmission/sec".format(np.sum(datas_ethernet_error)/datas_ethernet_time[-1]))
print("Transmission time : {} sec".format(datas_ethernet_time[-1]))
print("Rate of transfer : {} mb/sec".format(file_size/datas_ethernet_time[-1]))

print("\n")

print("4G stats :")
print("Mean : {} retransmission/sec".format(np.sum(datas_4g_error)/datas_4g_time[-1]))
print("Transmission time : {} sec".format(datas_4g_time[-1]))
print("Rate of transfer : {} mb/sec".format(file_size/datas_4g_time[-1]))

print("\n")

print("Wifi stats :")
print("Mean : {} retransmission/sec".format(np.sum(datas_wifi_error)/datas_wifi_time[-1]))
print("Transmission time : {} sec".format(datas_wifi_time[-1]))
print("Rate of transfer : {} mb/sec".format(file_size/datas_wifi_time[-1]))

plt.figure("TCP Retransmission")
plt.bar(datas_4g_time, datas_4g_error, label='4G')
plt.bar(datas_ethernet_time, datas_ethernet_error, label='ethernet')
plt.bar(datas_wifi_time, datas_wifi_error, label='wifi')
plt.show()