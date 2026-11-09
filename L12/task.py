import mysql.connector
import getpass




user_password = getpass.getpass("enter your password: ")
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

enter your password: strongpassword
[(1, 'ftm70', '001fa', 'active')
 
"""






