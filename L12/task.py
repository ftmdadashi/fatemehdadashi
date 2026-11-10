"""
 kar ba paygahe dade MySQL dar python
 
dar in tamrin bayad yek paygahe dade dar MySQL ijad karde , sepas az tarighe python

ba aan ertebat bargharar konid. sepas  be paygahe dadeh users ba estefade az karbare 

user_manager motasel shavid. jadvali be name user_information ijad konid, yek record

jadid dar aan besazid, record sabt shodeh ra ba estefade az python az database 

daryaft konid , etelaate recorde daryaft shode ra dar khoroji namaysh dahid.



1. ijade karbare jadid:
    
   CREATE USER 'user_manager'@'localhost' IDENTIFIED BY 'strongpassword';

    
2. ijade paygahe dadeh be name : users :
    
    CREATE DATABASE IF NOT EXISTS users;


3. etaye dastresi kamel be karbar baraye paygahe dadeh ijad shode:
    
    GRANT ALL PRIVILEGES ON users.* TO 'user_manager'@'localhost';

"""
    
    

import mysql.connector
from dotenv import load_dotenv 
import os



load_dotenv()
user_password = os.getenv("user_password")
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='user_manager',
    password=user_password,
    database='users'
)

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user_information(
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                status VARCHAR(20) DEFAULT 'active')''')

connection.commit()

#-----------------------------------------------------------------------

cursor.execute('''INSERT INTO user_information (username,password,status)
                VALUES ("ftm70","001fa","active")''')

connection.commit()

#-----------------------------------------------------------------------

cursor.execute('SELECT * FROM user_information')
result = cursor.fetchall()

#------------------------------------------------------------------------

print(result)
cursor.close()


"""


[(1, 'ftm70', '001fa', 'active')
 
"""






