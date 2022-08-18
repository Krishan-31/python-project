import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
mycursor = mydb.cursor()
def trainsdetails():
    print("TRAINS DETAILS")
    ch="y"
    while (ch=='y'):
        t_num=int(input("enter train no:"))
        t_name=input("enter train name:")
        t_ac1=int(input("enter no. of seats in ac1:"))
        t_slp=int(input("enter no. of seats in slp:"))
        t_dis=int(input("enter total distance in km:"))
        t_start=input("enter train's initial station:")
        t_end=input("enter train's final station:")
        t_route=print('from',t_start,'to',t_end)
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
        mycursor = mydb.cursor()
        stru=("INSERT INTO trainsdetails(t_num,t_name,t_ac1,t_slp,t_dis,t_route)  VALUES (%s,%s,%s,%s,%s,%s)")
        data=(t_num,t_name,t_ac1,t_slp,t_dis,t_route)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n")                 



#function of intermiadiate stations
def intermiadiatestations():
    print("DETAILS of intermiadiate stations")
    ch="y"
    while (ch=='y'):
        t_num=int(input("enter train no:"))
        t_halts=input("enter total no. of halts:")
        t_nameofstations=[]
        next="y"
        while next=="y":
            station=input("enter name of station:")
            t_nameofstations.append(station)
            next=input("enter your choice y/n:")    
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
        mycursor = mydb.cursor()
        stru=("INSERT INTO intermiadiatestations  VALUES (%s,%s,%s)")
        data=(t_num,t_halts,t_nameofstations)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")
       
        
        

def Reservation_of_passengers():
    print("PASSENGERS DETAILS")
    ch="y"
    while (ch=='y'):
        p_t_num=int(input("enter train no:"))
        a=print(p_t_num)
        P_name=input("enter passenger name:")
        P_sex=input("enter SEX of PASSENGER :")
        p_age=int(input("enter age of passenger:"))
        PWD=(input("is passenger is handicapped(y/n):"))
        pick_up=input("enter station from which passenger sit:")
        dest=input("enter destination point:")
        route=print("from",pick_up,"to",dest)
        fare=float(input("enter fare for trip:"))
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT t_nameofstations  FROM intermiadiatestations WHERE t_num=45526")
        results=mycursor.fetchall()
        my_list=list(results)
        for i in my_list:
            print(i)
        mydb.commit()
        x=0
        y=0
        for i in results:
            if i != dest:
                x=x+1
            else:
                break
        for i in results:
            if i != pick_up:
                y=y+1
            else:
                break
        num_of_halts=x-y-1
        print(num_of_halts)
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
        mycursor = mydb.cursor()
        stru=("INSERT INTO reservation VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(p_t_num,P_name,P_sex,p_age,PWD,pick_up,dest,route,fare,num_of_halts)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")
        




def cancellationofticket(name):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
    mycursor = mydb.cursor()
    mycursor.execute("delete from reservation where name=")
    mydb.commit()
    
def deletion_trainrrecords():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="railway")
    mycursor = mydb.cursor()
    mycursor.execute("delete from trainsdetails where t_num=265425")
    mydb.commit()
deletion_trainrrecords()    
print("deletion completed")        
        
        
    



  
