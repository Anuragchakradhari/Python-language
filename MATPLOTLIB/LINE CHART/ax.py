import matplotlib.pyplot as plt
time = [1,2,3,4,5,6]
values = [20,65,78,0,12,67]
fig, ax= plt.subplots()
ax.plot(time, values, marker='o')
ax.set_xlabel('time')
ax.set_ylabel('values')
ax.set_title('Line chart')
plt.show()