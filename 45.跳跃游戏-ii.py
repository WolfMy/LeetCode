#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# [1] 贪心算法（正向思维） --> 64 ms	14.8 MB
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        # 思路：总是跳到当前位置能到达范围内的最大的数
        steps = 0
        # 记录当前‘步数’能走到的最远位置
        end = 0
        # 记录当前‘位置’能到达的最远位置
        furthestPos = 0
        for position in range(n-1):
            # 每次更新 当前‘位置’能到达的最远位置
            furthestPos = max(furthestPos, position+nums[position])
            # 如果走到了 当前‘步数’能走到的最远位置，那么步数+1
            if position == end:
                end = furthestPos
                steps += 1
        return steps
        
# [2] 贪心算法（逆向思维）--> 超出时间限制（全1情况）
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        # 思路：已知一定能到达最后一个位置，那么我们去找距离最后一个位置最远且可达的位置，直到找到第0个位置
        lastPos = n - 1
        steps = 0
        while lastPos != 0:
            # 从左至右查找，第一个能到达lastPos的位置，更新lastPos和steps
            for i in range(n-1):
                if i + nums[i] >= lastPos:
                    lastPos = i
                    steps += 1
                    break
        return steps
# @lc code=end

