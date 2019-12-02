from functools import reduce
from random import randint

nums = [randint(1, 3) for x in range(10)]
soma = reduce(lambda x, y: x * y, nums)
print(nums)
print(soma)
