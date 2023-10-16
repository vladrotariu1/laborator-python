def count_words(text):
    return len(text.split(' '))


input_string = str(input('Enter your text: '))
number_of_words = count_words(input_string)

print(number_of_words)
