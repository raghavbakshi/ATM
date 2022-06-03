from db_obs import sql

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

