#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
'''
# [1] 暴力法 --> 通过	7608 ms	14.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res
'''
# [2] 两遍哈希表 --> 通过	56 ms	14.9 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = dict()
        # 创建哈希表，key为nums中的值，value为对应的下标
        for index, value in enumerate(nums):
            hasmap[value] = index
        # 遍历nums，查找target-num是否在HasMap中，且不是本身
        for i in range(len(nums)):
            if target-nums[i] in hasmap and i != hasmap.get(target-nums[i]):
                return [i, hasmap.get(target-nums[i])]

# @lc code=end

