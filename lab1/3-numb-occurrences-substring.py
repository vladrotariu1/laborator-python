substring = str(input('Enter first string: '))
string = str(input('Enter second string: '))

numb_occurrences = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        numb_occurrences += 1

print(numb_occurrences)
