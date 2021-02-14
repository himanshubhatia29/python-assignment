import mysql.connector
cnx = mysql.connector.connect(user='root',password='himanshu123',host='127.0.0.1',database='router_master')
cursor = cnx.cursor()
cursor  =  cnx.cursor ()
#create the salesman table 
entry_nos=input("Enter the no of records to be inserted:")
no=int(entry_nos)
print(no)
for i in range(0,no):
    s_id = input('sap ID:')
    s_name = input('Host Name:')
    s_city = input('Loop Back:')
    s_commision = input('Mac Address:')
    cursor.execute("""
    INSERT INTO router_roaster(sapId, hostName, loopBack, macAddress)
    VALUES (%s,%s,%s,%s)
    """, (s_id, s_name, s_city, s_commision))
    cnx.commit ()
    print ( 'Data entered successfully.' )
    # cnx.close ()
if (cnx):
  cnx.close()
  print("\nThe Mysql connection is closed.")


