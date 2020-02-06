#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
'''
将快指针（当前遍历的数字）和慢指针指向的数字的前一个数字比较（也就是满足条件的倒数第 2 个数）。
    - 如果相等，因为有序，所以倒数第 1 个数字和倒数第 2 个数字都等于当前数字，再添加就超过 2 个了。
    - 如果不相等，那么就添加。
作者：gsmplaysnswithnx
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/javakuai-man-zhi-zhen-jie-da-by-gsmplaysnswithnx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 快慢指针 --> 通过	72 ms	13.2 MB
# 如果每个元素最多出现三次，那么i=2,j=3,比较*j与*(i-2)是否相同
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        i = 1
        for j in range(2, len(nums)):
            if nums[i-1] != nums[j]:
                if j - i > 1:
                    nums[i+1] = nums[j]
                i += 1
        return i + 1
        
# @lc code=end

