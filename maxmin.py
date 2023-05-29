# list = [2, 4, 1, 0, 2, -1]
list = [20, 50, 12, 6, 14, 8]
# list = [100, -100]


def min_max(lst):
    minimum = lst[0]
    maximum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return [minimum, maximum]


print(min_max(list))

# 1. Given a list of integers, return the highest and lowest numbers in the array (without using max() or min())
#   1. Some example inputs and outputs would look like the below:
#     1. [2, 4, 1, 0, 2, -1] should return the array [-1, 4]
#     2. [20, 50, 12, 6, 14, 8] should return the array [6, 50]
#     3. [100, -100] should return the array [-100, 100]
