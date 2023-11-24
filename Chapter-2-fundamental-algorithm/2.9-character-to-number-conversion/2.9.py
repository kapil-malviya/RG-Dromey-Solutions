'''

Given the character representation of an integer convert it to its conventional decimal format.
  
'''


def char_to_decimal(char_value):
    decimal_value = 0

    for char in char_value:
        if '0' <= char <= '9':
            digit = int(char)
            decimal_value = decimal_value * 10 + digit
        else:
            raise ValueError("invalid character in the representation")

    return decimal_value

char_value = "123"
decimal_result = char_to_decimal(char_value)

print(f"character value: {char_value}")
print(f"decimal value : {decimal_result}")
print(type(decimal_result))
