# User database to store registered users
user_db = {}

#Test for username
def test_username(name):
    if name in user_db:
        print("Username Already used. Retry new username.")
        register()


# Function to register a new user
def register():
    username = input("Enter a username: ")
    test_username(username)
    password = input("Enter a password: ")
    user_db[username] = password
    print("Registration successful!")

# Function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_db and user_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed. Please check your username and password.")
        return False

# Function to access the secured page
def secured_page():
    print("Welcome to the secured page!")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Access Secured Page")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        if login():
            secured_page()
    elif choice == "3":
        if login():
            secured_page()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
