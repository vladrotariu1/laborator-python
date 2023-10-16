def get_number_of_1_bits(number):
    return int.bit_count(number)


input_number = int(input('Enter a value: '))
print(get_number_of_1_bits(input_number))
