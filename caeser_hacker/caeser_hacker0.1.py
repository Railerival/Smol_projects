import string

upper_case = string.ascii_uppercase

code = input("Enter the encrypted Caesar cipher message to hack:\n> ").upper()

for i in range(1,26):
    shifted = upper_case[(-i):]+upper_case[:(-i)]
    cipher = str.maketrans(upper_case,shifted)
    print(f"Key #{i}: {code.translate(cipher)}")

