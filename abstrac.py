from abc import ABC

class Car(ABC):
    
    def mileage(self):
        pass
        
    def model(self):
        print("All cars manufactured after 2020 have BS engine")
        
class Tesla(Car):
    def mileage(self):
        print("mileage is 30kmph")
        
class Volkswagen(Car):
    def mileage(self):
        print("mileage is 20kmpl")
        
class Renault(Car):
    def mileage(self):
        print("mileage is 24kmpl")   
        self.model()         
        
        
t1=Tesla()
t1.mileage()

v1=Volkswagen()
v1.mileage()

r1=Renault()
r1.mileage()    
    



            