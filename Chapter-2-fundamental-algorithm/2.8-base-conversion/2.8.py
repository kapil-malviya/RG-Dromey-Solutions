'''

Convert a decimal integer to its corresponding octal representation.

'''

def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return "0o0"

    octal_digits = []
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_digits.append(str(remainder))
        decimal_number //= 8

    octal_digits.reverse()
    octal_value = "0o" + "".join(octal_digits)
    return octal_value

decimal_number = 123
octal_result = decimal_to_octal(decimal_number)

print(f"decimal number: {decimal_number}")
print(f"octal number: {octal_result}")
