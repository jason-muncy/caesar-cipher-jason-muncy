shift = int(input('Please enter a number from 1-26 to shift: '))
encrypt = str(input('Please enter text to encrypt: '))
encrypted_message = ""

# creating list for a-z
alphabet = []

for i in range(ord('a'), ord('z')+1):
    alphabet.append(chr(i))

for i in encrypt:
    if i in alphabet:
        f = alphabet.index(i) + shift
        if f > 26:
            f = f % 26
        encrypted_message += alphabet[f]

print(encrypted_message)  
