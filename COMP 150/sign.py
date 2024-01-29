def numberSign(number):
    if number > 0:
        sign = 'positive'
    elif number < 0:
        sign = 'negative'
    elif number == 0:
        sign = 'zero'
    return sign
def main():
    number = int(input('Pick a number: '))
    sign = numberSign(number)
    print('Your number is',(numberSign(number)))

main()

