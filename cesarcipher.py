import math as math

def string_to_characters(message):
    return list(message)

def get_ords(char_list):
    ord_list = []
    for element in char_list:
        ord_list.append(ord(element))

    return ord_list

def apply_shift(shift, ord_list):
    shifted_list = []
    for element in ord_list:
        shifted_list.append(element + shift)

    return shifted_list

def main():
    message = 'hello'
    message_list = string_to_characters(message)
    ord_list = get_ords(message_list)

