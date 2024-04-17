# Author: Sakthi Santhosh
# Created on: 12/04/2024
#
# LeetCode: Palindrome Number (https://leetcode.com/problems/palindrome-number/)
class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp, reverse, weight = x, 0, 1

        while temp:
            reverse = reverse * 10 + temp % 10
            weight *= 10
            temp //= 10

        return x == reverse

if __name__ == "__main__":
    Solution().is_palindrome(121)
