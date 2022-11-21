
ALPHABET_SIZE = 26
ALPHABET_FIRST = ord('A')

def encrypt_caesar(input : str, key : int) -> str:
    result = ""
    for letter in input.upper():
        value = (ord(letter) - ALPHABET_FIRST + key) % ALPHABET_SIZE
        result += chr(ALPHABET_FIRST + value)

    return result

def decrypt_caesar(input : str, key : int) -> str:
    return encrypt_caesar(input, ALPHABET_SIZE - key)
