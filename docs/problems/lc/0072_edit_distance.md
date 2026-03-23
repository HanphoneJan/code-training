---
title: 编辑距离
platform: LeetCode
difficulty: 中等
id: 72
url: https://leetcode.cn/problems/edit-distance/
tags:
  - 字符串
  - 动态规划
topics:
  - ../../topics/string.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../patterns/edit_distance.md
  - ../../patterns/space_optimization.md
date_added: 2026-03-23
date_reviewed: []
---

# 0072. 编辑距离

## 题目描述

给你两个单词 `word1` 和 `word2`，请返回将 `word1` 转换成 `word2` 所使用的最少操作数。

你可以对一个单词进行如下三种操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符

## 示例

**示例 1：**
```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**
```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

---

## 解题思路

### 第一步：理解问题本质

**编辑距离**（Edit Distance / Levenshtein Distance）：两个字符串之间，由一个转成另一个所需的最少编辑操作次数。

**核心思想**：比较两个字符串的每个位置，决定需要哪种操作。

**示例推演**："horse" -> "ros"
- 对齐两个字符串：
  ```
  h o r s e
  r o s
  ```
- 发现第1个字符不同，第2个相同，后面也错开了

### 第二步：递归思路（暴力解法）

定义 `dfs(i, j)` = `word1[0..i]` 转换成 `word2[0..j]` 的最小编辑距离。

**递归终止条件**：
- `i < 0`：`word1` 已用完，需要插入 `j+1` 个字符
- `j < 0`：`word2` 已用完，需要删除 `i+1` 个字符

**递归情况**：
- 如果 `word1[i] == word2[j]`：不用操作，`dfs(i, j) = dfs(i-1, j-1)`
- 否则，取三种操作的最小值：
  - **删除**：`dfs(i-1, j) + 1`（删除 `word1[i]`）
  - **插入**：`dfs(i, j-1) + 1`（在 `word1[i]` 后插入 `word2[j]`）
  - **替换**：`dfs(i-1, j-1) + 1`（将 `word1[i]` 替换为 `word2[j]`）

**问题**：有大量重复计算，时间复杂度 O(3ⁿ)。

### 第三步：记忆化搜索

用 `@cache` 装饰器缓存递归结果，避免重复计算。

```python
@cache
def dfs(i: int, j: int) -> int:
    if i < 0: return j + 1
    if j < 0: return i + 1
    if s[i] == t[j]:
        return dfs(i - 1, j - 1)
    return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
```

### 第四步：动态规划

将递归改为递推，定义 `dp[i][j]`：
- `word1` 的前 `i` 个字符（`word1[0..i-1]`）
- 转换成 `word2` 的前 `j` 个字符（`word2[0..j-1]`）
- 所需的最小编辑距离

**为什么下标要+1？**
预留 `dp[0][j]` 和 `dp[i][0]` 处理空字符串：
- `dp[0][j] = j`：空串变成 `j` 个字符，需要插入 `j` 次
- `dp[i][0] = i`：`i` 个字符变成空串，需要删除 `i` 次

### 第五步：空间优化

**观察**：`dp[i][j]` 只依赖于上一行和当前行的左边。
- `dp[i-1][j]`：上一行
- `dp[i][j-1]`：当前行左边
- `dp[i-1][j-1]`：上一行左边（对角线）

**滚动数组**：只需保存两行，空间复杂度 O(m)。

**一维数组**：用一个数组 + 一个变量保存对角线，空间复杂度 O(m)。

---

## 完整代码实现

```python
from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        编辑距离 - 动态规划（二维数组版）

        dp[i][j] = word1[:i] 转换成 word2[:j] 的最小编辑距离
        """
        n, m = len(word1), len(word2)

        # dp[i][j] 表示 word1[:i] 转换为 word2[:j] 的最小编辑距离
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化边界
        dp[0] = list(range(m + 1))  # dp[0][j] = j
        for i in range(1, n + 1):
            dp[i][0] = i  # dp[i][0] = i

        # 填充DP表
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不用操作
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],     # 删除
                        dp[i][j - 1],     # 插入
                        dp[i - 1][j - 1]  # 替换
                    ) + 1

        return dp[n][m]

    def minDistanceOneArray(self, word1: str, word2: str) -> int:
        """
        编辑距离 - 空间优化（一维数组版）
        """
        m = len(word2)
        f = list(range(m + 1))

        for x in word1:
            pre = f[0]  # 保存对角线值
            f[0] += 1

            for j, y in enumerate(word2):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp

        return f[m]
```

---

## 示例推演

**示例**：`word1 = "horse"`, `word2 = "ros"`

**DP表**（部分）：

|  |  | r | o | s |
|--|--|---|---|---|
|  | 0 | 1 | 2 | 3 |
| h | 1 | 1 | 2 | 3 |
| o | 2 | 2 | 1 | 2 |
| r | 3 | 2 | 2 | 2 |
| s | 4 | 3 | 3 | 2 |
| e | 5 | 4 | 4 | 3 |

**关键计算**：
- `dp[1][1]`：h vs r，不同 → min(1,1,0)+1 = **1**（替换）
- `dp[2][2]`：o vs o，相同 → `dp[1][1]` = **1**
- `dp[5][3]`：e vs s，不同 → min(3,4,2)+1 = **3**

**结果**：`dp[5][3] = 3`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力递归 | O(3ⁿ) | O(n+m) | 有大量重复计算 |
| 记忆化搜索 | O(n×m) | O(n×m) | 递归栈空间 |
| 二维DP | O(n×m) | O(n×m) | 标准解法 |
| 滚动数组 | O(n×m) | O(m) | 空间优化 |
| 一维数组 | O(n×m) | O(m) | **最优空间** |

---

## 易错点总结

### 1. 下标对应关系

```python
# dp[i][j] 对应 word1[i-1] 和 word2[j-1]
if word1[i - 1] == word2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1]
```
注意 dp 数组和字符串下标的偏移。

### 2. 边界初始化

```python
dp[0] = list(range(m + 1))  # dp[0][j] = j
for i in range(1, n + 1):
    dp[i][0] = i  # dp[i][0] = i
```
不要漏了 `dp[i][0]` 的初始化。

### 3. 空间优化的对角线保存

```python
pre = f[0]  # 先保存
f[0] += 1   # 再更新
for j, y in enumerate(word2):
    tmp = f[j + 1]  # 保存当前值
    # 计算 f[j+1]
    pre = tmp  # 更新对角线供下一轮使用
```

### 4. 三种操作的理解

| 操作 | dp转移 | 实际含义 |
|------|--------|----------|
| 删除 | `dp[i-1][j]` | 删除word1[i-1] |
| 插入 | `dp[i][j-1]` | 在word1[i-1]后插入word2[j-1] |
| 替换 | `dp[i-1][j-1]` | 将word1[i-1]替换为word2[j-1] |

---

## 扩展思考

### 1. 如果操作代价不同？

例如：插入删除代价为1，替换代价为2。
```python
dp[i][j] = min(
    dp[i-1][j] + 1,      # 删除
    dp[i][j-1] + 1,      # 插入
    dp[i-1][j-1] + 2     # 替换代价为2
)
```

### 2. 如何输出具体的编辑操作？

需要在DP过程中记录"来源"，回溯得到操作序列。

### 3. 最长公共子序列（LCS）与编辑距离的关系

```
编辑距离 = len(word1) + len(word2) - 2 × LCS长度
```
当只允许插入和删除时成立。

---

## 应用场景

1. **拼写检查**：计算用户输入与词典单词的编辑距离
2. **DNA序列比对**：生物信息学中计算基因相似度
3. **版本控制**：diff 算法计算文件差异
4. **语音识别**：评价识别结果与标准文本的差异

---

## 相关题目

- [583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)
- [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)
- [161. 相隔为 1 的编辑距离](https://leetcode.cn/problems/one-edit-distance/)
