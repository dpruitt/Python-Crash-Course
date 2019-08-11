usernames = ["admin", "dylan", "user1", "user2", "user3"]

for user in usernames:
    if user == "admin":
        print("Hello administrator, would you like a status report?")
    else:
        print(f"Hello {user}.")
