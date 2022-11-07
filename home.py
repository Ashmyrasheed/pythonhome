import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'homeautomationdb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")

    print("1 add ")

    print("2 view all ")  

    print("3 search ")

    print("4 update ")    

    print("5 delete ")

    print("6 exit")

   

    choice = int(input('enter an option:'))

    if(choice==1):

        print(' insert selected')
        
        
    

    elif(choice==2):

        print('view ')

    elif(choice==3):

        print('search ')

    elif(choice==4):

        print('update ')

    elif(choice==5):

        print('delete ')

    elif(choice==6):

        break