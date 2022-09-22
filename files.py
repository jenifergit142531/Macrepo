#import os

filename="/Users/jenifery1409icloud.com/Desktop/Demos/pydemos3/files/newfile.txt"

try:
    with open(filename,'r') as fr:
        
        #read the file line by line
        lines=fr.readlines()
        
        #pointer for position
        ptr=1
        
        #opening file in write mode
        with open(filename,'w') as fw:
            for line in lines:
                if line.strip('\n')!='sunday':
                # ptr!=4:
                 fw.write(line)
                    
                ptr+=1
                    
            print("specific content is deleted")
                    
except:
    print("error.....")
















#os.remove(filename)
#os.rmdir(filename)
#f=open(filename,'w')
#f.write("Hello everyone ...we are talking about the file handling concepts in python")
#f.write("We are using \"w\"to write the contents to the file")
#print(f.read())
#f.write("clear all")
#print("Content is appended in the file")

