def collatz(number):
    if number % 2 == 0:
        print(number // 2, sep=' ')
        return number // 2
    else:
        print(3 * number + 1, sep=' ')
        return 3 * number + 1

try:
    number = int(input('Enter a number: '))
    number = collatz(number)
    while number != 1:
        number = collatz(number)
except ValueError:
    print('Please enter a number.')