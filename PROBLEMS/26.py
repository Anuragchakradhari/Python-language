from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def Book(self, fro, to ):
        print(f"Ticket is booked in train no. {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train no. :{self.trainNo} is running on time ")
        
    def getFare(self,  fro, to ):   # from is a defined keyword in python so we use fro only in place of from 
        print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(222,5555)} ")
        
t = Train(12399)
t.Book("Rampur", "Delhi")    
t.getStatus()
t.getFare("Rampur", "Delhi")    