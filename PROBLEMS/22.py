class Programmer:
    company = "Microsoft"
    def __init__(self, name , salary, pin):
        self.name= name
        self.salary = salary
        self.pin = pin
        
        
        
p= Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)        
s= Programmer("Shubham", 1200000, 245001)
print(s.name, s.salary, s.pin, s.company)        