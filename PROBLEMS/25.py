class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square id {self.n*self.n}")   
        
    def cube(self):
        print(f"The square id {self.n*self.n*self.n}")      
    def sqrroot(self):
        print(f"The square id {self.n**1/2}")  
    
    @staticmethod
    def hello():
        print("hello there!!")
        
            
a= Calculator(4)
a.hello()
a.square()
a.cube()
a.sqrroot()