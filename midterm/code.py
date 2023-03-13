import numpy as np
import matplotlib.pyplot as plt
# load the text file using numpy's loadtxt function
data = np.loadtxt('output2.txt')

# print the loaded data
print(data)

# access the columns of the numpy array
column1 = data[:, 0]
column2 = data[:, 1]

# print the columns
print(column1)
print(column2)

plt.plot(column1, column2)
plt.show()
