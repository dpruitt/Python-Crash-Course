usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello administrator, would you like a status report?")
        else:
            print(f"Hello {user}.")
else:
    print("We need to find some users.")
