#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
# 移位+减法 --> 152 ms	29 MB
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            # 除数左移1位，相当于乘2
            divisor <<= 1
        result = 0
        while count:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                result += 1 << count
                dividend -= divisor
        if sign:    result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1
        
# @lc code=end

