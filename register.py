from common import *
users = {}

def signUp(userName, password):
    if userName in users:
        print("User already exists")
    else:
        users[userName] = password
        print("User created successfully")
        quiz()
    
def logIn(userName , Password):
    if userName in users:
        if users[userName] == Password:
            print("Login successful")
            quiz()
        else:
            print("Incorrect password")
    else:
        print("User does not exist")
        exit()
