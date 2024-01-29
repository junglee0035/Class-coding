file = input('What file would you like to see the contents of? (ex. file.pdf): ')
f = open(file)
f.read().upper()
print("File Contents:",f.read().upper())
