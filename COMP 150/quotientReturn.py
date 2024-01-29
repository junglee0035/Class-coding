def quotientProblemString(x,y):
    quotient = x/y
    return 'The quotient of {} and {} is {}'.format(x, y, quotient)

def main():
    print(quotientProblemString(21,19))
    print (quotientProblemString(9,10))
    x = int(input('Enter an integer: '))
    y = int(input('Enter another integer: '))
    print(quotientProblemString(x,y))

main()