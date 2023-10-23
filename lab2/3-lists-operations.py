def get_computed_sets(a, b):
    return (
        a.intersection(b),
        a.union(b),
        a - b,
        b - a
    )


def main():
    size_first_array = int(input('Enter size of first array: '))
    first_array = [int(input('Enter a value: ')) for _ in range(size_first_array)]

    size_second_array = int(input('Enter size of second array: '))
    second_array = [int(input('Enter a value: ')) for _ in range(size_second_array)]

    primes = get_computed_sets(set(first_array), set(second_array))

    print(primes)


if __name__ == "__main__":
    main()