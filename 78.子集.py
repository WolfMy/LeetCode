#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# [1] 递归算法 --> 36 ms	13.6 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [r+[n] for r in res]
        return res

# [2] 回溯算法 --> 48 ms	13.6 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, curr):
            if start == k:
                res.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
                
        res = []
        for k in range(len(nums)+1):
            backtrack(0, [])
        return res

# [3] 字典排序（二进制排序）子集 --> 64 ms	13.6 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nth_bit = 1 << n
        for i in range(2**n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            res.append([nums[bit] for bit in range(n) if bitmask[bit]=='1'])
        return res
# @lc code=end

