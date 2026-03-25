---
title: 搜索二维矩阵
platform: LeetCode
difficulty: Medium
id: 74
url: https://leetcode.cn/problems/search-a-2d-matrix/
tags:
  - 数组
  - 二分查找
  - 矩阵
date_added: 2026-03-25
---

# 74. 搜索二维矩阵

## 题目描述

给你一个满足下述两条属性的 `m x n` 整数矩阵：

1. 每行中的整数从左到右按非严格递增顺序排列。
2. 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target`，如果 `target` 在矩阵中，返回 `true`；否则，返回 `false`。

## 示例

**示例 1：**
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例 2：**
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```

---

## 解题思路

### 第一步：理解问题本质

矩阵的特性保证了它可以被视为一个有序的一维数组。

### 第二步：最优解法 —— 虚拟索引二分查找

**核心洞察**：
- 将二维矩阵视为一维有序数组
- 虚拟索引 `idx` 转换为二维坐标：
  - 行号：`idx // n`
  - 列号：`idx % n`

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    搜索二维矩阵 - 二分查找

    核心思想：
    矩阵每行从左到右递增，每行第一个数大于上一行最后一个数。
    可以将二维矩阵视为一个有序的一维数组进行二分查找。

    虚拟索引转换：
    对于虚拟索引 idx，对应的矩阵位置为：
    - 行号：idx // n
    - 列号：idx % n

    时间复杂度：O(log(m*n)) = O(log m + log n)
    空间复杂度：O(1)
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 暴力 | O(m*n) | O(1) |
| **二分查找（最优）** | **O(log(m*n))** | **O(1)** |

---

## 相关题目

- [240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)
