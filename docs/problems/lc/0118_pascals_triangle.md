---
title: 杨辉三角
platform: LeetCode
difficulty: 简单
id: 118
url: https://leetcode.cn/problems/pascals-triangle/
tags:
  - 数组
  - 动态规划
topics:
  - ../../topics/array.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../patterns/dynamic_programming.md
date_added: 2026-04-03
date_reviewed: []
---

# 0118. 杨辉三角

## 题目描述

给定一个非负整数 `numRows`，生成「杨辉三角」的前 `numRows` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

## 示例

**示例 1：**
```
输入：numRows = 5
输出：[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2：**
```
输入：numRows = 1
输出：[[1]]
```

---

## 解题思路

### 第一步：理解杨辉三角的规律

杨辉三角有两个明显的特点：
1. 每行的第一个和最后一个元素都是 `1`
2. 其他位置的元素 = 上一行的前一列 + 上一行的当前列

用公式表示就是：`triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]`

### 第二步：暴力解法

直接按定义，先初始化一个全 0 的三角形，然后根据上一行逐个计算每个元素。

```python
def generate(numRows):
    if numRows <= 0:
        return []
    triangle = []
    for i in range(numRows):
        row = [0] * (i + 1)
        row[0] = row[-1] = 1
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```

这其实已经是比较优的解法了，时间复杂度 `O(numRows²)`，空间复杂度 `O(numRows²)`（用于存储结果）。

### 第三步：优化写法

利用「每行初始化时所有元素都是 1」这个特性，直接创建全 1 数组，只修改中间元素。

```python
def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```

### 第四步：最优解法

这道题的最优解法就是动态规划，上面的写法已经是最佳时间复杂度了，因为结果本身就有 `numRows²` 个元素，任何算法都必须至少生成这么多输出。

可以用列表推导式写得更加简洁：

```python
c = [[1] * (i + 1) for i in range(numRows)]
for i in range(2, numRows):
    for j in range(1, i):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
```

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    118. 杨辉三角 - 动态规划

    核心思想：
    杨辉三角的每个数字都等于它上方两数之和。
    1. 每行的第一个和最后一个元素为 1
    2. 其他元素 = 上一行的前一列 + 上一行的当前列

    时间复杂度：O(numRows²)
    空间复杂度：O(numRows²)，存储结果
    """

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        triangle = []

        for i in range(numRows):
            # 创建当前行，初始化为1（首尾元素保持为1）
            row = [1] * (i + 1)

            # 计算中间元素
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle
```

---

## 示例推演

以 `numRows = 4` 为例：

**i = 0**：创建 `[1]`，无中间元素，triangle = `[[1]]`

**i = 1**：创建 `[1, 1]`，无中间元素，triangle = `[[1], [1, 1]]`

**i = 2**：创建 `[1, 1, 1]`
- j = 1：`row[1] = triangle[0][0] + triangle[0][1] = 1 + 0`？不对。

实际上 `triangle[0]` 只有 `[1]`，没有 `triangle[0][1]`。但在代码中，当 `i = 2` 时 `j` 的范围是 `range(1, 2)`，只有 `j = 1`：
- `row[1] = triangle[1][0] + triangle[1][1] = 1 + 1 = 2`

triangle = `[[1], [1, 1], [1, 2, 1]]`

**i = 3**：创建 `[1, 1, 1, 1]`
- j = 1：`row[1] = triangle[2][0] + triangle[2][1] = 1 + 2 = 3`
- j = 2：`row[2] = triangle[2][1] + triangle[2][2] = 2 + 1 = 3`

最终结果：`[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(numRows²) | O(numRows²) | 结果本身就需要这么多空间 |
| 最优 | O(numRows²) | O(numRows²) | 已经是理论最优 |

---

## 易错点总结

### 1. 越界问题

j 的循环范围必须是 `range(1, i)`，不能是 `range(1, i+1)`，否则会访问 `triangle[i-1][i]` 导致越界。

### 2. 特殊情况

`numRows <= 0` 时应该返回空列表。

### 3. 初始化技巧

用 `[1] * (i + 1)` 初始化比先创建全 0 再设首尾更加简洁。

---

## 扩展思考

### 如果只需要生成第 n 行怎么办？

可以只用 `O(n)` 额外空间，滚动更新一维数组。

```python
def getRow(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row
```

## 相关题目

- [119. 杨辉三角 II](https://leetcode.cn/problems/pascals-triangle-ii/)
