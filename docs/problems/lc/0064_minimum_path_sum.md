---
title: 最小路径和
platform: LeetCode
difficulty: Medium
id: 64
url: https://leetcode.cn/problems/minimum-path-sum/
tags:
  - 数组
  - 动态规划
  - 矩阵
date_added: 2026-03-25
---

# 64. 最小路径和

## 题目描述

给定一个包含非负整数的 `m x n` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明**：每次只能向下或者向右移动一步。

## 示例

**示例 1：**
```
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
```

**示例 2：**
```
输入：grid = [[1,2,3],[4,5,6]]
输出：12
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**动态规划**问题。由于只能向右或向下移动，到达每个格子的路径只能从上方或左方过来。

### 第二步：暴力解法

**思路**：枚举所有从左上角到右下角的路径，计算路径和，取最小值。

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i >= m or j >= n:
                return float('inf')
            return grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)
```

**缺点**：时间复杂度指数级，有大量重复计算。

### 第三步：最优解法 —— 动态规划

**核心洞察**：
- 到达 `(i,j)` 的最小路径和 = min(从上方来的最小和, 从左方来的最小和) + 当前格子的值
- 这符合动态规划的最优子结构

**状态定义**：
- `dp[i][j]` = 从 `(0,0)` 到达 `(i,j)` 的最小路径和

**状态转移方程**：
```
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

**边界条件**：
- `dp[0][0] = grid[0][0]`
- 第一行：只能从左边来，`dp[0][j] = dp[0][j-1] + grid[0][j]`
- 第一列：只能从上面来，`dp[i][0] = dp[i-1][0] + grid[i][0]`

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    最小路径和 - 动态规划

    核心思想：
    从左上角到右下角，每次只能向右或向下移动，求路径和最小值。

    状态定义：
    dp[i][j] = 从 (0,0) 到达 (i,j) 的最小路径和

    状态转移方程：
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    （只能从上方或左方到达当前位置，选择路径和较小的那个）

    边界条件：
    - dp[0][0] = grid[0][0]
    - 第一行：只能从左边来，dp[0][j] = dp[0][j-1] + grid[0][j]
    - 第一列：只能从上面来，dp[i][0] = dp[i-1][0] + grid[i][0]

    时间复杂度：O(m * n)
    空间复杂度：O(m * n)，可以优化到 O(n)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])

        # dp[i][j] = 到达 (i,j) 的最小路径和
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # 初始化第一列：只能从上方来
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一行：只能从左边来
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 填充 DP 表
        for i in range(1, rows):
            for j in range(1, columns):
                # 从上方或左方选择较小的路径和，加上当前格子的值
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]
```

---

## 示例推演

以 `grid = [[1,3,1],[1,5,1],[4,2,1]]` 为例：

**初始化**：
```
dp[0][0] = 1
```

**第一列**（只能从上方来）：
```
dp[1][0] = dp[0][0] + 1 = 1 + 1 = 2
dp[2][0] = dp[1][0] + 4 = 2 + 4 = 6
```

**第一行**（只能从左边来）：
```
dp[0][1] = dp[0][0] + 3 = 1 + 3 = 4
dp[0][2] = dp[0][1] + 1 = 4 + 1 = 5
```

**填充其余部分**：
```
dp[1][1] = min(dp[0][1], dp[1][0]) + 5 = min(4, 2) + 5 = 7
dp[1][2] = min(dp[0][2], dp[1][1]) + 1 = min(5, 7) + 1 = 6
dp[2][1] = min(dp[1][1], dp[2][0]) + 2 = min(7, 6) + 2 = 8
dp[2][2] = min(dp[1][2], dp[2][1]) + 1 = min(6, 8) + 1 = 7
```

**结果**：`dp[2][2] = 7`

最优路径：`1 → 1 → 5 → 1 → 1` 或 `1 → 3 → 1 → 1 → 1`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 DFS | O(2^(m+n)) | O(m+n) | 指数级 |
| 记忆化搜索 | O(m*n) | O(m*n) | 自顶向下 |
| **动态规划（最优）** | **O(m*n)** | **O(m*n)** | 可优化至 O(n) |

---

## 易错点总结

### 1. 边界条件处理

第一行和第一列需要单独初始化，因为它们只有一个方向可以到达。

### 2. 空间优化

可以只使用一维数组，因为计算 `dp[i][j]` 只需要上一行和当前行的值。

```python
def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]

    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

    return dp[-1]
```

---

## 相关题目

- [62. 不同路径](https://leetcode.cn/problems/unique-paths/)
- [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/)
- [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/)
