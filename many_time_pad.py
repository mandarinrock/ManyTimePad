import ciphertexts
import math
# import sys

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

cipher_list = ciphertexts.cipher_list
cipher_int_list = []

def xor(a, b):
    # return bytes([x ^ y for x, y in zip(a, b)])

    return [(ord(a) ^ ord(b)) for a, b in zip(a, b)]

# def strxor(a, b):     # xor two strings of different lengths
#     if len(a) > len(b):
#        return "".join([(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
#     else:
#        return "".join([(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def int_xor(a, b):
    return a ^ b

def list_xor(a, b):
    if len(a) > len(b): return [int_xor(a[i], b[i]) for i in range(len(b))]
    else: return [int_xor(a[i], b[i]) for i in range(len(a))]

def string_to_int_list(string):
    int_list = []
    for i in range(len(string)):
        int_list.append(ord(string[i]))
    return int_list

# def isAlpha(char):
#     if char >= 65 and char <= 90: return True
#     if char >= 97 and char <= 122: return True
#     if char == ord(' '): return True
#     return False

def test_key_char(key_char, cipher_char):
    # if not isAlpha(key_char): return False
    if chr(key_char ^ cipher_char) in alphabet: 
        # print(chr(key_char ^ cipher_char))
        return True
    return False

def int_list_to_string(int_list):
    string = ""
    for i in range(len(int_list)):
        string += chr(int_list[i])
    return string

def hex_splitter(hex_string):
    hex_list = []
    for i in range(0, len(hex_string), 2):
        hex_list.append(hex_string[i:i+2])
    return hex_list

def show_first_first_decode():
    cipher0_0 = bytes.fromhex(cipher_list[0][0:2])[0]
    print(cipher0_0)
    cipher0_1 = bytes.fromhex(cipher_list[0])[1]
    print(cipher0_1)

def decoder():
    for i in range(len(cipher_list)):
        # cipher_list[i] = hex_splitter(cipher_list[i])
        cipher_list[i] = bytes.fromhex(cipher_list[i])
    # print(cipher_list[0][0])
    # print(cipher_list[1][0])
    # print(cipher_list[2][0])
    # print(cipher_list[3][0])
    # print(cipher_list[4][0])
    # print(cipher_list[5][0])
    # print(cipher_list[6][0])
    # print(cipher_list[7][0])
    # print(cipher_list[8][0])
    # print(cipher_list[9][0])
    # print(cipher_list[10][0])


def test_all_xor(xor):
    print("xor: " + str(xor))
    for possible in alphabet:
        # print("possible: " + possible)
        result = chr(ord(possible) ^ xor)
        # if result in alphabet:
        #     print(ord(result), end=" ")

def decrypt(cipher, key):
    if len(cipher) < len(key):
        for i in range(len(cipher)):
            letter= chr(cipher[i] ^ key[i])
            print(letter, end="")
        print()
    else:
        for i in range(len(key)):
            letter= chr(cipher[i] ^ key[i])
            print(letter, end="")
        print()

def get_longest_length(lists):
    longest = 0
    for i in range(len(lists)):
        if len(lists[i]) > longest:
            longest = len(lists[i])
    return longest


def main():
    decoder()
    plain_text = ""
    keys = []
    for cipher_idx in range(len(cipher_list)):
        for pos in range(len(cipher_list[cipher_idx])):
            valid_letters = [True] * len(alphabet)
            best_letters = [0] * len(alphabet)
            for cipher in cipher_list[1:]:
                if pos < len(cipher):
                    first_xor = cipher_list[cipher_idx][pos] ^ cipher[pos]
                    for idx in range(len(alphabet)):
                        if chr(first_xor ^ ord(alphabet[idx])) not in alphabet:
                            valid_letters[idx] = False
                        else:
                            best_letters[idx] += 1
            best_letter = 0
            best_idx = 0
            for idx in range(len(best_letters)):
                if best_letters[idx] > best_letter:
                    best_letter = best_letters[idx]
                    best_idx = idx
            plain_text += alphabet[best_idx]

        key = []
        for i in range(len(cipher_list[0])):
            key.append(cipher_list[0][i] ^ ord(plain_text[i]))
        print("key:", key)
        keys.append(key)

        # for cipher in cipher_list:
        #     decrypt(cipher, key)
    print(keys)
    key_results = [] * get_longest_length(keys)
    for possible in key_results:
        key_results.append([0] * 256)
    for i in range(len(keys)):
        for j in range(len(keys[i])):
            print("i: ", i)
            print("j: ", j)
            print(len(keys))
            print(len(keys[i]))
            print(keys[i][j])
            key_results[j][keys[i][j]] += 1
    best_key = [0] * len(key_results)
    for i in range(len(key_results)):
        most_freq = 0
        most_idx = 0
        for j in range(len(key_results[i])):
            if key_results[i][j] > most_freq:
                most_freq = key_results[i][j]
                most_idx = j
        best_key[i] = most_idx
    print(best_key)
    for cipher in cipher_list:
        decrypt(cipher, best_key)






    return


if __name__ == "__main__":
    main()