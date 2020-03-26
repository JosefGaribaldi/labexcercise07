class Negative(Exception):
    pass

def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
        string = 'Negatives not allowed:'
        if '\n' in numbers:
            numbers = numbers.replace('\n', ',')
        if ',' in numbers:
            numbers = numbers.split(',')
        for letter in numbers:
            if letter.isdigit():
                if int(letter) < 1000:
                    if int(letter) < 0:
                        if string != 'Negatives not allowed:':
                            string+= ','
                        string += letter
                    else:
                        total += int(letter)
            else:
                pass
        if string == 'Negatives not allowed:':
            return total
        else:
            return Negative(string)

assert Add('') == 0
assert Add('1,2') == 3
assert Add('1,2,3,4,5') == 15
assert Add('10,2,5,22,1,1') == 41
assert Add('1\n2,3') == 6
assert Add('1\n2\n3') == 6
assert Add('1001,2') == 2
assert Add('-1,2') == Negative('Negatives not allowed:-1')