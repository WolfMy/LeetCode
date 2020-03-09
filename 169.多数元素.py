#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
# [1] 哈希表 --> 52 ms	14.8 MB
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hasmap = defaultdict(int)
        for num in nums:
            hasmap[num] += 1
            if hasmap[num] > n//2:
                return num
''' 可采用以下方式
counts = collections.Counter(nums)
return max(counts.keys(), key=counts.get)
'''
# @lc code=end

