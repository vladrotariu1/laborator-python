camel_case_string = str(input('Enter your camel case string: '))
underscore_lower_case_string = ''.join(list(map(lambda letter: '_' + letter.lower() if letter.isupper() else letter, camel_case_string)))
underscore_lower_case_string = underscore_lower_case_string[1:] \
    if underscore_lower_case_string[0] == '_' \
    else underscore_lower_case_string

print(underscore_lower_case_string)
