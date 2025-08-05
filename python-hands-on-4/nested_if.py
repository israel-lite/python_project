username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        security_code = input("Enter security code: ")
        if security_code == "abc":
            access_level = input("Enter access level (high/low): ")
            if access_level == "high":
                confirmation = input("Type YES to confirm access: ")
                if confirmation == "YES":
                    print("Access Granted. Welcome, Admin!")
                else:
                    print("Access Denied: Confirmation failed.")
            else:
                print("Access Denied: Low-level access is not allowed.")
        else:
            print("Access Denied: Incorrect security code.")
    else:
        print("Access Denied: Wrong password.")
else:
    print("Access Denied: Unknown user.")

