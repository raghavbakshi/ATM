from db_obs import sql
import datetime


# Basic setup
o1=sql('localhost','root','password','ineuron')
o1.db_connection()
o1.database_creat()
o1.creat_table()

# insert records in User table
o1.insert_User((1,"raghav","19-07-1999","ra@gmail.com"))
o1.insert_User((2,"bakshi","20-07-1999","ragh@gmail.com"))
o1.insert_User((3,"vansh","21-07-1999","va@gmail.com"))
o1.insert_User((4,"suhail","22-07-1999","radf@gmail.com"))

# insert records in Bank Account table
o1.insert_BankAccountTable((1,"JKB",1234,True,5000))
o1.insert_BankAccountTable((2,"PNB",14,True,5500))
o1.insert_BankAccountTable((3,"PNB",12,False,65000))
o1.insert_BankAccountTable((4,"JKB",124,True,3000))

# Check the current account balance
def get_acc_bal(ID):
    mydb = connection.connect(host="localhost", user="root", passwd="password", use_pure=True)
    cursor = mydb.cursor()
    query='SELECT Amount FROM ineuron.BankAccountTable where userId = {}'.format(ID)
    cursor.execute(query)

    (i for i in cursor)
    return(i[0])

get_acc_bal(1)


# Withraw the amount
def withraw(ID,bank_acc_id,input_amount):
    mydb = connection.connect(host="localhost", user="root", passwd="password", use_pure=True)
    cursor = mydb.cursor()
    query='SELECT Amount FROM ineuron.BankAccountTable where userId = {}'.format(ID)
    cursor.execute(query)
    for i in cursor:
        amount_present = int(i[0])
    if amount_present <= 5000:
        return("Minimum balance of 5000 should be maintained")
    elif input_amount > amount_present:
        return("Insufficient Balance")
    else:
        updated_amount = amount_present - input_amount
        mydb = connection.connect(host="localhost", user="root", passwd="password", use_pure=True)
        cursor = mydb.cursor()
        query='UPDATE ineuron.BankAccountTable SET Amount = {} where userId = {}'.format(updated_amount,ID)
        cursor.execute(query)
        mydb.commit()
        o1.insert_TransactionTable((ID,bank_acc_id,input_amount))
    return "amount left in your account is: ",updated_amount

withraw(2,14,500)

# Account Statement

def statement(start,end,id):
    mydb = connection.connect(host="localhost", user="root", passwd="password", use_pure=True)
    cursor = mydb.cursor()
    query='SELECT * FROM ineuron.TransactionTable where transactionDate <= {} and transactionDate >= {} and userId = {} '.format(end,start,ID)
    cursor.execute(query)
    for i in cursor:
        print(i)    




"""
   END
    """