class Demo:
    a=4
    
o= Demo()
print(o.a) # Printsthe class attribute because instance attribute is not present
o.a = 0
print(o.a)    # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute , becaus eonly instance changes here not the class attribute 
