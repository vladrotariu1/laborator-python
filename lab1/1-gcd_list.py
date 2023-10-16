import math
from functools import reduce

size = int(input('Enter size of array: '))
numbers_list = [int(input('Enter a value: ')) for _ in range(size)]
result = reduce(math.gcd, numbers_list)

print(result)
