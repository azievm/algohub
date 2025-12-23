"""
Sliding Window examples in Python.

This file contains several classic Sliding Window problems,
ordered from basic to more advanced cases.

The core idea:
Maintain a window [left, right] and update the result incrementally
instead of recalculating everything from scratch.
"""

# --------------------------------------------------
# 1. Fixed-size window
# Task: find the maximum sum of a subarray of size k
# --------------------------------------------------

def max_sum_subarray(nums, k):
    """
    Returns the maximum sum of any contiguous subarray of length k.
    """
    window_sum = 0
    max_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        # Once the window reaches size k, process it
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)

            # Move the window forward
            window_sum -= nums[left]
            left += 1

    return max_sum


# --------------------------------------------------
# 2. Fixed-size window
# Task: calculate averages of all subarrays of size k
# --------------------------------------------------

def average_of_subarrays(nums, k):
    """
    Returns a list of averages for all contiguous subarrays of length k.
    """
    result = []
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 == k:
            result.append(window_sum / k)

            window_sum -= nums[left]
            left += 1

    return result


# --------------------------------------------------
# 3. Variable-size window
# Task: minimum length subarray with sum >= target
# --------------------------------------------------

def min_subarray_length(target, nums):
    """
    Returns the minimum length of a contiguous subarray
    whose sum is greater than or equal to target.
    """
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        # Try to shrink the window while the condition is satisfied
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float("inf") else min_length


# --------------------------------------------------
# 4. Variable-size window (strings)
# Task: longest substring without repeating characters
# --------------------------------------------------

def longest_unique_substring(s):
    """
    Returns the length of the longest substring
    without duplicate characters.
    """
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Remove characters until the current one becomes unique
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# --------------------------------------------------
# 5. Advanced case
# Task: count subarrays with sum less than or equal to k
# --------------------------------------------------

def count_subarrays_with_sum_at_most_k(nums, k):
    """
    Counts the number of contiguous subarrays
    whose sum is less than or equal to k.

    Assumes all numbers are non-negative.
    """
    left = 0
    current_sum = 0
    count = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        # All subarrays ending at 'right' and starting from [left..right]
        count += right - left + 1

    return count


# --------------------------------------------------
# Basic test runs
# --------------------------------------------------

if __name__ == "__main__":
    print("Max sum subarray:")
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9

    print("\nAverages of subarrays:")
    print(average_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

    print("\nMinimum subarray length:")
    print(min_subarray_length(7, [2, 3, 1, 2, 4, 3]))  # 2

    print("\nLongest unique substring:")
    print(longest_unique_substring("abcabcbb"))  # 3

    print("\nCount of subarrays with sum <= k:")
    print(count_subarrays_with_sum_at_most_k([1, 2, 1, 1, 1], 3))  # 10
