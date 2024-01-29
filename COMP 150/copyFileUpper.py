def main():
    file = input('What file would you like to modify to all uppercase? (ex. note.txt): ')

    f = open(file, 'r')
    m = open('UPPER' + file, 'w')

    for line in f:
        m.write(line)

main()