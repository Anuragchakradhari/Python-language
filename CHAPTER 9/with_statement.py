'''f = open("file.txt")  #by default the mode is in read mode 
data= f.read()
print(data)
f.close()
'''
# The same can be written using with statement like this:
with open("file.txt") as f :
    print(f.read())
    
# Now you dosnt need to close() the file 