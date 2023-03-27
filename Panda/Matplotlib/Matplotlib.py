import matplotlib.pyplot as plt
import numpy as np


# ex1:
# plt.plot([1,2,3],[2,3,4])
# plt.show()

# ex2:

x1 = [10,5,40]
y1 = [23,45,89]

x2 = [30,7,45]
y2 = [5,8,9]

plt.bar(x1,y1)
# plt.plot(x2,y2,label='Second')
plt.legend() # add Label NavBox
plt.show()