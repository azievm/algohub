"""
Prefix Sum examples.
"""

# --------------------------------------------------
# Build prefix sum
# --------------------------------------------------

def build_prefix_sum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix


# --------------------------------------------------
# Query range sum
# --------------------------------------------------

def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    p = build_prefix_sum(nums)
    print(range_sum(p, 1, 3))  # 9
