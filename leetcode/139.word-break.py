#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 好题目，有思路但是写起来还是很麻烦
from typing import List
from collections import Counter
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 字符频率剪枝
        s_counter = Counter(s)
        # 统计所有单词中每个字符的总出现次数
        dict_counter = Counter()
        for word in wordDict:
            dict_counter.update(word)
        # 如果 s 中任一字符的计数 > 字典中该字符的总数，则不可能拆分
        for ch, cnt in s_counter.items():
            if cnt > dict_counter.get(ch, 0):
                return False
        m = len(s)
        word_set = set(wordDict)

        ans = False
        @lru_cache #lru_cache是必须的否则会超时
        def dfs(k:int):
            nonlocal ans
            if k == m:
                ans = True
                return
            path = ""
            for i in range(k,m):
                path += s[i]
                if path in word_set:
                    dfs(i+1)
                    if ans:
                        return
        dfs(0)
        return ans
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

