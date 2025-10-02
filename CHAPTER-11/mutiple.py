class Employee:
    company = "ITC"
    name = "Raghav"
    salry= 20000
    def show(self):
        print(f"The namne of the employee is {self.name} an dthe salry is {self.salry}")
class Coder:
    language= "Python"
    def printlanguages(self):
        print(f"Out of all langaugea here is your language: {self.language}")
               
class Programmer(Employee, Coder) :
    company = "ITC infotech"
    def showlanguage(self) :
        print(f" The name of Company is {self.company} and he is good with {self.language} language")
        
a = Employee()
b = Programmer()
c= Coder()

b.show()
b.printlanguages()
b.showlanguage()        