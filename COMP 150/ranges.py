def main():
    n = int(input('Enter a number: '))
    num_sequence = []
    numbers = range(1, n+1)
    for n in numbers:
        if n == 4:
            num_sequence.append(n)
            print('Numbers 1 - 4', num_sequence)

        elif n >= 4:
            num_sequence.append(n)
            print('Numbers 1 -',n , num_sequence)

main()