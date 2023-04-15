import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([22, 35, 34, 45, 50])

model1 = np.poly1d(np.polyfit(x, y, 1))
model2 = np.poly1d(np.polyfit(x, y, 2))

time_to_predict = 12
print((model1(time_to_predict) + model2(time_to_predict)) / 2)
