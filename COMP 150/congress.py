def main():
    age = int(input('What is your age? '))
    residency = int(input('How many years have you been a U.S citizen? '))
    if age >= 30 and residency >= 9:
        print('You are eligible for both the House and Senate!')
    elif age >= 25 and residency >= 7:
        print('You are eligible for only the House.')
    else:
        print('You are not eligible for congress.')

main()