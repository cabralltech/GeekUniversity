from random import randint

nums = []
c = 0
while c < 6:
    n = randint(1, 99)
    if n % 2 ==0 and n not in nums:
        nums.append(n)
        c += 1
print(nums)
print('- ' * 15)
print(nums[::-1])
