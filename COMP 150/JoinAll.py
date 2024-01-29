def joinStrings(stringList):
    word = " "
    for string in stringList:
        word = word + string
    return word

def main():
    print(joinStrings(['chocolate', 'ice', 'cream']))
    print(joinStrings(['beautiful', 'sunny', 'beach']))
    print(joinStrings(['red', 'hot', 'peppers']))

main()
