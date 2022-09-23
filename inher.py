#creating base class

class Game:
    
    #public method
    def fun(self):
        print("Fun games from 9 - 5 and all allowed")
        
    #private method
    
    def __notfun(self):
        print("Dangerous game and strictly not allowed")   
        
        #accessing private method via public method
    def Help(self):
        self.__notfun()     

#creating derived class 1
        
#class Rollercoaster(Game) :
class Rollercoaster:
    
    # calls the base class public method
    def smallboats(self):
        print("kids game and is fun")
        self.Help()
        
      #calls the base class private method  
    def waterslide(self):
        print("Only adults with caution")
        self.__notfun()
 
 # creating derived class 2
 
class Watersplash(Game,Rollercoaster):
    
    def Speedboat(self):
        print("Allowed for adults only")
        self.smallboats()
        
    def slide(self):
        print("Kids below 6 are only allowed")   
        self.fun() 
    
 #creating objects for derived class1 and accessing its methods
        
#g1=Rollercoaster()
#g1.smallboats()
#g1.waterslide()

#creating object for derived class 2

w1=Watersplash()
w1.Speedboat()
w1.slide()

#g2=Game()

#g2.Help()

        
                  
    