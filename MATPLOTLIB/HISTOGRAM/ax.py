import matplotlib.pyplot as plt 
import numpy as np
data= np.random.normal(0,1,1000)
fig, ax = plt.subplots()
ax.hist(data, bins= 30, alpha = 0.5, color= 'green', edgecolor='black')
ax.set_title('Histogram')
ax.set_ylabel('frequencies')
ax.set_xlabel('values')
plt.show()