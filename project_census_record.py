import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
mycursor = mydb.cursor()

print("LET'S START FILLING DATA OF 16th CENSUS (2020)")
print("1.Population Data")
print("2.Distribution Of Population")
print("3.DETAILS REGARDING EDUCATION")
print("4.DETAILS of infrastructure development")
print("5.DETAILS REGARDING MIGRATED POPULATION")
print('6.DETAILS OF RESOURCES')
print('7.DETAILS OF PROGRESS REPORT')


#1.function of population data
def population_data():
    print("Population Data")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_ppln=int(input("enter population 2020:"))
        st_pplo=int(input("enter population 2011:"))
        st_increase=((st_ppln-st_pplo)/st_ppln)*100
        st_child=int(input("enter percentage of people in age (1-14):"))
        st_adult=int(input("enter percentage of people in age (14-50):"))
        st_old=input("enter percentage of people in age (above50):")
        st_area=int(input("enter total geographical area in (m sq.):"))
        st_density=st_ppln/st_area
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO population VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_ppln,st_pplo,st_increase,st_child,st_adult,st_old,st_area, st_density)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n")
    

#2.function of population_distribution
def population_distribution():
    print(" Distribution of Population ") 
    ch="y"
    count=0
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_pplR=int(input("enter rural population 2020:"))
        st_pplU=int(input("enter urban population 2020:"))
        st_areaR=int(input("enter total rural area in (m sq.) :"))
        st_areaU=int(input("enter total urban area in (m sq.) :"))
        st_densityR=st_pplR/st_areaR
        st_densityU=st_pplU/st_areaU
        st_female=int(input("enter female population:"))
        st_male=int(input("enter male population:"))
        st_sexratio=int((st_female/st_male)*100)
        st_infant=int(input("enter infant mortility rate:"))
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO distribution_of_population VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_pplR,st_pplU,st_areaR,st_areaU,st_densityR,st_densityU,st_female,st_male,st_sexratio,st_infant)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n")
        
        
#3.function on infrastructure of states
def infrastructure():
    print("DETAILS of infrastructure development")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_monuments=int(input("enter number of monuments:"))
        st_railwaystations=int(input("enter number of railway stations:"))
        st_internationalairports=int(input("enter number of international airports :"))
        st_domesticairports=int(input("enter number of domestic airports:"))
        st_shipports=input("enter number of ship ports:")
        st_mnc=int(input("enter number of MNC companies:"))
        st_hotels=int(input("enter number of 5 star hotels :"))
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO infrastructure VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_monuments,st_railwaystations,st_internationalairports,st_domesticairports,st_shipports,st_mnc,st_hotels)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")
          
        
#4.function of showing education status
def education():
    print("DETAILS REGARDING EDUCATION")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_literacy=int(input("enter literacy rate in %:"))
        st_ltcfemale=int(input("enter literacy rate among female in %:"))
        st_ltcmale=int(input("enter literacy rate among male in %:"))
        st_university=int(input("enter number of national universities or institutions:"))
        st_colleges=int(input("enter number of state colleges :"))
        st_govtschool=int(input("enter number of government school:"))
        st_pvtschool=input("enter number of private schools:")
        st_stdfemale=int(input("enter num0ber of female getting higher education:"))
        st_govtjob=int(input("enter average number of person in govt jobs per family :"))
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO educational_development VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_literacy,st_ltcfemale,st_ltcmale,st_university,st_colleges, st_govtschool,st_pvtschool, st_stdfemale,st_govtjob)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")

        
#5.function to give data of migration
def migration():
    print("DETAILS REGARDING MIGRATED POPULATION")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_migedu=int(input("enter population which migrated for education :"))
        st_migjob=int(input("enter population migrated for job:"))
        st_migother=int(input("enter population migrated for any other purpose:"))
        M=(st_migedu+st_migjob+st_migother)
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO migration_data VALUES (%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_migedu,st_migjob,st_migother,M)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")        


#6.function of resources avalibility
def resources():
    print("DETAILS OF RESOURCES")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_GWlevel=int(input("enter ground water level:"))
        st_crop=input("enter major crop growing :")
        st_forest=int(input("enter total forest area in (m sq.):"))
        st_coast=int(input("enter total area covered with water in (m sq.):"))
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO DETAILS_OF_RESOURCES VALUES (%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_GWlevel,st_forest,st_coast,st_crop)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")


#7.function of progress report
def progress():
    print("DETAILS OF PROGRESS REPORT")
    ch="y"
    while (ch=='y'):
        st_num=int(input("enter sr no:"))
        st_name=input("enter state name:")
        st_dist=int(input("enter number of districts :"))
        st_enublocks=int(input("enter total enumeration blocks:"))
        st_inprog=int(input("enter total districts in work progress:"))
        st_enublupload=int(input("enter enumeration on blocks uploaded:"))
        st_dataup=int(input("enter status of data uploaded:"))
        st_balance=st_enublocks-st_enublupload
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="panther",database="sixteenth_census")
        mycursor = mydb.cursor()
        stru=("INSERT INTO progress_report VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(st_num,st_name,st_dist,st_enublocks,st_inprog,st_enublupload,st_dataup,st_balance)
        mycursor.execute(stru,data)
        mydb.commit()
        print("insertion completed")
        print("do you want add more data ?")
        ch=input("enter your choice y/n:")

for i in range(7):
    choice=int(input('enter your choice:'))
    if choice==1:
        print(population_data())
    elif choice==2:
        print(population_distribution())
    elif choice==3:
        print(education())
    elif choice==4:
        print(infrastructure())
    elif choice==5:
        print(migration())
    elif choice==6:
        print(resources())
    elif choice==7:
        print(progress())
    else:
        print("wrong selection")
print("THANK YOU")


    



  
