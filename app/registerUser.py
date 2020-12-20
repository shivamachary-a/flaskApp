import mysql.connector

from datetime import datetime

def registerUserSQL(firstName, lastName, email, passHash):
    if checkIfExists(firstName) == True:
        rds_host = 'entropy-db.cykvxxderykd.eu-central-1.rds.amazonaws.com'
        db_user = 'master'
        password = 'Shivam99'
        db_name = 'entropy'
        
        conn = mysql.connector.connect(user=db_user, password=password,
                                       host=rds_host,
                                       database=db_name)
                                       
        cur = conn.cursor()
        currentTime = str(datetime.today())
        
        cur.execute("""INSERT INTO users (firstName, lastName, email, passHash)
        VALUES (%s, %s, %s, %s)""", (firstName, lastName, email, passHash))
        conn.commit()
    
        response = "User Added"
        cur.close()
        
    
    else: 
        response = "User already exists"
        
    return response


def showUsers():
    rds_host = 'entropy-db.cykvxxderykd.eu-central-1.rds.amazonaws.com'
    db_user = 'master'
    password = 'Shivam99'
    db_name = 'entropy'
    
    conn = mysql.connector.connect(user=db_user, password=password,
                                   host=rds_host,
                                   database=db_name)
                                   
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    cur.close()
    return str(result)
    
   
   
def checkIfExists(name):
    rds_host = 'entropy-db.cykvxxderykd.eu-central-1.rds.amazonaws.com'
    db_user = 'master'
    password = 'Shivam99'
    db_name = 'entropy'
    
    conn = mysql.connector.connect(user=db_user, password=password,
                                   host=rds_host,
                                   database=db_name)
                                   
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT * FROM users 
    WHERE firstName = %s)""", (name,))
    result = cur.fetchall()
    conn.commit()
    cur.close()
    print(result)
    if int(result[0][0]) > 0:
        return False
    else: 
        return True
 
def commit():
    rds_host = 'entropy-db.cykvxxderykd.eu-central-1.rds.amazonaws.com'
    db_user = 'master'
    password = 'Shivam99'
    db_name = 'entropy'
    
    conn = mysql.connector.connect(user=db_user, password=password,
                                   host=rds_host,
                                   database=db_name)
                                   
    cur = conn.cursor()
    cur.execute("REPAIR TABLE users")
    
showUsers()
    


