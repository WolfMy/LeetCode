#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
'''
# [1] 动态规划（记忆化） --> 404 ms	16.9 MB
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        # 动态规划 d[x] = sum(nums[:x]) (1<=x<=n, d[0]=0)
        # 所以sumRange(i, j) = d[j+1] - d[i]
        # 添加缓存
        self.cache = {}

    def sumRange(self, i: int, j: int) -> int:
        if not i in self.cache:
            self.cache[i] = sum(self.nums[:i])
        if not j+1 in self.cache:
            self.cache[j+1] = sum(self.nums[:j+1])

        return self.cache[j+1] - self.cache[i]
'''
# [2] 动态规划（提前计算） --> 通过	164 ms	16.6 MB
class NumArray:
    def __init__(self, nums: List[int]):
        if(not nums):
            return 
        n=len(nums)
        self.dp=[0]*(n+1)
        self.dp[1]=nums[0]
        for i in range(2,n+1):
            self.dp[i]=nums[i-1]+self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# @lc code=end

