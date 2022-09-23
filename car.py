"""class car:
    carname="vento"
    price=12345
    year=2012
    
    def show(self):
        print(self.carname)
        print(self.price)
        print(self.year)
 
c1=car()
c1.show()


# deleting object or fileds 

del c1.carname
del c1

c1.show()"""

class car:
    
     #constructor definition here
     
    def __init__(self):
        print("This is a first empty constructor")
        
    def __init__(self):
        print("This is a second empty constructor")    
        

    
c1=car()   
c2=car()     
#c1=car("Polo",345678,2010)

#c1.display()      


"""def __init__(self,carname,price,year):
        self.carname=carname
        self.price=price
        self.year=year
        
    def display(self):
        print(self.carname)
        print(self.price)
        print(self.year)"""
    