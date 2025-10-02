import matplotlib.pyplot as plt
portions= [ 15,45,30,10]
names = ['a','b','c','d']
plt.pie(portions, labels= names, autopct= '%1.1f%%')
plt.title('Pie Chart')
plt.show()