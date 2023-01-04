from dbconfig import *
import time
import schedule




resData=0

#----postgresql--connection-------------------------------------------

print(mydb)
# mycurs=mydb.cursor()  
# mycurs.execute("Select * FROM pcount")
#     # global myresult
# myresult = mycurs.fetchone()
# print(myresult)
#------Function--Start--------------------------------------------------

def secdule_count():
    mycurs=mydb.cursor()  
    mycurs.execute("select count from pcount ORDER BY id DESC LIMIT 1")
    # global myresult
    myresult = mycurs.fetchone()
    # print(myresult)
    
#--------------------------------------------------------------------    
    # global resData
    for i in myresult:
        resData=i
    # print(resData)
    return resData
#--------------------------------
def posdata_insert():
    poscursor=conn.cursor()
    posql = poscursor.execute("INSERT INTO count(rcount) VALUES (%s)"%(resData))
    conn.commit()

#-------------------------------
# print(resData)
# schedule.every(2).seconds.do(secdule_count)
# schedule.every(3).seconds.do(posdata_insert)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

print(secdule_count())