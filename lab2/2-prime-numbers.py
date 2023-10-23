import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_primes(numbers_list):
    return list(filter(lambda number: is_prime(number), numbers_list))


def main():
    size = int(input('Enter size of array: '))
    numbers_list = [int(input('Enter a value: ')) for _ in range(size)]
    primes = get_primes(numbers_list)

    print(primes)


if __name__ == "__main__":
    main()
