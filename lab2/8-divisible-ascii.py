def ascii_divisible(strings_list, x=1, flag=True):
    result = []

    for string in strings_list:
        char_array = []
        for char in string:
            if ord(char) % x == 0 and flag is True:
                char_array.append(char)
            elif ord(char) % x != 0 and flag is not True:
                char_array.append(char)

        result.append(char_array)

    return result


def main():
    result = ascii_divisible(["test", "hello", "lab002"], 2, False)
    print(result)


if __name__ == "__main__":
    main()
