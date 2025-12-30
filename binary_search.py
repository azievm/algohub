"""
Binary Search patterns.
Works on sorted arrays.
"""

# --------------------------------------------------
# Classic Binary Search
# --------------------------------------------------

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# --------------------------------------------------
# Leftmost occurrence (lower bound)
# --------------------------------------------------

def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    print(binary_search([1,2,3,4,5], 4))  # 3
    print(lower_bound([1,2,2,2,3], 2))    # 1
