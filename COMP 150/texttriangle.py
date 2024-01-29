n = int(input('Enter a small positive integer: '))
for k in range(n+1):
    for j in range(k):
        print('#', end='')
    print("")

print ('')

for k in range(n, 0, -1):
    for j in range(k):
        print('#', end='')
    print("")