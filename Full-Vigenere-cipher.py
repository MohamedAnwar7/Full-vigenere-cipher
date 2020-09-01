# Generate key until it's length equal to our string length
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


# encrypt our string
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i])+ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


# Decrypt cipher-text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


string = input('Enter your plain-text:\t')
keyword = input('Enter your key:\t')
key = generateKey(string, keyword)
cipher_text = cipherText(string, key)
print('Ciphertext :', cipher_text)
print('original/Decrypted text : ', originalText(cipher_text, key))
