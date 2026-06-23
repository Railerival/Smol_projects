import string

c = 0
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

x = input("Do you want to (e)ncrypt or (d)ecrypt?:\n")
key = int(input("Please enter the key (0 to 25) to use:\n"))
if key < 0 or key > 25:
    print("Error the key is too high")
    quit()
if x == "e":
    c = 1
    msg = input("Enter the message to encrypt:\n")
elif x == 'd':
    c = 2
    code = input("Enter the message to decrypt:\n")
else:
    print("that is not a valid command")

if c == 1:
    shifted = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    cipher_ascii_code = msg.maketrans(string.ascii_lowercase, shifted)
    print(msg.translate(cipher_ascii_code))
if c == 2:
    shifted = string.ascii_lowercase[(26 - (key + 1)):]+string.ascii_lowercase[:26 - (key + 1)]
    dec_msg_ascii_code = code.maketrans(shifted,string.ascii_lowercase)
    print(code.translate(dec_msg_ascii_code))




