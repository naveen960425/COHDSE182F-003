plaintext = input('Enter message: ')
alphabet = "abcdefghijklmnopqrstuvqxyz"
key = 1
cipher = ''

for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]

print('Your encrypted message is: '+ cipher)        
