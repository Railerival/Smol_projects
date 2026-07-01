import string

VOWELS = "aeiou"
function_check = 0
pig_latin_list = []

msg = input("Enter your message:\n> ").lower()
msg_list = msg.split(" ")
for word in msg_list:
    if word.isalpha():
        if word[0] in VOWELS:
            pig_latin_word = word + "yay"
        else:
            pig_latin_word = word[1:]+ word[0:1] + "ay"
        pig_latin_list.append(pig_latin_word)
    else:
        print("You have a character in the message that is not an alphabet")
        function_check = 1
        break
if function_check != 1:
    print(" ".join(pig_latin_list))



