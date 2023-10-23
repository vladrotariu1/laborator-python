from collections import Counter


def get_values_occurring_n_times_in_lists(lists, number_occurrences):
    dictionary = Counter({})
    result = []

    for lst in lists:
        dictionary += Counter(lst)

    for key, value in dict(dictionary).items():
        if value == number_occurrences:
            result.append(key)

    return result


def main():
    result = get_values_occurring_n_times_in_lists([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2)
    print(result)


if __name__ == "__main__":
    main()
