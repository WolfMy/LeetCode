#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
# 二分查找 --> 108 ms	29.1 MB
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid + 1
            else:
                return mid
        return right
        
# @lc code=end

