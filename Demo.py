a=input("Enter the A value : ")
b=input("Enter the B value :")
try:
    c=a/b
except ArithmeticError:
    print("divide by zero error")
else:
    print("Output :",c)
finally:
    print("Finally done")

"""filename="/Users/jenifery1409icloud.com/Desktop/Demos/pydemos/notes/sample.txt"
try:
     f=open(filename,'w')
     try:
         f.write("hello")
     except:
         print("Unable to write")
     finally:
         f.close()
except:
         print("unable to open the file")"""
        
        
    