import os

lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c = 0
output = ""
output_list = []

def encrypter(list,key,i):
    """finds the encrypted letter and appends it to the output list"""
    indec = list.index(i)
    indec = indec + key
    indec = indec % 26
    output_list.append(uppercase_letters[indec])
    return output_list

def decrypter(list,key,i):
    """finds the decrypted letter and appends it to the output list"""
    indec = list.index(i)
    indec = indec - key

    output_list.append(uppercase_letters[indec])
    return output_list

def main():
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
        for i in msg:
            if i in lowercase_letters:
                output_list = encrypter(lowercase_letters,key,i)
                output = "".join(output_list)
            elif i in uppercase_letters:
                output_list = encrypter(uppercase_letters,key,i)
                output = "".join(output_list)
            else:
                output_list.append(i)
                output = output.join(output_list)

    elif c == 2:
        for i in code:
            if i in lowercase_letters:
                output_list = decrypter(lowercase_letters,key,i)
                output = "".join(output_list)
            elif i in uppercase_letters:
                output_list = decrypter(uppercase_letters,key,i)
                output = "".join(output_list)
            else:
                output_list.append(i)
                output = output.join(output_list)

    print(output)

if __name__ == "__main__":
    main()