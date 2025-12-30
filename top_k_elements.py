"""
Top K Elements using Heaps.
"""

import heapq


# --------------------------------------------------
# Top K Largest
# --------------------------------------------------

def top_k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap


# --------------------------------------------------
# Top K Smallest
# --------------------------------------------------

def top_k_smallest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)

    return [-x for x in heap]


if __name__ == "__main__":
    print(top_k_largest([3,2,1,5,6,4], 2))   # [5,6]
    print(top_k_smallest([3,2,1,5,6,4], 2))  # [1,2]
