def quotientProblem(x,y):
    quotient = x/y
    sentence = 'The sum of {} and {} is {}'.format(x, y, quotient)
    print(sentence)

def main():
    quotientProblem(21,9)
    x = int(input('Enter an integer: '))
    y = int(input('Enter another integer: '))
    quotientProblem(x, y)

main()