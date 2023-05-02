import sqlite3
import base64

# Connect to the database
conn = sqlite3.connect('users.db')

cursor = conn.cursor()

# See if the username matches a known user

def loginCheck(userName, password):
    
    statement = f"SELECT username from users WHERE userName='{userName}';"
    cursor.execute(statement)
    if not cursor.fetchone():
        print("User not found")
        
    else:
        print("User found")
        
        # See if the password matches the username

        statement = f"SELECT username from users WHERE userName='{userName}' AND password='{password}';"
        cursor.execute(statement)
        if not cursor.fetchone():
            print("User not found")
            check = False
        else:
            print("User found")
            check = True
    
    
    
    return check


# Register the user

def registerUser(username, password):
    
    statement = f"INSERT INTO users (username,password) VALUES ('{username}','{password}')"
    cursor.execute(statement)
    conn.commit()

