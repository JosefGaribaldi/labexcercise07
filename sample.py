def Fizzbuzz(value):
    string = ''
    if value%5 == 0:
        string += 'Fizz'
    if value%3 == 0:
        string += 'Buzz'
    return string

assert Fizzbuzz(15) == 'Fizz'