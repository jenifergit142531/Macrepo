import sqlite3

def deleteTable():
 try:
   sqliteConnection = sqlite3.connect('Film.db')
   cursor=sqliteConnection.cursor()
   print("Successfully connected to database")
   
   create_query="""delete from film where id=101"""
   result=cursor.execute(create_query)
   sqliteConnection.commit()
   
   print("Record is deleted successfully")
   cursor.close()
   
 except sqlite3.Error as error:
  print("Error while connecting to the database",error)
    
 finally:   
    if sqliteConnection:
     sqliteConnection.close()
     print("The connection is closed")
  
deleteTable()
 

def updateTable():
 try:
   sqliteConnection = sqlite3.connect('Film.db')
   cursor=sqliteConnection.cursor()
   print("Successfully connected to database")
   
   create_query="""update film set fname='batman' where id=101"""
   result=cursor.execute(create_query)
   sqliteConnection.commit()
   
   print("Record is updated successfully")
   cursor.close()
   
 except sqlite3.Error as error:
  print("Error while connecting to the database",error)
    
 finally:   
    if sqliteConnection:
     sqliteConnection.close()
     print("The connection is closed")
  
#updateTable()

def insertTable():
 
 try:
   sqliteConnection = sqlite3.connect('Film.db')
   cursor=sqliteConnection.cursor()
   print("Successfully connected to database")
   
   create_query="""insert into film(id,fname,tprice) values (101,'Avatar',200)"""
   result=cursor.execute(create_query)
   sqliteConnection.commit()
   
   print("Record is inserted successfully")
   cursor.close()
   
 except sqlite3.Error as error:
  print("Error while connecting to the database",error)
    
 finally:   
    if sqliteConnection:
     sqliteConnection.close()
     print("The connection is closed")
  
#insertTable()

def createTable():
 try:
   sqliteConnection = sqlite3.connect('Film.db')
   cursor=sqliteConnection.cursor()
   print("Successfully connected to database")
   
   create_query="""create table film(id int primary key not null,fname text,tprice int)"""
   result=cursor.execute(create_query)
   sqliteConnection.commit()
   
   print("Table is created successfully")
   cursor.close()
   
 except sqlite3.Error as error:
  print("Error while connecting to the database",error)
    
 finally:   
    if sqliteConnection:
     sqliteConnection.close()
     print("The connection is closed")
     
#createTable()   
   
   
   
   
   

def createdB():
 try:
   
   sqliteConnection = sqlite3.connect('Film.db')
   cursor=sqliteConnection.cursor()
   print("Database is created succesfully")
   
   select_query="select sqlite_version();"
   cursor.execute(select_query)
   result1=cursor.fetchall()
   print(result1)
   
   select_query2="select date('now');"
   cursor.execute(select_query2)
   result2=cursor.fetchall()
   print(result2)
   
   cursor.close ()
        
 except sqlite3.Error as error:
      print("Error while connecting to the database",error)
    
 finally:   
    if sqliteConnection:
     sqliteConnection.close()
     print("The connection is closed")
     