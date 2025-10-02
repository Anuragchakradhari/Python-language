# function definitioṇ
def avg():
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    average= (a+b)/2
    print(average)
# function call    
avg()    

# functions with argument
def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)
    return "ok"   #return value
    
goodDay("harrry" , "Thank You")
goodDay("Rohan" , "Thank You")
goodDay("Divya" , "Thanks")    


