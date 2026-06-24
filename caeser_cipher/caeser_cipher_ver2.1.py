import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

x = input("Do you want to (e)ncrypt or (d)ecrypt?:\n")
key = int(input("Please enter the key (0 to 25) to use:\n"))
if key < 0 or key > 25:
    print("Error the key is too high")
    quit()
if x == "e":
    msg = input("Enter the message to encrypt:\n")
    shifted = lower_case[key:] + lower_case[:key]
    cipher_ascii_code = msg.maketrans(lower_case, shifted)
    print(msg.translate(cipher_ascii_code))
elif x == 'd':
    code = input("Enter the message to decrypt:\n")
    shifted = lower_case[(26 - (key + 1)):]+lower_case[:26 - (key + 1)]
    dec_msg_ascii_code = code.maketrans(shifted,lower_case)
    print(code.translate(dec_msg_ascii_code))
else:
    print("that is not a valid command")

    




