#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
# [1] 数学方法 --> 56 ms	14.9 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

# [2] 位运算（掩码思想） --> 44 ms	14.7 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 位运算
        # ones记录出现1次的二进制位
        # ones ^= num          0与num异或运算
        # twos记录出现2次的二进制位
        # twos |= ones & num   ones与num与运算，再与twos自身或运算
        # threes记录出现3次的二进制位
        # threes = ones & twos threes记录ones和twos都为1的位
        # 一次迭代后，将ones和twos中出现3次的位清零
        # ones &= ~threes   twos &= ~threes
        ones = twos = threes = 0
        for num in nums:
            # 先计算twos再计算ones，否则twos会计算num2次
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones

# @lc code=end

