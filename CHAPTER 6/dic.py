marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}
print(marks, type(marks))

# dictionary is mutable
# it is indexed

# METHODS OF DICTIONARY
print(marks.items()) #gives key valuse as list in the form of tuple
print(marks.keys())  #print the key values like rohan, shubham...
print(marks.values())#print the key values like 100, 56...

marks.update({"Harry": 99}) #update marks od harry from 100 to 99
print(marks)
print(marks.get("Harry"))