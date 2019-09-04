# key must be between 0 and 26
# only worry about lowercase

string = input("Enter a string to encrypt:\n")
key = input("Enter a key for the cipher\n")

output = ''
for aChar in string:
    someValue = ord(aChar) - 97 + int(key)
    output = output + chr(someValue % 26 + 97)

print(output)
