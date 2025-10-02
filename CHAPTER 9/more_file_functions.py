f= open("file.txt")
# line= f.readlines()   # makes a list of the lines
line=f.readline() 
while(line!= ""):
    print(line)
    line=f.readline()
# print(line, type(line))
f.close()