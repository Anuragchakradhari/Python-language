import matplotlib.pyplot as plt
categories = ['A','B','C','D']
values= [23,54,60,7]
fig, ax= plt.subplots(figsize= (8,5))
ax.bar(categories, values, color = "lightgreen")
ax.set_xlabel('categories')
ax.set_ylabel('values')
ax.set_title('Scatter Plot')
plt.show()