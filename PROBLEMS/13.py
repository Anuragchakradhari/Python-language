# greatest of three numbers
def greatest(a,b,c) :
    if(a>b and a>c):
        print("a is the greatest")
    elif(b>a and  b>c): 
        print("b is the greatest")
    else:
        print("c is the greatest")
        
greatest(3,9,2)