#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
# [1] 回溯算法+记忆化 --> 超出时间限制
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 哈希表实现记忆化  position:True/False 表示当前位置是否可达最后一个位置
        self.hasmap = {}
        return self.backtrack(0, nums)

    def backtrack(self, position, nums):
        if position == len(nums) - 1:
            return True
        if position in self.hasmap:
            return self.hasmap[position]
        
        # 最远可到达的位置
        furthestPostition = min(position+nums[position], len(nums)-1)
        for i in range(furthestPostition, position, -1):
            if self.backtrack(i, nums):
                return True

        self.hasmap[position] = False
        return False

# [2] 动态规划（自底向上） --> 超出时间限制
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        # 哈希表实现记忆化  position:True/False 表示当前位置是否可达最后一个位置
        hasmap = {n-1:True}
        # 自底向上动态规划
        for position in range(n-2, -1, -1):
            hasmap[position] = False
            furthestPosition = min(position+nums[position], n-1)
            for i in range(furthestPosition, position, -1):
                if hasmap[i]:
                    hasmap[position] = True
                    break
        return hasmap[0]

# [3] 贪心算法 --> 44 ms	14.8 MB
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        lastPosition = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0
        ''' 52 ms	14.6 MB
        class Solution:
        def canJump(self, nums: List[int]) -> bool:
            n = len(nums)
            if n <= 1:
                return True
            # 记录最远能到达的位置
            furthestPosition = 0
            for i in range(n-1):
                position = i + nums[i]
                # 如果当前位置可达，并且当前位置的最远距离 大于 最远能到达的位置，那么更新最远能到达的位置
                if furthestPosition >= i and position > furthestPosition:
                    furthestPosition = position
            return furthestPosition >= n-1
        '''

# @lc code=end

