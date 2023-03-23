# - *- coding: utf- 8 - *- 
import pandas as pd 
import matplotlib.pyplot as plt


max_temps = pd.read_csv('part-00000', delimiter='\t', header=None, names=['year', 'avgtemp', 'maxtemp', 'mintemp'])


plt.plot(max_temps['year'], max_temps['maxtemp'] /10, marker="o")
plt.plot(max_temps['year'], max_temps['avgtemp'] /10, marker="o")
plt.plot(max_temps['year'], max_temps['mintemp'] /10, marker="o")

plt.title('Nhiệt độ cao nhất ghi nhận được theo từng năm ')
plt.xlabel('Năm')
plt.ylabel('Nhiệt độ ($^\circ$C)')

plt.show()
