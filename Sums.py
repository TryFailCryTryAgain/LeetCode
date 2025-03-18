
nums = [1,5,12,3,6]
target = 21
self = 2

sorted = set(nums)
"""
Logic steps:

1. take the num array and sort it from lower -> higher (set(nums))
2. Take the first num + second num inside the array, if its lower than the target j+1, when i + j+1 is > target, i+1, j-1, then i+1 + j, until its higher or equal
3. 

"""

for i in sorted:
    for j in sorted[i]:
        print(i + j)