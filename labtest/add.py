def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
        if '\n' in numbers:
            numbers = numbers.replace('\n', ',')
        if ',' in numbers:
            numbers = numbers.split(',')
        for letter in numbers:
            if letter.isdigit():
                total += int(letter)
            else:
                pass
        return total

assert Add('') == 0
assert Add('1,2') == 3
assert Add('1,2,3,4,5') == 15
assert Add('10,2,5,22,1,1') == 41
assert Add('1\n2,3') == 6
assert Add('1\n2\n3') == 6