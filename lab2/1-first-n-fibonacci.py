def get_first_n_fibonacci(n):
    assert n >= 1, "Number should greater or equal to 1"

    if n == 1:
        return [1]

    fibonacci_array = [1, 1]

    for _ in range(n - 2):
        fibonacci_array.append(fibonacci_array[-1] + fibonacci_array[-2])

    return fibonacci_array


input_number = int(input('How many number you want to see: '))
result = get_first_n_fibonacci(input_number)

print(result)
