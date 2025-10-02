import matplotlib.pyplot as plt 
import numpy as np
data= np.random.normal(0,1,1000)
plt.hist(data, bins= 30, alpha = 0.7, color= 'blue', edgecolor='black')
plt.title('Histogram')
plt.ylabel('frequencies')
plt.xlabel('values')
plt.show()