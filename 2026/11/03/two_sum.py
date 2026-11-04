"""
Daily practice: Two Sum

Given a list of integers and a target integer, return the indices of the
two numbers that add up to the target.

You may assume that each input has exactly one solution, and you may not
use the same element twice.

Example:
    nums = [2, 7, 11, 15]
    target = 9
    two_sum(nums, target) -> [0, 1]
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return the indices of the two numbers that add up to target."""
    # Store each number and its index so we can find its complement later.
    seen = {}

    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i

    return []


if __name__ == "__main__":
    print(two_sum([3, 2, 4], 6))
