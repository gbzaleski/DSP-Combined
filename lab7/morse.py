
MORSE_CODE_DICT = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ' ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}

def morse_encode(input : str) -> str:
    result = ""
    for letter in input.upper():
        if letter in MORSE_CODE_DICT:
            result += MORSE_CODE_DICT[letter] + " "
        else:
            result += letter + " "

    return result[:-1]

def morse_decode(input : str) -> str:
    result = ""

    for letter in input.split(" "):
        for key in MORSE_CODE_DICT:
            if MORSE_CODE_DICT[key] == letter:
                result += key
                break

    return result
        