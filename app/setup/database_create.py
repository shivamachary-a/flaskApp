import mysql.connector

def populate():
    
    rds_host = 'entropy-db.cykvxxderykd.eu-central-1.rds.amazonaws.com'
    db_user = 'master'
    password = 'Shivam99'
    db_name = 'entropy'
    
    conn = mysql.connector.connect(user=db_user, password=password,
                                   host=rds_host,
                                   database=db_name)
                                   
    cur = conn.cursor()
    
    cur.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    cur.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(255), lastName VARCHAR(255), email VARCHAR(255), passHash VARCHAR(255))")
    print("Database Created.")
populate()
    