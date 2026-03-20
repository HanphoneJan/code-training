---
title: 最长回文子串
platform: LeetCode
difficulty: 中等
id: 5
url: https://leetcode.cn/problems/longest-palindromic-substring/
tags:
  - 字符串
  - 动态规划
  - 双指针
topics:
  - ../../topics/string.md
patterns:
  - ../../patterns/two_pointers.md
date_added: 2026-03-20
date_reviewed: []
---

# 0005. 最长回文子串

## 题目描述

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

**示例 1：**
```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**
```
输入：s = "cbbd"
输出："bb"
```

**约束**：`1 <= s.length <= 1000`，`s` 仅由数字和英文字母组成。

---

## 解题思路

### 第一步：理解问题本质

回文串的核心性质是**轴对称**：以某个字符（奇数长度）或两个相邻字符之间的间隙（偶数长度）为中心，向两侧展开时字符完全对称。

例如：
- `"aba"` → 以中间的 `b` 为中心，奇数长度回文
- `"abba"` → 以 `bb` 之间的间隙为中心，偶数长度回文

这个性质直接启发了"中心扩展"的思路。

### 第二步：暴力解法

枚举所有子串，逐一判断是否是回文串，记录最长的那个。

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    result = ""
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            # 判断 sub 是否是回文
            if sub == sub[::-1] and len(sub) > len(result):
                result = sub
    return result
```

- 时间复杂度：O(n³)——枚举子串 O(n²)，判断回文 O(n)
- 空间复杂度：O(n)——存储候选子串

**问题**：对每个子串独立判断，完全没有利用回文串"从中心向外扩展"的对称性质，大量重复判断。

### 第三步：优化解法——动态规划

定义 `dp[i][j]` 表示 `s[i..j]` 是否是回文串。状态转移：

```
dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
```

基础情况：
- 单个字符 `dp[i][i] = True`
- 相邻相同字符 `dp[i][i+1] = (s[i] == s[i+1])`

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # 长度为 1
    for i in range(n):
        dp[i][i] = True

    # 长度为 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2

    # 长度从 3 到 n
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length

    return s[start:start + max_len]
```

- 时间复杂度：O(n²)
- 空间复杂度：O(n²)——需要一个 n×n 的 dp 表

**还能优化吗？** 同样是 O(n²) 时间，但空间可以降到 O(1)。

### 第四步：最优解法——中心扩展

**核心思想**：遍历每一个可能的"中心"，从中心向两侧扩展，直到两侧字符不相等为止，记录扩展出的最长回文长度。

对于长度为 `n` 的字符串，共有 `2n - 1` 个中心：
- `n` 个字符本身（奇数长度回文的中心）
- `n - 1` 个相邻字符之间的间隙（偶数长度回文的中心）

用 `expandAroundCenter(left, right)` 函数从 `[left, right]` 出发向外扩展：
- 初始 `(left, right) = (i, i)` 处理奇数长度
- 初始 `(left, right) = (i, i+1)` 处理偶数长度

扩展时只要 `s[left] == s[right]` 就继续向外，函数返回最终回文范围的左右端点。

---

## 完整代码实现

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            # 向两侧扩展，直到越界或字符不匹配
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 循环结束时 left 和 right 各越出一位，回退一位得到实际范围
            return left + 1, right - 1

        start, end = 0, 0

        for i in range(len(s)):
            l1, r1 = expandAroundCenter(i, i)      # 奇数长度：以 s[i] 为中心
            l2, r2 = expandAroundCenter(i, i + 1)  # 偶数长度：以 s[i] 和 s[i+1] 之间为中心

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
```

---

## 示例推演

**输入**：`s = "cbbd"`

逐一以每个字符为中心进行扩展，当前记录的最长回文初始为 `start=0, end=0`（即 `"c"`）。

**i = 0，中心为 `s[0] = 'c'`**：
- 奇数扩展：`expandAroundCenter(0, 0)`
  - 初始：`left=0, right=0`，`s[0]='c'` 匹配
  - 向外：`left=-1`，越界，停止
  - 返回：`(0+1, 0-1) = (0, 0)`，即 `"c"`，长度 1
- 偶数扩展：`expandAroundCenter(0, 1)`
  - 初始：`left=0, right=1`，`s[0]='c'` vs `s[1]='b'`，不匹配，立即停止
  - 返回：`(0+1, 1-1) = (1, 0)`，长度 = 0-1 = -1（表示空串）
- 当前最长：`"c"`，`start=0, end=0`

**i = 1，中心为 `s[1] = 'b'`**：
- 奇数扩展：`expandAroundCenter(1, 1)`
  - `left=1, right=1`，`s[1]='b'` 匹配
  - 向外：`left=0, right=2`，`s[0]='c'` vs `s[2]='b'`，不匹配，停止
  - 返回：`(0+1, 2-1) = (1, 1)`，即 `"b"`，长度 1
- 偶数扩展：`expandAroundCenter(1, 2)`
  - `left=1, right=2`，`s[1]='b'` vs `s[2]='b'`，匹配
  - 向外：`left=0, right=3`，`s[0]='c'` vs `s[3]='d'`，不匹配，停止
  - 返回：`(0+1, 3-1) = (1, 2)`，即 `"bb"`，长度 2
- 长度 2 > 当前最长 1，更新：`start=1, end=2`

**i = 2，中心为 `s[2] = 'b'`**：
- 奇数扩展：`expandAroundCenter(2, 2)`
  - `left=2, right=2`，`s[2]='b'` 匹配
  - 向外：`left=1, right=3`，`s[1]='b'` vs `s[3]='d'`，不匹配，停止
  - 返回：`(1+1, 3-1) = (2, 2)`，即 `"b"`，长度 1
- 偶数扩展：`expandAroundCenter(2, 3)`
  - `left=2, right=3`，`s[2]='b'` vs `s[3]='d'`，不匹配，停止
  - 返回：`(3, 2)`，长度 -1（空串）
- 无更新，当前最长仍为 `"bb"`

**i = 3，中心为 `s[3] = 'd'`**：
- 奇数扩展：`expandAroundCenter(3, 3)`
  - `left=3, right=3`，`s[3]='d'` 匹配
  - 向外：`left=2, right=4`，`right=4` 越界，停止
  - 返回：`(3, 3)`，即 `"d"`，长度 1
- 偶数扩展：`expandAroundCenter(3, 4)`
  - `right=4` 初始就越界，立即停止
  - 返回：`(4, 3)`，长度 -1（空串）
- 无更新，当前最长仍为 `"bb"`

**最终结果**：`s[1:3] = "bb"`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力枚举 | O(n³) | O(n) | 枚举所有子串并逐一验证 |
| 动态规划 | O(n²) | O(n²) | 需要 n×n 的 dp 表 |
| 中心扩展 | O(n²) | O(1) | **最优解**，时间同 dp 但空间降至常数 |

---

## 易错点总结

- **扩展函数的返回值**：循环结束时 `left` 和 `right` 各向外越出了一步，所以实际回文范围是 `[left+1, right-1]`，不能直接返回 `left` 和 `right`。
- **偶数中心的初始化**：偶数长度回文用 `expandAroundCenter(i, i+1)` 启动，当 `i = n-1` 时 `i+1 = n` 已越界，因此循环条件 `right < len(s)` 会立即终止，得到空串，无需特殊处理。
- **长度比较方式**：用 `r - l > end - start` 而非记录显式长度变量，减少变量数量；但要注意当返回空串时 `r < l`，差值为负，不会触发更新，逻辑自洽。
- **初始值设置**：`start=0, end=0` 保证至少返回第一个字符，避免空字符串的边界问题。

---

## 扩展思考

### 1. Manacher 算法

中心扩展最坏情况仍是 O(n²)（如全为相同字符 `"aaaa...a"`）。Manacher 算法通过记录已扩展过的回文信息，将时间复杂度降至 O(n)，是回文子串问题的终极解法。

### 2. 回文问题的通用思路

- **判断回文**：双指针从两端向中间收缩
- **最长回文子串**：中心扩展（本题）
- **最长回文子序列**：动态规划（LeetCode 516）

### 3. 相关题目

- [647. 回文子串](https://leetcode.cn/problems/palindromic-substrings/)——统计所有回文子串数量，中心扩展同理
- [516. 最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)——子序列不要求连续，需要 dp
- [214. 最短回文串](https://leetcode.cn/problems/shortest-palindrome/)——在字符串前面添加最少字符使其成为回文
