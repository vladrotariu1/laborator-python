def is_palindrome(string):
    return string == string[::-1]


input_string = str(input('Enter your string: '))
print(is_palindrome(input_string))
