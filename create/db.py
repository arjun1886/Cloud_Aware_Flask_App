import mysql.connector

mydb2 = mysql.connector.connect(host = "172.17.0.2", port = "3306", user = 'root', password = '', auth_plugin = 'mysql_native_password')
mycursor2 = mydb2.cursor()
mycursor2.execute("DROP DATABASE IF EXISTS selfieless")
mycursor2.execute("CREATE DATABASE selfieless")
mydb1 = mysql.connector.connect(host = "172.17.0.2", port = "3306", user = 'root', password = '', auth_plugin = 'mysql_native_password', database = 'selfieless')

mycursor1 = mydb1.cursor()
mycursor1.execute("""DROP TABLE IF EXISTS acts""")
mycursor1.execute("""DROP TABLE IF EXISTS users""")
mycursor1.execute("""DROP TABLE IF EXISTS categories""")
mycursor1.execute("""CREATE TABLE users (username VARCHAR(100) PRIMARY KEY, passwd VARCHAR(50))""")
mycursor1.execute("""CREATE TABLE categories (catname VARCHAR(50) PRIMARY KEY)""")
mycursor1.execute("""CREATE TABLE acts (actid integer PRIMARY KEY,uname VARCHAR(100) ,times VARCHAR(100),votes integer, caption VARCHAR(300),catname VARCHAR(50), imgb64 VARCHAR(100), FOREIGN KEY(catname) REFERENCES categories(catname))""")