import string


def shift(key):
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet[:key]:
        alphabet.remove(letter)
        alphabet.append(letter)
    return alphabet


def encrypt(word, key):
    alphabet = list(string.ascii_lowercase)
    shifted = shift(key)

    encrypted = ""
    for letter in word:
        for position in range(len(shifted)):
            if alphabet[position] == letter:
                encrypted += shifted[position]

    return encrypted


def decrypt(word, key):
    shifted = shift(key)
    decrypt = []
    decrypted = ""

    for letter in shifted[-key:]:
        shifted.remove(letter)
        decrypt.append(letter)
    decrypt.extend(shifted)

    for letter in word:
        for position in range(len(shifted)):
            if shifted[position] == letter:
                decrypted += decrypt[position]
    return decrypted


encrypt = encrypt("test", 2)
print(encrypt)

decrypt = decrypt(encrypt, 2)
print(decrypt)
