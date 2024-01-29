def letterGrade(score):
    if score < 60:
        letter = 'F'
    elif score < 70:
        letter = 'D'
    elif score < 80:
        letter = 'C'
    elif score < 90:
        letter = 'B'
    else:
        letter = 'A'
    return letter

def main():
    x = float(input('Enter a numerical grade: '))
    letter = letterGrade(x)
    print('Your grade is ' + letter + '.')

main()