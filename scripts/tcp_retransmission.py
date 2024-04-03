import matplotlib.pyplot as plt
import numpy as np

datas_4g_time, datas_4g_error = np.loadtxt('./plots/datas/tcp_retransmission4g.csv', delimiter=',', unpack=True, skiprows=1)
datas_ethernet_time, datas_ethernet_error = np.loadtxt('./plots/datas/tcp_retransmissionethernet.csv', delimiter=',', unpack=True, skiprows=1)

print("Ethernet stats :")
print("Mean : {} retransmission/sec".format(np.sum(datas_ethernet_error)/datas_ethernet_time[-1]))
print("Transmission time : {} sec\n".format(datas_ethernet_time[-1]))

print("4G stats :")
print("Mean : {} retransmission/sec".format(np.sum(datas_4g_error)/datas_4g_time[-1]))
print("Transmission time : {} sec".format(datas_4g_time[-1]))

plt.figure("TCP Retransmission")
plt.bar(datas_4g_time, datas_4g_error, label='4G')
plt.bar(datas_ethernet_time, datas_ethernet_error, label='4G')
plt.show()