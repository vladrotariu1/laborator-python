def is_palindrome(number):
    return str(number) == str(number)[::-1]


def get_palindrome_count_and_max_palindrome(numbers_list):
    palindrome_list = [x for x in numbers_list if is_palindrome(x)]

    return tuple([len(palindrome_list), max(palindrome_list)])


def main():
    result = get_palindrome_count_and_max_palindrome([11211, 45, 132, 121, 9001009])
    print(result)


if __name__ == "__main__":
    main()
