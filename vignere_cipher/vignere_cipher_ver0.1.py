import string
import sys

full_key = []
alphabet_list = []
output = []
key_flag = 0

lower_case_string = string.ascii_lowercase
for letter in lower_case_string:
    alphabet_list.append(letter)
numbers_list = []
for number in range(0,26):
    numbers_list.append(number)


eord = input("""The Vigenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.
Do you want to (e)ncrypt or (d)ecrypt?:\n""").lower()

user_key = input("""Please specify the key to use.
It can be a word or any combination of letters:\n""").lower()

if eord != "e" or "d":
    print("u can only encrypt or decrypt")
    sys.exit()
else:
    if user_key.isalpha():
        if eord == "e":
            msg = input("enter the message to encrypt:\n")
            for letter in user_key:
                key = alphabet_list.index(letter)
                full_key.append(key)
            for letter in msg:
                if letter.isalpha():
                    power_of_letter = alphabet_list.index(letter) #power of letter is basically index of the letter in alphabet_list
                else:
                    power_of_letter = 0
                msg_letter_index = msg.index(letter)
            for key in full_key:
                output.append(alphabet_list[((power_of_letter+key)%26)])
            output = "".join(output)
            print(f"Encrypted message is:\n{output}")

        elif eord == "d":
            code = input("enter the code to decrypt:\n")
    else:
        print("key can only be a word or combination of letters")
        sys.exit()
