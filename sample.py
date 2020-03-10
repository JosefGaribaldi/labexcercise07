def Fizzbuzz(value):
    if value%5 == 0 and value%3 == 0:
        return 'FizzBuzz'
    if value%5 == 0:
        return 'Buzz'
    if value%3 == 0:
        return 'Fizz'

assert Fizzbuzz(15) == 'FizzBuzz'
assert Fizzbuzz(5) == 'Buzz'
assert Fizzbuzz(3) == 'Fizz'
assert Fizzbuzz(2) == 2