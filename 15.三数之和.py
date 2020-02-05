#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
'''
排序 + 双指针
本题的难点在于如何去除重复解。
算法流程：
1. 特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
2. 对数组进行排序。
3. 遍历排序后数组：
        若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
        对于重复元素：跳过，避免出现重复解
        令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
            当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
            若和大于 0，说明 nums[R] 太大，RR 左移
            若和小于 0，说明 nums[L] 太小，LL 右移

作者：zhu_shi_fu
链接：https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 排序 遍历+双指针 --> 通过	736 ms	16.6 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 特判：n<3 则返回[]
        if n < 3:
            return res
        # 排序
        nums.sort()
        # 遍历nums，至倒数第二个
        for i in range(n-2):
            # 如果当前值大于0，后面都比0大，所以不存在三数和为0
            if nums[i] > 0:
                break
            # 如果当前值与左值相等，那么跳过
            if i >0 and nums[i] == nums[i-1]:
                continue
            # 双指针L、R，指向nums[i+1, n-1]
            L = i + 1
            R = n - 1
            while(L < R):
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 如果L和L+1位置的值相等，L继续右移
                    L += 1
                    while(L<R and nums[L]==nums[L-1]):
                        L += 1
                    # 如果R和R-1位置的值相等，R继续左移
                    R -= 1
                    while(L<R and nums[R]==nums[R+1]):
                        R -= 1
                elif sum < 0:
                    # 和小于0，说明nums[L]太小，L右移
                    L += 1 
                else:
                    # 和大于0，说明nums[R]太大，R左移
                    R -= 1
        return res
        
# @lc code=end

