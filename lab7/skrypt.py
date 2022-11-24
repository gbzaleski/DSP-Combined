import caesar
import morse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-e", action = "store_const", const = "e",
                    dest = "action_type", help = "encryption of file")
parser.add_argument("-d", action = "store_const", const = "d",
                    dest = "action_type", help = "decryption of file")

parser.add_argument("input_file", help = "file to be read")
parser.add_argument("output_file", help = "file to save result")

parser.add_argument("-c", action = "store_const", const = "c",
                    dest = "cipher_type", help = "caesar cipher to encode or decode")
parser.add_argument("-m", action = "store_const", const = "m",
                    dest = "cipher_type", help = "morse code to encode or decode")

parser.add_argument("-n", type = int, default = 3, nargs = "?", dest = "shift",
                    help = "value of the right shift of the letters in the cipher")

args = parser.parse_args()

def cipher(action_type, input_file, output_file, cipher_type, shift):
    with open(input_file, 'r') as r_f, open(output_file,'w') as w_f:
        for line in r_f:
            stripped_line = line.strip()
            if cipher_type == "m":
                if action_type == "e":
                    w_f.write(morse.morse_encode(stripped_line))
                if action_type == "d":
                    w_f.write(morse.morse_decode(stripped_line))
            if cipher_type == "c":
                if action_type == "e":
                    w_f.write(caesar.encrypt_caesar(stripped_line, shift))
                if action_type == "d":
                    w_f.write(caesar.decrypt_caesar(stripped_line, shift))
            w_f.write('\n')


cipher(args.action_type, args.input_file, args.output_file, args.cipher_type, args.shift)
