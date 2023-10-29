alphabet= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
'z': 26
}
sentence= input('Insert message to encrypt: ')
shift= int(input('What number do you want to shift?'))

encrypted_sentence = ''
for char in sentence:
    if char.isalpha():
        is_upper = char.isupper()
        char = char.lower()  
        shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        if is_upper:
            shifted_char = shifted_char.upper()
        encrypted_sentence += shifted_char
    else:
        encrypted_sentence += char

print('Encrypted message:', encrypted_sentence)    
