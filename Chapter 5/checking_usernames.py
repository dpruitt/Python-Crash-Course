current_users = ["admin", "dylan", "user1", "user2", "user3"]
new_users = ["DYLAN", "new2", "new3", "new4", "new5"]
lower_current_users = []

for user in current_users:
    lower_current_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_current_users:
        print("Username is not available.")
    else:
        print("Username is available.")

