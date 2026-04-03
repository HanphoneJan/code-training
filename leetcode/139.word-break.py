#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start
from typing import List
from collections import Counter
from functools import lru_cache

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    139. 单词拆分 - 记忆化搜索 / 动态规划

    核心思想：
    判断字符串 s 能否被拆分成 wordDict 中的一个或多个单词。
    这是一个典型的 "能否恰好分割" 问题，可以用记忆化搜索（DFS + 剪枝）解决。

    算法框架：
    从位置 k 开始，枚举所有可能的结束位置 i：
    - 如果 s[k:i+1] 在 word_set 中，递归检查 s[i+1:] 是否也能拆分
    - 如果能拆分到末尾（k == m），说明成功

    剪枝优化：
    1. 字符频率剪枝：如果 s 中某个字符的数量超过 wordDict 中该字符的总数，直接返回 False
    2. lru_cache 记忆化：避免重复计算同一位置的搜索结果
    3. 提前终止：一旦找到可行解立即返回 True

    时间复杂度：O(m²)，m 为 s 的长度
    空间复杂度：O(m)，递归栈和记忆化缓存
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 字符频率剪枝
        s_counter = Counter(s)
        dict_counter = Counter()
        for word in wordDict:
            dict_counter.update(word)
        # 如果 s 中任一字符的计数 > 字典中该字符的总数，则不可能拆分
        for ch, cnt in s_counter.items():
            if cnt > dict_counter.get(ch, 0):
                return False

        m = len(s)
        word_set = set(wordDict)  # 转成集合，O(1) 查找

        ans = False

        @lru_cache(maxsize=None)  # 记忆化搜索，避免超时
        def dfs(k: int):
            nonlocal ans
            if k == m:
                ans = True
                return
            if ans:  # 已找到答案，提前返回
                return

            path = ""
            for i in range(k, m):
                path += s[i]
                if path in word_set:
                    dfs(i + 1)
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


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("a", ["a"], True),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("cars", ["car", "ca", "rs"], True),
    ]

    print("单词拆分 - 测试开始")
    for i, (s, wordDict, expected) in enumerate(tests, 1):
        # 清除 lru_cache 状态需要重新创建 Solution 实例
        sol = Solution()
        result = sol.wordBreak(s, wordDict)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: s='{s}' -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
