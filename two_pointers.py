"""
Two Pointers examples in Python.

Used when scanning from both ends of a linear data structure.
Often reduces O(N^2) to O(N).
"""

# --------------------------------------------------
# 1. Valid Palindrome
# --------------------------------------------------

def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a valid palindrome.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# --------------------------------------------------
# 2. Container With Most Water
# --------------------------------------------------

def max_area(height):
    """
    Returns the maximum water container area.
    """
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current = min(height[left], height[right]) * width
        max_water = max(max_water, current)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
