# C = 5*(f-32)/9  fehrenhite to celsius 
def convert(f):
    return 5*(f-32)/9
    
f = int(input("Enter the temperature: "))
print(f"{convert(f)} Degree C")