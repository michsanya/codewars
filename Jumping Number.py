def jumping_number(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10

    if len(digits) < 2:
        return "Jumping!!"

    i = 1
    for digit in digits:
        if len(digits) != i:
            if (digit - digits[i] == 1) & (digit - digits[i] == -1):
                i += 1
                continue
            else:
                return "Not!!"
        else:
            return "Jumping!!"

print (jumping_number(12321))

jumping_number(1232125)
