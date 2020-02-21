#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
# [1] 快速幂算法（递归） --> 140 ms	29.1 MB
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        return self.fastPow(x, n)
    
    def fastPow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x

        half = self.fastPow(x, n//2)
        return half * half * self.fastPow(x, n%2)

# [2] 快速幂算法（迭代） --> 112 ms	29.2 MB
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        ans = 1
        current_product = x
        while n:
            if n % 2 == 1:
                ans *= current_product
            current_product *= current_product
            n //= 2
        return ans
        
# @lc code=end

