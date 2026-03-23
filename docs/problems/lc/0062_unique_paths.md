---
title: 不同路径
platform: LeetCode
difficulty: 中等
id: 62
url: https://leetcode.cn/problems/unique-paths/
tags:
  - 数学
  - 动态规划
  - 组合
topics:
  - ../../topics/math.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../topics/combinatorics.md
date_added: 2026-03-23
date_reviewed: []
---

# 0062. 不同路径

## 题目描述

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 "Start" ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 "Finish" ）。

问总共有多少条不同的路径？

## 示例

**示例 1：**
```
输入：m = 3, n = 7
输出：28
```

**示例 2：**
```
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```

**示例 3：**
```
输入：m = 7, n = 3
输出：28
```

---

## 解题思路

### 第一步：理解问题本质

**约束条件**：
- 只能向下或向右移动
- 需要走 `(m-1)` 步向下 + `(n-1)` 步向右 = `m+n-2` 步
- 问题转化为：在这 `m+n-2` 步中选择哪些步向右（或向下）

**组合数学视角**：
从 `m+n-2` 个位置中选择 `n-1` 个位置放"右"（或选择 `m-1` 个位置放"下"）。

答案 = C(m+n-2, n-1) = (m+n-2)! / ((n-1)! × (m-1)!)

### 第二步：动态规划思路

**状态定义**：
`dp[i][j]` = 从起点到达 `(i,j)` 的不同路径数

**状态转移**：
```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```
因为只能从上方或左方到达当前位置。

**边界条件**：
- `dp[0][j] = 1`（第一行只有一条路径：一直向右）
- `dp[i][0] = 1`（第一列只有一条路径：一直向下）

### 第三步：空间优化

`dp[i][j]` 只依赖上一行和当前行的左边，可以用一维数组滚动更新。

---

## 完整代码实现

```python
from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        不同路径 - 组合数学解法（最优）

        核心思想：从 m+n-2 步中选择 n-1 步向右
        """
        # 选择 n-1 个位置放"右"，其余放"下"
        return comb(m + n - 2, n - 1)

    def uniquePathsByDP(self, m: int, n: int) -> int:
        """
        动态规划解法 - 空间优化版
        """
        # dp[j] 表示当前行第 j 列的路径数
        dp = [1] * n  # 初始化第一行，所有位置的路径数都是 1

        for i in range(1, m):  # 从第二行开始遍历
            for j in range(1, n):  # 从第二列开始
                # dp[j] 存储的是上一行的值（dp[i-1][j]）
                # dp[j-1] 存储的是当前行的值（dp[i][j-1]）
                dp[j] += dp[j - 1]

        return dp[n - 1]

    def uniquePathsBy2D(self, m: int, n: int) -> int:
        """
        标准二维DP写法，更容易理解
        """
        # dp[i][j] = 到达 (i,j) 的路径数
        dp = [[0] * n for _ in range(m)]

        # 初始化边界
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 填充DP表
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
```

---

## 示例推演

**示例**：`m = 3, n = 7`

**组合数学计算**：
```
C(3+7-2, 7-1) = C(8, 6) = C(8, 2) = 8! / (2! × 6!) = 28
```

**DP表推演**：

初始化：
```
1  1  1  1  1  1  1
1  0  0  0  0  0  0
1  0  0  0  0  0  0
```

填充后：
```
1  1  1  1  1  1  1
1  2  3  4  5  6  7
1  3  6  10 15 21 28
```

**结果**：`dp[2][6] = 28`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 组合数学 | O(min(m,n)) | O(1) | **最优**，直接计算 |
| 一维DP | O(m×n) | O(n) | 空间优化版 |
| 二维DP | O(m×n) | O(m×n) | 易于理解 |

---

## 易错点总结

### 1. 组合数参数

```python
comb(m + n - 2, n - 1)  # 不是 comb(m+n, n)
```

只需要走 `m+n-2` 步（不是 `m+n` 步，因为起点不算）。

### 2. DP边界初始化

```python
for i in range(m):
    dp[i][0] = 1  # 第一列
for j in range(n):
    dp[0][j] = 1  # 第一行
```

边界都是 1，因为只能沿一个方向走。

### 3. 一维DP的更新顺序

```python
for j in range(1, n):  # 从左到右
    dp[j] += dp[j-1]
```

必须是正序，因为 `dp[j]` 依赖 `dp[j-1]`（当前行已经更新的值）。

### 4. 大数问题

Python 的整数可以任意大，但其他语言需要注意溢出问题。答案可能非常大（如 `m=100, n=100` 时约为 `9e58`）。

---

## 扩展思考

### 1. 如果有障碍物？

这就是 [63. 不同路径 II]，需要在DP转移时检查障碍物：
```python
if grid[i][j] == 0:  # 不是障碍物
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
else:
    dp[i][j] = 0
```

### 2. 如果机器人可以走 8 个方向？

需要 BFS 或 DFS 来统计路径数，不再是简单的DP。

### 3. 如果要求输出所有路径？

需要用 DFS 回溯，记录当前路径，到达终点时保存。

---

## 相关题目

- [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/)
- [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/)
- [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/)
- [931. 下降路径最小和](https://leetcode.cn/problems/minimum-falling-path-sum/)
