class Negative(Exception):
    pass

def Add(numbers):
    if numbers == '':
        return 0
    else:
        total = 0
        string = 'Negatives not allowed:'
        clean_string = ''
        while numbers != '':
            if numbers[0].isdigit() or numbers[0] == '-' and numbers[1].isdigit():
                clean_string += numbers[0]
            else:
                if clean_string == '' or clean_string[-1] == ',' or len(numbers) == 1:
                    pass
                else:
                    clean_string += ','
            numbers = numbers[1:]
        numbers = clean_string.split(',')
        for letter in numbers:
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
            return string

assert Add('') == 0
assert Add('1,2') == 3
assert Add('1,2,3,4,5') == 15
assert Add('10,2,5,22,1,1') == 41
assert Add('1\n2,3') == 6
assert Add('1\n2\n3') == 6
assert Add('1001,2') == 2
assert Add("//X\n1X2") == 3
assert Add("//%\n1%2%3") == 6 
assert Add('-1,2') == 'Negatives not allowed:-1'
assert Add("2,-4,3,-5") == 'Negatives not allowed:-4,-5'
