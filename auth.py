from werkzeug.security import generate_password_hash, check_password_hash


# Demo analyst account
users = {

    "analyst": generate_password_hash("SOC@123")

}



def login(username, password):

    if username in users:

        if check_password_hash(users[username], password):

            return True


    return False



if __name__ == "__main__":


    username = input("Username: ")

    password = input("Password: ")


    if login(username, password):

        print("✅ Login successful")

    else:

        print("❌ Invalid credentials")