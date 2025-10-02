import matplotlib.pyplot as plt
x= [2,5,3,8,9,4]
y= [0,5,4,5,3,8]
plt.scatter(x,y,color = 'red',label= 'Data Points')
plt.title('Scatter plot')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()