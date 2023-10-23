def group_by_rhyme(words):
    rhyme_dict = {}

    for word in words:
        rhyme_key = word[-2:]

        if rhyme_key in rhyme_dict:
            rhyme_dict[rhyme_key].append(word)
        else:
            rhyme_dict[rhyme_key] = [word]

    return list(rhyme_dict.values())


def main():
    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    result = group_by_rhyme(words)
    print(result)


if __name__ == "__main__":
    main()


