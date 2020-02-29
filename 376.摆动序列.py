#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
# 贪心算法 --> 32 ms	13.4 MB
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        diff = [nums[i]-nums[i-1] for i in range(1,n)]
        prevdiff = diff[0]
        count = 1 if prevdiff==0 else 2
        for i in range(1, n-1):
            if (prevdiff>=0 and diff[i]<0) or (prevdiff<=0 and diff[i]>0):
                count += 1
                prevdiff = diff[i]
        return count
        
# @lc code=end

