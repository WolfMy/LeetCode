#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start

# [1] 图论+BFS --> 124 ms	17.2 MB
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList:
            return 0
        # 预处理：将字典里的单次，如hit拆分为 *it、h*t、hi* 三种形式
        n = len(beginWord)
        all_combinations = defaultdict(list)
        for word in wordList:
            for i in range(n):
                wildcard = word[:i] + '*' + word[i+1:]
                all_combinations[wildcard].append(word)
        # 存储已访问过的单词
        visited = {beginWord:True}
        queue = [(beginWord, 1)]
        while queue:
            nextword, level = queue.pop(0)
            # 尝试这个单词所有的通配形式
            for i in range(n):
                wildcard = nextword[:i] + '*' + nextword[i+1:]
                if wildcard in all_combinations:
                    # 若通配形式存在，那么把此形式的所有单词放进队列
                    for word in all_combinations[wildcard]:
                        if word == endWord:
                            return (level + 1)
                        # 进队列的前提是这个单词未被访问过
                        if word not in visited:
                            queue.append((word, level+1))
                            visited[word] = True
        return 0

