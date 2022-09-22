def my_gen():
    n=1
    print("This is printed first")
    #generator function contains yield statement
    yield n
    
    n+=1
    print("This is printed second")
    yield n
    
    n+=2
    print("This is printed third time")
    yield n
    
result=my_gen()  
next(result)
next(result) 
next(result)
     