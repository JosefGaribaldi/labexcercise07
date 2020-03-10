def Fizzbuzz(value):
    if value%5 == 0 and value%3 == 0:
        return 'FizzBuzz'

assert Fizzbuzz(15) == 'FizzBuzz'
print(Fizzbuzz(15))
print(Fizzbuzz(5))
print(Fizzbuzz(9))
print(Fizzbuzz(2))