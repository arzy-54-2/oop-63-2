

def find_element(array, target):
    for i in array:
        if i == target:
            print('+')
        else:
            print('-')

def binary_search(array, target):

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return '+'
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "-"



nums = [2,7,11,15]
target = 9

def two_sum(array, target):
    num_map = {}
    for i, j in enumerate(array):
        current = target - j
        if current in num_map:
            return [i, num_map[current]]
        num_map[j] = i

print(two_sum(nums, target))
