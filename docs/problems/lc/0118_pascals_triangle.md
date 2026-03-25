---
title: 杨辉三角
platform: LeetCode
difficulty: Easy
id: 118
url: https://leetcode.cn/problems/pascals-triangle/
tags:
  - 数组
  - 动态规划
date_added: 2026-03-25
---

# 118. 杨辉三角

## 题目描述

给定一个非负整数 `numRows`，生成「杨辉三角」的前 `numRows` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

## 示例

**示例 1：**
```
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2：**
```
输入: numRows = 1
输出: [[1]]
```

---

## 解题思路

### 第一步：理解问题本质

杨辉三角的特点：
1. 每行的第一个和最后一个元素为 1
2. 其他元素 = 上一行的前一列 + 上一行的当前列

### 第二步：最优解法 —— 动态规划

**核心洞察**：
- 按行生成，每行根据上一行计算
- 先初始化为1，再计算中间元素

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    杨辉三角 - 动态规划

    核心思想：
    每行的第一个和最后一个元素为1，其他元素 = 上一行的前一列 + 上一行的当前列

    时间复杂度：O(numRows²)
    空间复杂度：O(numRows²)
    """

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        triangle = []

        for i in range(numRows):
            # 创建当前行，初始化为1
            row = [1] * (i + 1)

            # 计算中间元素
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **动态规划（最优）** | **O(numRows²)** | **O(numRows²)** |

---

## 相关题目

- [119. 杨辉三角 II](https://leetcode.cn/problems/pascals-triangle-ii/)
