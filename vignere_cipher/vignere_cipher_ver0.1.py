import string
import sys

alphabet_list = []
conversion_list = []
output_list = []
lower_case_string = string.ascii_lowercase
character_count = 0

def get_number(letter):
    if not letter.isalpha():
        return letter
    index = alphabet_list.index(letter)
    return index
    
def get_alphabet(number):
    return alphabet_list[number]

for letter in lower_case_string:
    alphabet_list.append(letter)

function = input("""The Vigenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.
Do you want to (e)ncrypt or (d)ecrypt?:""").lower()

if not(function == "e" or function == "d"):
    print("Only encryption and decryption possible")
    sys.exit()

key = input("""Please specify the key to use.
It can be a word or any combination of letters:""").lower()

if not key.isalpha():
    print("Only alphabet keys are allowed")
    sys.exit()

key_length = len(key)

if function == "e":
    message = input("Enter the message to encrypt:").lower()

    for letter in message:
        msg_number = get_number(letter)
        conversion_list.append(msg_number)

    for msg_character_index, msg_character in enumerate(conversion_list):
        if isinstance(msg_character, int):
            key_index = ((msg_character_index - character_count) % key_length)
            key_number = get_number(key[key_index])
            encrypted_number = ((key_number + msg_character) % 26)
            output_list.append(get_alphabet(encrypted_number))
        else:
            character_count += 1
            output_list.append(msg_character)
else:
    cipher_text = input("Enter the message to encrypt:").lower()

    for letter in cipher_text:
        cipher_number = get_number(letter)
        conversion_list.append(cipher_number)
    for cipher_character_index, cipher_character in enumerate(conversion_list):
        if isinstance(cipher_character, int):
            key_index = ((cipher_character_index - character_count) % key_length)
            key_number = get_number(key[key_index])
            encrypted_number = ((cipher_character - key_number) % 26)
            output_list.append(get_alphabet(encrypted_number))
        else:
            character_count += 1
            output_list.append(cipher_character)



print("".join(output_list).upper())
        