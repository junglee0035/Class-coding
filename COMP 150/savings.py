def main():
    initial = float(input('Enter initial balance: '))
    annual = float(input('Enter annual percentage(ex: .04): '))
    desired = float(input('Enter desired balance: '))

    ci1= initial * (pow((1 + annual), 1))
    ci2 = initial * (pow((1 + annual), 2))
    ci3 = initial * (pow((1 + annual), 3))

    print(initial)
    print("%.2f" % ci1)
    print("%.2f" % ci2)
    print("%.2f" % ci3)

main()