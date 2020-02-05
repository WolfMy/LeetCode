#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
# 排序 双循环遍历+双指针 --> 通过	164 ms	13 MB
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        # 特判：nums长度小于4，返回[]
        if n < 4:
            return []
        # 排序
        nums.sort()
        # 双循环遍历nums
        for i in range(n-3):
            # 如果i与左值相等，那么跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ######################################## 优化执行时间
            # 如果当前i对应的和的最小值都大于target，那么结束循环
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 如果当前i对应的和的最大值都小于target，那么跳过
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            ##################################################
            for j in range(i+1, n-2):
                # 如果j与左值相等，那么跳过
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                ######################################## 优化执行时间
                # 如果当前j对应的和的最小值都大于target，那么结束循环
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 如果当前i对应的和的最大值都小于target，那么跳过
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                ##################################################
                L = j + 1
                R = n - 1
                while(L < R):
                    sum = nums[i] + nums[j] + nums[L] + nums[R]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        # 如果L和L+1位置的值相等，L继续右移
                        L += 1
                        while(L<R and nums[L]==nums[L-1]):
                            L += 1
                        # 如果R和R-1位置的值相等，R继续左移
                        R -= 1
                        while(L<R and nums[R]==nums[R+1]):
                            R -= 1
                    elif sum < target:
                        # 和小于target，说明nums[L]太小，L右移
                        L += 1
                    else:
                        # 和大于target，说明nums[R]太大，R左移
                        R -= 1
        return res

# @lc code=end

