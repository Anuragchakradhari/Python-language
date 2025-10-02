import matplotlib.pyplot as plt
x= [2,5,3,8,9,4]
y= [0,5,4,5,3,8]
fig, ax = plt.subplots()
ax.scatter(x,y,color = 'black',label= 'Data Points')
ax.set_title('Scatter plot')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
plt.show()