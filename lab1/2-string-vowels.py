from functools import reduce

string = str(input('Enter string: '))
numb_vowels = reduce(lambda cumulator, current_char: cumulator + 1 if current_char.lower() in 'aeiou' else cumulator, string, 0)

print(numb_vowels)
