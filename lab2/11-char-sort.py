def sort_by_3rd_char(*lists):

    for l in lists:
        if len(l) < 2:
            print("List" + str(l) + "is invalid")
            return

    return sorted(lists, key=lambda i: i[1][2])


def main():
    result = sort_by_3rd_char(['abc', 'bcd'], ['abc', 'zza'])
    print(result)


if __name__ == "__main__":
    main()
