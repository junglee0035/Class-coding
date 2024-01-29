def printLocations(s, target):
    repetitions = s.count(target)
    portionOfString = s
    position = 0
    temporary = 0
    for i in range(repetitions):
        position = portionOfString.find(target)
        portionOfString.find(target)
        # print(portionOfString)
        print(position + temporary)
        position += 1
        temporary = temporary + position
        portionOfString = portionOfString[position:]
    print("_____")

def main():
    phrase = 'Here, there, everywhere!'
    print('Phrase:', phrase)
    for target in ['ere', 'er', 'e', 'eh', 'zx']:
        print('finding:', target)
        printLocations(phrase, target)
    print('All done!')

main()
