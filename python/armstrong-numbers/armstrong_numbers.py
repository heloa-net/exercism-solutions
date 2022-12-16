def is_armstrong_number(number):
    digits = [int(digit) for digit in list(str(number))]
    length = len(digits)

    return sum(digits[n] ** length for n in range(length)) == number