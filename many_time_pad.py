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
    print(cipher_list[0][0])
    print(cipher_list[1][0])
    print(cipher_list[2][0])
    print(cipher_list[3][0])
    print(cipher_list[4][0])
    print(cipher_list[5][0])
    print(cipher_list[6][0])
    print(cipher_list[7][0])
    print(cipher_list[8][0])
    print(cipher_list[9][0])
    print(cipher_list[10][0])


def test_all_xor(xor):
    print("xor: " + str(xor))
    for possible in alphabet:
        # print("possible: " + possible)
        result = chr(ord(possible) ^ xor)
        if result in alphabet:
            print(ord(result), end=" ")

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


def main():

    # for i in range(127):
    #     print(i)
    #     test_all_xor(i)
    #     print()
    # test_all_xor(77)
    # return

    decoder()
    # for i in range(len(cipher_list)):

    # return
    plain_text = ""
    for pos in range(len(cipher_list[0])):
        print("Position: " + str(pos))
        print("Target: " + str(cipher_list[0][pos]))
        # valid_letters = [True] * len(alphabet)
        valid_letters = [True] * len(alphabet)
        best_letters = [0] * len(alphabet)
        for cipher in cipher_list[1:]:
            first_xor = cipher_list[0][pos] ^ cipher[pos]
            # print("Cipher: " + str(cipher[pos]))
            for idx in range(len(alphabet)):
                if chr(first_xor ^ ord(alphabet[idx])) not in alphabet:
                    valid_letters[idx] = False
                else:
                    print(alphabet[idx], end="")
                    best_letters[idx] += 1
            print()

        # print(valid_letters)
        # for idx in range(len(valid_letters)):
        #     if valid_letters[idx]:
        #         print(alphabet[idx], end="")
        #         plain_text += alphabet[idx]
        best_letter = 0
        best_idx = 0
        for idx in range(len(best_letters)):
            if best_letters[idx] > best_letter:
                best_letter = best_letters[idx]
                best_idx = idx
        print(alphabet[best_idx], end=" ")
        print(best_letters)
        plain_text += alphabet[best_idx]
        # print()
    print()
    print(plain_text)

    key = []
    for i in range(len(cipher_list[0])):
        key.append(cipher_list[0][i] ^ ord(plain_text[i]))
    print("key:", key)

    for cipher in cipher_list:
        decrypt(cipher, key)




    return
    for i in range(len(cipher_list)):
        cipher_list[i] = hex_splitter(cipher_list[i])
        # print(cipher_list[i][0])

    for i in range(1, len(cipher_list)):
        print("cipher text 1:\t", cipher_list[0][0])
        print("cipher text " + str(i+1) + ":\t", cipher_list[i][0])
        xor_0 = strxor(cipher_list[0][0], cipher_list[i][0])
        print("xor: ", (xor_0))
    return
    for i in range(len(xor_0_1)):
        possible_keys.append([])
        for letter in alphabet:
            # if test_key_char(ord(letter), ord(xor_0_1[i])) and test_key_char(ord(letter), ord(xor_0_2[i])):
            if test_key_char(ord(letter), ord(xor_0_1[i])):
                possible_keys[i].append(letter)
                # break
        # print(possible_keys[-1])
    for i in range(len(possible_keys)):
        print(cipher_list[0][i], cipher_list[1][i], possible_keys[i], xor_0_1[i])
        # print(xor_0_1[i])
    # print(len(possible_keys))
    # print(possible_key)




# def main():

#     possible_keys = []


#     for i in range(len(cipher_list)):
#         cipher_int_list.append(string_to_int_list(cipher_list[i]))
#     int_target = string_to_int_list(ciphertexts.target_ciphertext)
#     # print(cipher_int_list[0])
#     # print(cipher_int_list[1])

#     for letter in range(len(ciphertexts.target_ciphertext)):
#         # possible_keys.append([])
#         max_letter = ''
#         max_count = 0
#         for key in alphabet:
#             alpha_count = 0
#             isValid = True
#             if not test_key_char(ord(key), int_target[letter]):
#                 isValid = False
#                 # continue
#             else:
#                 alpha_count += 1

#             for i in range(len(cipher_int_list)):
#                 if not test_key_char(ord(key), cipher_int_list[i][letter]):
#                     isValid = False
#                     break
#                 else:
#                     alpha_count += 1
#             if alpha_count > max_count and isValid:
#                 max_letter = key
#                 max_count = alpha_count
#             # if isValid: possible_keys[letter].append(key)
#         possible_keys.append(max_letter)

#     # for i in range(len(possible_keys)):
#         # print(possible_keys[i])
#     print(possible_keys)




#     return

    # xor_out = cipher_int_list[0]
    # for i in range(1, len(cipher_int_list)):
    #     print("*****************", i)
    #     # temp = xor_out
    #     # xor_out = list_xor(xor_out, cipher_int_list[i])
    #     print(list_xor(cipher_int_list[0], cipher_int_list[i]))
    #     # for j in range(len(xor_out)):
    #     #     print(temp[j], "\t|\t", cipher_int_list[i][j], "\t|\t", xor_out[j])

        # print(xor_out)


    # strxor_0_1 = strxor(cipher_list[0], cipher_list[1])
    # print(strxor_0_1)
    # strxor_0_1_2 = strxor(strxor_0_1, cipher_list[2])
    # print(strxor_0_1_2)
    # strxor_0_1_2_3 = strxor(strxor_0_1_2, cipher_list[3])
    # print(strxor_0_1_2_3)
    # strxor_0_1_2_3_4 = strxor(strxor_0_1_2_3, cipher_list[4])
    # print(strxor_0_1_2_3_4)
    # strxor_0_1_2_3_4_5 = strxor(strxor_0_1_2_3_4, cipher_list[5])
    # print(strxor_0_1_2_3_4_5)
    # strxor_0_1_2_3_4_5_6 = strxor(strxor_0_1_2_3_4_5, cipher_list[6])
    # print(strxor_0_1_2_3_4_5_6)
    # strxor_0_1_2_3_4_5_6_7 = strxor(strxor_0_1_2_3_4_5_6, cipher_list[7])
    # print(strxor_0_1_2_3_4_5_6_7)
    # strxor_0_1_2_3_4_5_6_7_8 = strxor(strxor_0_1_2_3_4_5_6_7, cipher_list[8])
    # print(strxor_0_1_2_3_4_5_6_7_8)
    # strxor_0_1_2_3_4_5_6_7_8_9 = strxor(strxor_0_1_2_3_4_5_6_7_8, cipher_list[9])
    # print(strxor_0_1_2_3_4_5_6_7_8_9)

    # xor_out = cipher_list[0]
    # for i in range(1, len(cipher_list)):
    #     print("*****************", i)
    #     temp = xor_out
    #     xor_out = xor(xor_out, cipher_list[i])
    #     for j in range(len(xor_out)):
    #         # if xor_out[j] == '\x00':
    #             # xor_out[j] = ' '
    #         print(temp[j], "\t|\t", cipher_list[i][j], "\t|\t", xor_out[j])

    #     print(xor_out)
    # output = xor(cipher_list[0], cipher_list[1])
    # print(output)
    # for i in range(len(output)):
    #     print(type(output[i]))


if __name__ == "__main__":
    main()