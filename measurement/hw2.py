import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel('PSP_20081005.xls', header=0, usecols=[0, 1, 2, 3], names=['Time', 'PSP3', 'PSP4', 'PSP7'])
Time, PSP3, PSP4, PSP7 = data.iloc[:, 0].values, data.iloc[:, 1].values, data.iloc[:, 2].values, data.iloc[:, 3].values
n = len(Time)


#linewidth = 0.75
time=np.linspace(0,24,1390)
plt.plot(time,PSP3, label = 'PSP 300-3000 nm', color = 'red')
plt.plot(time,PSP4, label = 'PSP 400-3000 nm', color = 'green')
plt.plot(time,PSP7, label = 'PSP 700-3000 nm', color = 'blue')
plt.legend()
plt.xlabel('time (min)')
plt.ylabel('solar radiation[W/m$^2$]')
#x_labels = [str(i) for i in range(0, 24)]
#x_ticks = np.arange(0, len(Time), 61)
#plt.xlim(0,1440)
#plt.xticks(x_ticks, x_labels)
plt.title('PSP_20081005 @25.01476, 121.53898')
filename='hw2_1.png'
plt.savefig(filename)
plt.show()