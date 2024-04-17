# Author: Sakthi Santhosh
# Created on: 12/04/2024
#
# LeetCode: Two Sum (https://leetcode.com/problems/two-sum/)
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            if target - num in hashmap:
                return hashmap[target - num], index

            hashmap[num] = index

if __name__ == "__main__":
    Solution().two_sum([1, 2, 3, 4, 5], 7)
