---
title: 动态规划
category: 算法思想
difficulty_range: [中等, 困难]
last_updated: 2026-03-05
---

# 动态规划

## 知识点概述

动态规划（Dynamic Programming）用于解决具有**重叠子问题**与**最优子结构**的问题。

### 适用条件

动态规划能解决的问题必须满足两个核心条件：
1. **最优子结构**：原问题的最优解可以由子问题的最优解推导出来
2. **无后效性**：一旦确定了子问题的解，后续推导原问题时，不会再改变子问题的解

### 两种实现方式

1. **记忆化搜索**：自上而下的递归实现，配合缓存
2. **递推**：自下而上的迭代实现，配合状态转移方程

## 常见考点

- 状态定义与转移
- 一维/二维 DP
- 空间优化

## 入门 DP：爬楼梯

[70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)

### 方法一：记忆化搜索

```python
from functools import cache

def climbStairs(self, n: int) -> int:
    @cache  # 自动记忆化，Python 3.9+
    def dfs(i: int) -> int:
        if i == 0:
            return 1
        if i < 0:
            return 0
        return dfs(i - 1) + dfs(i - 2)
    return dfs(n)
```

### 方法二：递推

```python
def climbStairs(self, n: int) -> int:
    f = [0] * (n + 1)
    f[0] = f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
```

### 方法三：空间优化

```python
def climbStairs(self, n: int) -> int:
    f0 = f1 = 1
    for i in range(2, n + 1):
        new_f = f0 + f1
        f0, f1 = f1, new_f
    return f1
```

## 网格图 DP

[1594. 矩阵的最大非负积](https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/)

```python
def maxProductPath(self, grid: List[List[int]]) -> int:
    mod = 10**9 + 7
    m, n = len(grid), len(grid[0])

    # 需要同时维护最大和最小值，因为负数×负数=正数
    maxgt = [[0] * n for _ in range(m)]
    minlt = [[0] * n for _ in range(m)]

    maxgt[0][0] = minlt[0][0] = grid[0][0]
    for i in range(1, n):
        maxgt[0][i] = minlt[0][i] = maxgt[0][i - 1] * grid[0][i]
    for i in range(1, m):
        maxgt[i][0] = minlt[i][0] = maxgt[i - 1][0] * grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] >= 0:
                maxgt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
                minlt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
            else:
                maxgt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
                minlt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]

    return maxgt[m - 1][n - 1] % mod if maxgt[m - 1][n - 1] >= 0 else -1
```

## 0-1 背包

每个物品只能选一次（要么选，要么不选）。

[416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

```python
def canPartition(self, nums: List[int]) -> bool:
    @cache
    def dfs(i: int, j: int) -> bool:
        if i < 0:
            return j == 0
        if j < nums[i]:
            return dfs(i - 1, j)  # 只能不选
        return dfs(i - 1, j - nums[i]) or dfs(i - 1, j)  # 选或不选

    s = sum(nums)
    return s % 2 == 0 and dfs(len(nums) - 1, s // 2)
```

## 经典线性 DP：最长公共子序列

[1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

```python
def longestCommonSubsequence(self, s: str, t: str) -> int:
    n, m = len(s), len(t)

    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if s[i] == t[j]:
            return dfs(i - 1, j - 1) + 1
        return max(dfs(i - 1, j), dfs(i, j - 1))

    return dfs(n - 1, m - 1)
```

## DP 解题步骤

1. **确定状态**：定义 `dp[i]` 或 `dp[i][j]` 的含义
2. **确定状态转移方程**：找出状态之间的关系
3. **确定初始状态**：边界条件
4. **确定遍历顺序**：确保计算当前状态时，依赖的状态已经计算过
5. **空间优化**（可选）：滚动数组等技巧
