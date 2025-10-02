class Employee:
    company = "ITC"
    name = "Raghav"
    salry= 20000
    def show(self):
        print(f"The namne of the employee is {self.name} an dthe salry is {self.salry}")
        
class Programmer(Employee) :
    company = "ITC infotech"
    language = "Python"
    def showlanguage(self) :
        print(f" The Company is {self.company} and he is good with {self.language} language")
        
        
a = Employee()
b = Programmer()

print(a.company,b.company)

a.show()
b.show()
b.showlanguage()       