def column_traversal(*lists):

    max_len = 0
    for l in lists:
        if len(l) > max_len:
            max_len = len(l)

    completed_lists = [l+[None for i in range(len(l), max_len)] for l in lists]

    return list(zip(*completed_lists))


def main():
    result = column_traversal([1,2,3], [5,6,7], ["a", "b", "c"])
    print(result)


if __name__ == "__main__":
    main()
