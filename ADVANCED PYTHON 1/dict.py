dict1 = {'a': 1, 'b':2 , 'c':3}
dict2 = {'c': 5, 'd': 6, 'e':7}

merged = dict1 | dict2 
print(merged) #Output will be {'a':1, 'b':2 , 'c':5, 'd': 6, 'e': 7}