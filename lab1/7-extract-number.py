def first_number(string):
    number = ''
    number_started = False
    for char in string.split():
        if char.isnumeric():
            number_started = True
            number += char
        else:
            if number_started is True:
                return number

    return number


input_string = str(input('Enter your text: '))
first_number_in_text = first_number(input_string) if first_number(input_string) != '' else None
print(first_number(input_string))
