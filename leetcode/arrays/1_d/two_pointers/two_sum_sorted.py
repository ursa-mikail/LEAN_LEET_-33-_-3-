def two_sum_sorted(nums, target):
    """
    Given a sorted array, find two numbers that add up to target.
    Return their indices (1-indexed).
    
    Example: nums = [2, 7, 11, 15], target = 9 → [1, 2]
    """
    # Your code here
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Test cases
print(two_sum_sorted([2, 7, 11, 15], 9))  # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))       # [1, 3]
print(two_sum_sorted([-1, 0], -1))        # [1, 2]

"""
[1, 2]
[1, 3]
[1, 2]
"""