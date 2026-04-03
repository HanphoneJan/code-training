---
title: 分割回文串
platform: LeetCode
difficulty: 中等
id: 131
url: https://leetcode.cn/problems/palindrome-partitioning/
tags:
  - 字符串
  - 回溯
  - 动态规划
topics:
  - ../../topics/string.md
  - ../../topics/backtracking.md
patterns:
  - ../../patterns/backtracking.md
date_added: 2026-04-03
date_reviewed: []
---

# 0131. 分割回文串

## 题目描述

给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是 **回文串**。返回 `s` 所有可能的分割方案。

**回文串** 是正着读和反着读都一样的字符串。

## 示例

**示例 1：**
```
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
```

**示例 2：**
```
输入：s = "a"
输出：[["a"]]
```

---

## 解题思路

### 第一步：理解问题

需要把字符串切成若干段，每段都必须是回文。这是一个典型的**组合/分割问题**。

### 第二步：暴力解法

枚举所有可能的分割方式（每个位置都可以选择切或不切），然后检查每一段是否都是回文。

对于长度为 `n` 的字符串，有 `2^(n-1)` 种分割方式，时间复杂度 `O(n * 2^n)`。

### 第三步：回溯优化

在 DFS 的过程中，如果发现当前子串不是回文，就立即剪枝，不再往下递归。

### 第四步：最优解法 - 回溯 + 动态规划预处理

标准的回溯解法：
1. 从位置 `i` 开始，枚举结束位置 `j`
2. 如果 `s[i:j+1]` 是回文，加入路径，递归处理 `j+1`
3. 到达字符串末尾时记录方案

**进一步优化**：可以用动态规划预处理所有子串是否回文，把判断时间从 `O(n)` 降到 `O(1)`。但对于一般数据规模，直接翻转字符串判断（`t == t[::-1]`）已经足够。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    131. 分割回文串 - 回溯算法

    核心思想：
    从位置 i 开始枚举所有可能的结束位置 j，如果 s[i:j+1] 是回文串，
    就加入路径，然后递归处理 j+1 开始的子串。

    时间复杂度：O(n * 2^n)
    空间复杂度：O(n)，递归深度
    """

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1]:  # 是回文串
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
```

---

## 示例推演

以 `s = "aab"` 为例。

**dfs(0)**，i = 0：
- j = 0，t = `"a"`，是回文。path = `["a"]`，进入 **dfs(1)**
  - j = 1，t = `"a"`，是回文。path = `["a", "a"]`，进入 **dfs(2)**
    - j = 2，t = `"b"`，是回文。path = `["a", "a", "b"]`，进入 **dfs(3)**
      - i == 3 == n，ans 加入 `["a", "a", "b"]`，返回
    - 回溯，path = `["a", "a"]`
  - j = 2，t = `"ab"`，不是回文，跳过
  - 回溯，path = `["a"]`
- j = 1，t = `"aa"`，是回文。path = `["aa"]`，进入 **dfs(2)**
  - j = 2，t = `"b"`，是回文。path = `["aa", "b"]`，进入 **dfs(3)**
    - i == 3，ans 加入 `["aa", "b"]`，返回
  - 回溯，path = `["aa"]`
- j = 2，t = `"aab"`，不是回文，跳过
- 回溯，path = `[]`

最终结果：`[["a", "a", "b"], ["aa", "b"]]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n * 2^n) | O(n) | 枚举所有分割 |
| 回溯 | O(n * 2^n) | O(n) | **最优解**，回文判断可预优化 |

---

## 易错点总结

### 1. path 的拷贝

记录答案时必须用 `path.copy()` 或 `path[:]`，否则回溯后 path 内容会变。

### 2. 回文判断

用 `t == t[::-1]` 简洁直观。对于大规模数据，可用 DP 预处理：

```python
dp = [[False] * n for _ in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
            dp[i][j] = True
```

### 3. 回溯的位置

`dfs(j + 1)` 而不是 `dfs(i + 1)`，因为当前子串是从 `i` 到 `j`，下一步从 `j+1` 开始。

---

## 扩展思考

### 如果只要求最少分割次数？

就是 [132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/)，用动态规划解决。

### 回文判断的扩展

Manacher 算法可以在 `O(n)` 内找出所有回文子串，但在这里是 overkill。

## 相关题目

- [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)
- [39. 组合总和](https://leetcode.cn/problems/combination-sum/)
- [132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/)
