import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def tempcalmultisethardcode(values , time):
  temperatures = {}
  for i in range(len(values)):
      temperatures[i] = values[i][0] * (time ** 2) + values[i][1] * time + values[i][2]
  return temperatures


time_values = np.linspace(0 , 10 , 50)
values = {
    0 : [0.02, 1.5, 20],
    1 : [0.01, 2, 18],
    2 : [0.03, 1, 25]
}
temperatures = tempcalmultisethardcode(values , time_values)
for i in range(len(temperatures)):
    plt.plot(time_values , temperatures[i] , label = "set" + str(i+1) + ' : ' + ' , '.join(map(str , values[i])))
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for Multi-set Hard code inputs')
plt.show()