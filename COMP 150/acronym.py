answer = input("Enter a phrase: ")

letters = (answer.replace('of', '')).split()

a = ""

for word in letters:
    a = a + word[0].upper()

print(f'The acronym of {answer} is {a}')