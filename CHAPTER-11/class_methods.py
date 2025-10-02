class Employee:
    a=1
    # def show(self):
    #     print(f"The value of a is {self.a}")        here the output will be 45 because self
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")      # here the output will be 1 because of class method
           
e= Employee()
e.a = 45 
e.Show()       