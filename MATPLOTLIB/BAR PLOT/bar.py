import matplotlib.pyplot as plt
categories = ['a','b','c']
values = ['3','9','6']
plt.figure(figsize=(8,9))  # for the size of the terminal that open after running the program
plt.bar(categories, values, color= 'skyblue')
plt.title('Bar plot')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()