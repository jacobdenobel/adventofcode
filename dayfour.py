from itertools import groupby

input_range = (193651, 649729,)

matches = []
for number in range(*input_range):
    digits = str(number)
    last_digit = digits[0]

    for digit in digits[1:]:
        if int(digit) < int(last_digit):
            break
        last_digit = digit
    else:
        for k, group in groupby(digits):
            if len("".join(group)) == 2:
                matches.append(number)
                break
           
print(len(matches))


