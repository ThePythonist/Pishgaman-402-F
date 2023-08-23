def register():
    username = input("Choose a username : ")
    password = input("Choose a password : ")

    open("users.txt", "a").write(username + "\n")
    open("passwords.txt", "a").write(password + "\n")

    print(f"Registered user {username}")


def login():
    users = open("users.txt").read().split("\n")
    passwords = open("passwords.txt").read().split("\n")
    accounts = dict(zip(users, passwords))

    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if username in accounts:
        if accounts[username] == password:
            print("Logged in")
        else:
            print("Password is incorrect")
    else:
        print("Account doesn't exist")


def main():
    choice = input("""
Choose an action :
1 : Register
2 : Login to account
: 
""")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Choose 1 or 2. Try again")
        main()


main()
