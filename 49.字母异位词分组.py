#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
# [1] 排序字符串相等 -->  104 ms	16.9 MB
# 思路：当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1:
            return [strs]
        # 哈希表 key:字符串排序后的字符数组  value:字符串排序后等于key的字符串
        ans = {}
        # 一次迭代
        for s in strs:
            # 此处必须转为元组
            anagram = tuple(sorted(s))
            if anagram not in ans:
                ans[anagram] = []
            ans[anagram].append(s)
        return ans.values()
''' 官方写法 --> 116 ms	17 MB
# collections.defaultdict(function_factory) 构建的是一个类似dict的对象
# 其中keys的值，自行确定赋值；但是values的类型，是function_factory的类实例，而且具有默认值。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1:
            return [strs]
        # 哈希表 key:字符串排序后的字符数组  value:字符串排序后等于key的字符串
        ans = collections.defaultdict(list)
        # 一次迭代
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
'''
# [2] 字符计数相等 --> 120 ms	18.6 MB
# 思路：当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1:
            return [strs]
        # 哈希表 key:计数元组  value:字符串排序后等于key的字符串
        ans = collections.defaultdict(list)
        # 一次迭代
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        
