usernames = []
passwords = []

def registerAccount(username, password):
    usernames.append(username)
    passwords.append(password)

    return True

def loginToAccount(username, password):
    for users in range(len(usernames)):
        if usernames[users] == username:
            if passwords[users] == password:
                return True; break
            else: return False; break
        else: return False; break

def mainFunction():
    createOrLogin = input("Would you like to login or create an account? (C/L) ")
    if createOrLogin == 'C' or createOrLogin == 'c':
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        success = registerAccount(username, password)

        if success == True:
            print("Successfully created an account")
            mainFunction()
        else: mainFunction()
    elif createOrLogin == 'L' or createOrLogin == 'l':
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        success = loginToAccount(username, password)
        if success == True:
            print("Successfully logged in")
        else:
            print("Incorrect username or password")
            mainFunction()

if __name__ == "__main__":
    mainFunction()