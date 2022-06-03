import mysql.connector as connection
import datetime
class sql():
    def __init__(self, host, user, passwd,db_name):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db_name=db_name

    
    def db_connection(self):
        mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True,auth_plugin='mysql_native_password')
        try:
            
            query = "SHOW DATABASES"
            print('database connected')
            cursor = mydb.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as e:
            mydb.close()
            
    def database_creat(self):
        try:
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True)
            query = "create database IF NOT EXISTS " + self.db_name
            cursor = mydb.cursor() 
            cursor.execute(query)
            print('database created')
            mydb.close()
        except Exception as e:
            mydb.close()
            
    def creat_table(self):
        try:
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True)
            query = "create table {}.User(userId VARCHAR(20), userName VARCHAR(20), userdob VARCHAR(20), userEmail VARCHAR(30), userCreatedDate DATE,PRIMARY KEY (userId))".format(self.db_name)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('User table created')
            query = "create table {}.BankAccountTable(userId VARCHAR(20), bankAccountId VARCHAR(20), bankAccountNum VARCHAR(20), isActive VARCHAR(20), Amount VARCHAR(20),PRIMARY KEY (userId))".format(self.db_name)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('BankAccount table created')
            query = "create table {}.TransactionTable(userId VARCHAR(20), bankAccountId VARCHAR(20), withdrawAmount VARCHAR(20),transactionDate DATE,PRIMARY KEY (userId))".format(self.db_name)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('transaction table created')
            mydb.close()
        except Exception as e:
            mydb.close()
            print(str(e))
    
    def insert_User(self,insert):
        self.insert=insert
        
        try:
            print(self.insert)
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True)
            query = "INSERT INTO {}.User values{}".format(self.db_name,self.insert)
            x = datetime.datetime.now()
            query = query[:-1]
            query = query + "," + str(x.date()) + ")" 
            print(query)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('values added into the User table')
            mydb.commit()
        except Exception as e:
            mydb.close()
            print(str(e))
    def insert_BankAccountTable(self,insert):
        self.insert=insert
        
        try:
            print(self.insert)
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True)
            query = "INSERT INTO {}.BankAccountTable values{}".format(self.db_name,self.insert)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('values added into the BankAccountTable')
            mydb.commit()
        except Exception as e:
            mydb.close()
            print(str(e))
    def insert_TransactionTable(self,insert):
        self.insert=insert
        
        try:
            print(self.insert)
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, use_pure=True)
            query = "INSERT INTO {}.TransactionTable values{}".format(self.db_name,self.insert)
            x = datetime.datetime.now()
            query = query[:-1]
            query = query + ","+ str(x.date()) + ")"
            print(query)
            cursor = mydb.cursor()
            cursor.execute(query)
            print('values added into the TransactionTable ')
            mydb.commit()
        except Exception as e:
            mydb.close()
            print(str(e))
    
    
