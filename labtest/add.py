def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
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