def merge_dictionaries(dict_1, dict_2, keep_1=False, keep_2=False):
    if keep_1 and keep_2:
        raise Exception("Only one variable can be true")

    result_dict = dict({})
    if keep_2:
        for item in dict_2.items():
            result_dict.setdefault(item[0], item[1])

        for item in dict_1.items():
            result_dict.setdefault(item[0], item[1])
    else:
        for item in dict_1.items():
            result_dict.setdefault(item[0], item[1])

        for item in dict_2.items():
            result_dict.setdefault(item[0], item[1])

    return result_dict


def merge_with_conflict_resolution(dict_1, dict_2):
    result_dict = dict({})

    for item in dict_1.items():
        result_dict.setdefault(item[0], item[1])

    for item in dict_2.items():
        if result_dict.get(item[0]) is not None:
            result_dict.setdefault([result_dict.get(item[0]), item[1]])

    return result_dict


def main():
    dict_1 = dict({
        "name": "John Doe",
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001"
        },
        "interests": ["programming", "reading"]
    })

    dict_2 = dict({
        "age": 35,
        "occupation": "Software Engineer",
        "address": {
            "state": "NY",
            "zipcode": "10002"
        },
        "interests": ["traveling", "photography"]
    })

    print(merge_dictionaries(dict_1, dict_2))
    print(merge_dictionaries(dict_1, dict_2, keep_2=True))

    print(merge_with_conflict_resolution(dict_1, dict_2))


if __name__ == "__main__":
    main()
