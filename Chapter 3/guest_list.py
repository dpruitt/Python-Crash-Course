guests = ["Mark", "Jason", "Eric"]
print(f"{guests[0]}, please come to my dinner party.")
print(f"{guests[1]}, please come to my dinner party.")
print(f"{guests[2]}, please come to my dinner party.")

leaver = "Mark"
print(f"{leaver} cannot make the party.")
guests.remove(leaver)
guests.append("John")
print(f"{guests[0]}, please come to my dinner party.")
print(f"{guests[1]}, please come to my dinner party.")
print(f"{guests[2]}, please come to my dinner party.")

print("We have found a bigger table.")
guests.insert(0, "Luke")
guests.insert(2, "Greg")
guests.append("Mike")
print(f"{guests[0]}, please come to my dinner party.")
print(f"{guests[1]}, please come to my dinner party.")
print(f"{guests[2]}, please come to my dinner party.")
print(f"{guests[3]}, please come to my dinner party.")
print(f"{guests[4]}, please come to my dinner party.")
print(f"{guests[5]}, please come to my dinner party.")

print("We can only invite two people to dinner.")
uninvited = guests.pop()
print(f"Sorry {uninvited}, you are gone.")
uninvited = guests.pop()
print(f"Sorry {uninvited}, you are gone.")
uninvited = guests.pop()
print(f"Sorry {uninvited}, you are gone.")
uninvited = guests.pop()
print(f"Sorry {uninvited}, you are gone.")
print(f"{guests[0]}, please come to my dinner party.")
print(f"{guests[1]}, please come to my dinner party.")
print(f"I am inviting {len(guests)} guests to dinner.")
del guests
print(guests)


