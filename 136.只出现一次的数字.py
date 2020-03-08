#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
# [1] 数学方法 --> 36 ms	15.2 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 利用set将nums变为没有重复数字的列表
        return 2*sum(set(nums)) - sum(nums)

# [2] 位运算 --> 36 ms	14.8 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor运算
        # a ^ 0 = a     a ^ a = 0
        res = 0
        for n in nums:
            res ^= n
        return res
# @lc code=end

