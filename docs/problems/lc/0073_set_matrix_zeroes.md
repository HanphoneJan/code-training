---
title: 矩阵置零
platform: LeetCode
difficulty: Medium
id: 73
url: https://leetcode.cn/problems/set-matrix-zeroes/
tags:
  - 数组
  - 矩阵
  - 原地算法
date_added: 2026-03-25
---

# 73. 矩阵置零

## 题目描述

给定一个 `m x n` 的矩阵，如果一个元素为 `0`，则将其所在行和列的所有元素都设为 `0`。请使用**原地**算法。

## 示例

**示例 1：**
```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**
```
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

---

## 解题思路

### 第一步：理解问题本质

需要将所有包含 0 的行和列都置为 0。难点在于：**原地算法**，即 O(1) 额外空间。

### 第二步：暴力解法

**思路**：遍历矩阵，记录所有 0 的位置，然后根据记录置零。

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # 记录所有0的位置
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # 置零
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
```

**缺点**：使用了 O(m+n) 额外空间。

### 第三步：最优解法 —— 利用矩阵本身存储信息

**核心洞察**：
- 用第一行和第一列作为标记位
- `matrix[i][0] = 0` 表示第 i 行需要置零
- `matrix[0][j] = 0` 表示第 j 列需要置零
- 用两个变量记录第一行和第一列本身是否有零

**算法步骤**：
1. 检查第一行和第一列是否有零，记录在两个变量中
2. 遍历矩阵（从第二行第二列开始），如果遇到 0，将对应的第一行和第一列位置置 0
3. 根据第一行和第一列的标记，将对应行和列置零
4. 根据之前的记录，处理第一行和第一列

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    矩阵置零 - 原地算法

    核心思想：
    将矩阵中所有0所在的行和列都置为0。
    要求使用 O(1) 额外空间，因此需要利用矩阵本身存储信息。

    策略：
    1. 用第一行和第一列作为标记位，记录该行/列是否需要置零
    2. 先用两个变量记录第一行和第一列本身是否有零
    3. 遍历矩阵（从第二行第二列开始），如果遇到0，将对应的第一行和第一列位置置0
    4. 再次遍历，根据第一行和第一列的标记置零
    5. 最后根据之前的记录处理第一行和第一列

    时间复杂度：O(m * n)
    空间复杂度：O(1)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # 记录第一行和第一列本身是否有零
        first_row_has_zero = 0 in matrix[0]

        # 用第一行和第一列作为标记位
        # matrix[i][0] = 0 表示第 i 行需要置零
        # matrix[0][j] = 0 表示第 j 列需要置零
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 根据标记置零（从后往前遍历，避免影响第一列的标记）
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(m*n) | O(m+n) | 使用额外集合 |
| **原地算法（最优）** | **O(m*n)** | **O(1)** | 利用矩阵本身存储信息 |

---

## 相关题目

- [289. 生命游戏](https://leetcode.cn/problems/game-of-life/)
