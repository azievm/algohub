"""
Monotonic Stack patterns.
"""

# --------------------------------------------------
# Next Greater Element
# --------------------------------------------------

def next_greater_elements(nums):
    stack = []
    result = [-1] * len(nums)

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result


if __name__ == "__main__":
    print(next_greater_elements([2,1,2,4,3]))  # [4,2,4,-1,-1]
