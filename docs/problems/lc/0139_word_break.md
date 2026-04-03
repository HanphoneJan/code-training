---
title: 单词拆分
platform: LeetCode
difficulty: 中等
id: 139
url: https://leetcode.cn/problems/word-break/
tags:
  - 字符串
  - 动态规划
  - 回溯
  - 记忆化搜索
topics:
  - ../../topics/string.md
  - ../../topics/dynamic_programming.md
  - ../../topics/backtracking.md
patterns:
  - ../../patterns/dynamic_programming.md
date_added: 2026-04-03
date_reviewed: []
---

# 0139. 单词拆分

## 题目描述

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。请你判断是否可以利用字典中出现的单词拼接出 `s`。

**注意：** 不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

## 示例

**示例 1：**
```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```

**示例 2：**
```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
注意你可以重复使用字典中的单词。
```

**示例 3：**
```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

---

## 解题思路

### 第一步：理解问题

判断字符串 `s` 能否被完全拆分成字典中的单词。这是一个**完全背包 / 分割型 DP** 问题。

### 第二步：暴力解法 - 回溯

从位置 0 开始，枚举所有可能的结束位置，如果子串在字典中，就递归检查剩余部分。

```python
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    def dfs(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and dfs(end):
                return True
        return False
    return dfs(0)
```

没有剪枝时会超时，因为同一个位置可能被重复计算很多次。

### 第三步：优化 - 记忆化搜索

用 `lru_cache` 或数组记录每个位置是否可拆分，避免重复计算：

```python
from functools import lru_cache

def wordBreak(s, wordDict):
    word_set = set(wordDict)
    @lru_cache
    def dfs(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and dfs(end):
                return True
        return False
    return dfs(0)
```

### 第四步：最优解法 - 动态规划

设 `dp[i]` 表示 `s[0:i]`（前 i 个字符）是否可以被拆分。

状态转移：
```
dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
```

```python
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
```

时间复杂度：`O(n²)`，空间复杂度：`O(n)`。

---

## 完整代码实现

```python
from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    """
    139. 单词拆分 - 记忆化搜索

    核心思想：
    从位置 k 开始枚举所有结束位置，如果子串在字典中，递归检查剩余部分。
    使用 lru_cache 避免重复计算同一位置的结果。

    时间复杂度：O(m²)
    空间复杂度：O(m)
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 字符频率剪枝
        s_counter = Counter(s)
        dict_counter = Counter()
        for word in wordDict:
            dict_counter.update(word)
        for ch, cnt in s_counter.items():
            if cnt > dict_counter.get(ch, 0):
                return False

        m = len(s)
        word_set = set(wordDict)
        ans = False

        @lru_cache(maxsize=None)
        def dfs(k: int):
            nonlocal ans
            if k == m:
                ans = True
                return
            if ans:
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
```

---

## 示例推演

以 `s = "leetcode"`, `wordDict = ["leet", "code"]` 为例。

**dfs(0)**：从位置 0 开始
- i = 0~3，path = `"leet"`，在字典中，进入 **dfs(4)**
  - i = 4~7，path = `"code"`，在字典中，进入 **dfs(8)**
    - k == 8 == m，ans = True，返回

最终答案：`True`

以 `s = "catsandog"`, `wordDict = ["cats", "dog", "sand", "and", "cat"]` 为例：

**dfs(0)**：
- `"cats"` 在字典中，进入 **dfs(4)**
  - `"and"` 在字典中，进入 **dfs(7)**
    - `"og"` 不在字典中，`"dog"` 需要 `s[7:10]`，但字符串只剩 2 个字符
    - 没有可选路径，返回 False
  - `"sand"` 在字典中，进入 **dfs(8)**
    - 只剩 `"og"`，不在字典中
- `"cat"` 在字典中，类似的分析也会发现无法完全匹配

最终答案：`False`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力回溯 | O(2^n) | O(n) | 无记忆化会超时 |
| 记忆化搜索 | O(n²) | O(n) | 避免重复计算 |
| 动态规划 | O(n²) | O(n) | **最优解** |

---

## 易错点总结

### 1. 字符频率剪枝

当字典很大时，先进行字符频率剪枝可以快速排除一些无解情况。

### 2. lru_cache 的清零

如果同一个 Solution 实例被多次调用，Python 的 `@lru_cache` 基于函数对象，会被复用。在测试中最好每次新建实例。

### 3. DP 的初始状态

`dp[0] = True` 表示空字符串总是可以被拆分（作为基准状态）。

---

## 扩展思考

### 如果要求输出所有拆分方案？

就是 [140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/)，需要在回溯时记录路径。

### 如果字典中的单词只能用一次？

那就变成了排列组合问题，需要用状态压缩 DP。

## 相关题目

- [140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/)
- [472. 连接词](https://leetcode.cn/problems/concatenated-words/)
