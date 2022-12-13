import mysql.connector as msql
#---------- Function for creating connection object ----------
def connection():
try:
con=msql.connect(host='localhost',user='root',passwd='mysql',database='PROJECTCS')
if con.is_connected()==True:
print("\t\t\t\t!!!!! Welcome to Computer Lab Stock Management Syatem !!!!! ")
print("\t\t\t\tYou are successfully connected to database PROJECTCS.")
x=input("\t\t\t\t Press any key to continue......")
return con
except msql.Error:
print("OOPs ! Couldn't connected with database ")
con=connection()
cursor=con.cursor()
#---------- Function for adding a new record ----------
def insert_r():
code=input('Enter item code ::::-> ')
name=input('Enter item name ::::-> ')
company=input('Enter company name ::::: -- >> ')
no=int(input('Enter bill no : ::::: -- >> '))
bill_date=input('Enter bill date ::::: -- >> ')
qty=int(input('Enter quantity ::::: -- >> '))
rate=int(input('Enter rate per item ::::: -- >> '))
tcost=int(input('Enter total cost ::::: -- >> '))
itype=input('Enter c for consumable and nc for non-consumable ::::: -- >> ')
doc=input('Enter date of condemnation ::::: -- >> ')

sql="insert into stock(ICODE,INAME,COMPANY_NAME,BILL_NO,\
BILL_DATE,QTY,RATE,TOTAL_COST,ITEM_TYPE,DATE_OF_CONDEMN)\
values('{}','{}','{}',{},'{}',{},{},{},'{}','{}')".format(code,name,\

company,no,bill_date,qty,rate,tcost,itype,doc)
cursor.execute(sql)
con.commit()
#---------- Function to display the records ----------
def display():
print("\n")
print("\t\t\t THE DETAILS OF STOCK IN COMPUTER LAB IS :::")
print("\t\t\t ===========================================\n")
cursor.execute('SELECT * FROM STOCK')
data=cursor.fetchall()
if data==[]:
print("OOPS ! No Record Found\n")
else:
print("ICODE\t\tINAME\t\tCOMPANY\tBILL NO\tBILL DATE\tQTY\tRATE\tT
COST\tTYPE\tDATE_CONDEMN")
for i in data:
for j in range(0,10):
print(i[j],end='\t')
print()
#---------- Function to search the records ----------
def search():
stype=input("Press s/S for String type and i/I for Integer column type search ::::: -- >>")
if stype in 'sS':
col_name=input('Enter column name for which u want to do search ::::: -- >> ')
value=input('Enter the value to be searched ::::: -- >>')
cursor.execute("SELECT * FROM STOCK WHERE %s='%s'"%(col_name,value))
elif stype in 'iI':
col_name=input('Enter column name for which u want to do search ::::: -- >>')
value=int(input('Enter the value to be searched ::::: -- >>'))
cursor.execute("SELECT * FROM STOCK WHERE %s=%s"%(col_name,value))
data=cursor.fetchall()
if data==[]:
print("OOPS ! No Record Found\n")
else:
print("\nRecord found and details are .......\n")
for i in data:

for j in range(0,10):
print(i[j],end='\t')
print()
#---------- Function to update a record ----------
def update():
code=input('Enter the item code ::::::-->> ')
col_change=input('Enter column name for which u want to change the value ::::: -- >> ')
value_new=input('Enter the new value ::::: -- >>')

cursor.execute("UPDATE STOCK SET {}='{}' WHERE
icode='{}'".format(col_change,value_new,code))
cursor.execute("SELECT * FROM STOCK WHERE icode='{}'".format(code))
data=cursor.fetchall()
if data==[]:
print("OOPS ! No Record Found\n")
else:
print("ICODE","INAME","COMPANY NAME","BILL NO","BILL
DATE","QTY","RATE","TOTAL COST","ITEM TYPE","DATE OF CONDEMN")
for i in data:
for j in range(0,10):
print(i[j],end=" ")
print()
con.commit()
#---------- Function to delete a record ----------
def delete():
code=input('Enter item code ::::: -- >> \n\n ')
cursor.execute("SELECT * FROM STOCK WHERE ICODE='{}'".format(code))
data=cursor.fetchall()
if data==[]:
print("OOPS ! No Record Found\n")
else:
cmd="DELETE FROM STOCK WHERE ICODE='{}'".format(code)
cursor.execute(cmd)
con.commit()

print("Record deleted successfully\n")
print("The details after deletion are:::::")
print("========================\n")
cursor.execute('SELECT * FROM STOCK')
data=cursor.fetchall()
if data==[]:
print("OOPS ! No Record Found\n")
else:
print("ICODE\t\tINAME\t\tCOMPANY\tBILL NO\tBILL DATE\tQTY\tRATE\tT
COST\tTYPE\tDATE_CONDEMN")
for i in data:
for j in range(0,10):
print(i[j],end='\t')
print()
con.commit()
#---------- Function to display the structure of the table ----------
def info():
print("\n====================================THE STRUCTURE OF THE
TABLE STOCK IS ======================================\n")
print("Field \t\t\t Type \t\t\t Null \t\t\t Key \t\t\t Default ")
print("ICODE \t\t\t varchar(10) \t\t NO \t\t\t PRI \t\t\t NULL ")
print("INAME \t\t\t varchar(15) \t\t NO \t\t\t\t\t\t NULL ")
print("COMPANY_NAME \t\t varchar(15) \t\t YES \t\t\t\t\t\t NULL ")
print("BILL_NO \t\t\t int(11) \t\t\t YES \t\t\t\t\t\t NULL ")
print("BILL_DATE \t\t date \t\t\t YES \t\t\t\t\t\t NULL ")
print("QTY \t\t\t int(11) \t\t\t YES \t\t\t\t\t\t NULL ")
print("RATE \t\t\t decimal(10,2) \t\t YES \t\t\t\t\t\t NULL ")
print("TOTAL_COST \t\t decimal(12,2) \t\t YES \t\t\t\t\t\t NULL ")
print("ITEM_TYPE \t\t varchar(7) \t\t YES \t\t\t\t\t\t CON ")
print("DATE_OF_CONDEMN \t date \t\t\t YES \t\t\t\t\t\t NULL ")

#---------- Function to display the abbreviations of items ----------
def icodes():
print(" \n\nTHE ITEM NAMES AND THEIR ABBREVIATIONS FOR CREATING
ICODE ")
print("============================================================"
)
print("ITEM NAME \t\t\tITEM CODE")
print("KEYBOARD\t\t\tKB")
print("MOUSE\t\t\t\tMO")
print("MONITOR\t\t\tMT")
print("RAM\t\t\t\tRM")
print("HUB\t\t\t\tHB")
print("HARD DISC\t\t\tHD")
print("PROJECTOR\t\t\tPJ")
print("For creating the Item code use ====>>> abbreviation+dd+mm+yy (date of
bill)")
#---------- Main Function----------
def main():
ch='y'
while ch in 'Yy':
print('\n\t\t\t\t COMPUTER LAB STOCK REGISTER MANAGEMENT SYSTEM')
print('\t\t\t\t ==================================================\n')
info()
icodes()
print('\n\t::::: MENU :::::\n')
print("\tPress 1 to ADD a record ")
print("\tPress 2 to DISPLAY all the records ")
print("\tPress 3 to SEARCH for a record ")
print('\tPress 4 to UPDATE a record ')
print("\tPress 5 to DELETE a record ")
print("\tPress 6 to show the STRUCTURE of the table ")
opt=int(input("\tEnter your choice ::::: -- >> "))

if opt==1:
insert_r()
elif opt==2:
display()
elif opt==3:
search()
elif opt==4:
update()
elif opt==5:
delete()
elif opt==6:
info()
else:
print('OOPS ! WRONG CHOICE')
ch=input('\n Do you want to continue? (Y/N) ::::: -- >>')

#---------- Calling of main function ----------
main()
