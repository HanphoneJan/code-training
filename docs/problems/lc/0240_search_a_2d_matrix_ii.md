---
title: 搜索二维矩阵 II
platform: LeetCode
difficulty: Medium
id: 240
url: https://leetcode.cn/problems/search-a-2d-matrix-ii/
tags:
  - 数组
  - 二分查找
  - 分治
date_added: 2026-04-09
---

# 240. 搜索二维矩阵 II

## 题目描述

编写一个高效的算法来搜索 `m x n` 矩阵 `matrix` 中的一个目标值 `target`。该矩阵具有以下特性：

- 每行的元素从左到右升序排列
- 每列的元素从上到下升序排列

**示例 1：**

```
输入: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 5
输出: true
```

**示例 2：**

```
输入: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 20
输出: false
```

**提示：**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- 每行的所有元素保证互不相同
- 每列的所有元素保证互不相同

---

## 解题思路

### 第一步：理解问题本质

矩阵具有两个方向的单调性：
- 水平方向：从左到右递增
- 垂直方向：从上到下递增

这种"二维有序"的特性意味着我们可以从特殊位置开始搜索，利用单调性排除大量元素。

### 第二步：暴力解法

遍历整个矩阵，逐个比较元素。

```python
def searchMatrix_brute(matrix, target):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
    return False
```

**为什么不够好？**
- 时间复杂度 O(m*n)，没有利用矩阵的有序性
- 对于 300x300 的矩阵，最多需要 90000 次比较

### 第三步：优化解法 - 逐行二分查找

对每一行进行二分查找。

```python
import bisect

def searchMatrix_binary_search(matrix, target):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        idx = bisect.bisect_left(matrix[i], target)
        if idx < n and matrix[i][idx] == target:
            return True
    return False
```

**复杂度分析：**
- 时间复杂度 O(m * log n) - 对 m 行分别二分
- 空间复杂度 O(1)

### 第四步：最优解法 - Z字形搜索

从矩阵的右上角开始搜索，利用矩阵的单调性决定搜索方向。

**为什么选择右上角？**
- 右上角的元素是一行中最大的、一列中最小的
- 从右上角出发，可以明确排除一行或一列

**搜索策略：**
- 当前值 > target：向左移动（减小）
- 当前值 < target：向下移动（增大）
- 当前值 == target：找到目标

---

## 完整代码实现

```python
from typing import List
import bisect


class Solution:
    """
    240. 搜索二维矩阵 II

    核心思路：
    利用矩阵的排序特性：每行从左到右递增，每列从上到下递增。

    解法一：逐行二分查找
    - 对每一行进行二分查找，时间复杂度 O(m * log n)

    解法二：从右上角开始搜索（Z字形搜索）
    - 从矩阵右上角 (0, n-1) 开始
    - 如果当前值 > target，向左移动（列减1）
    - 如果当前值 < target，向下移动（行加1）
    - 如果相等，返回 True

    时间复杂度: O(m + n) - 最多移动 m + n 步
    空间复杂度: O(1) - 只使用常数额外空间
    """

    # 解法一：逐行二分查找，时间复杂度 O(m * log n)
    def searchMatrix_binary_search(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            idx = bisect.bisect_left(matrix[i], target)
            if idx < len(matrix[i]) and matrix[i][idx] == target:
                return True
        return False

    # 解法二：Z字形搜索，时间复杂度 O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始
        x, y = 0, n - 1

        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                # 当前值太大，向左移动（减小）
                y -= 1
            else:
                # 当前值太小，向下移动（增大）
                x += 1

        return False
```

---

## 示例推演

以示例 1 为例，`target = 5`：

```
初始位置: (0, 4) = 15

步骤 1: matrix[0][4] = 15 > 5，向左移动
       位置: (0, 3) = 11

步骤 2: matrix[0][3] = 11 > 5，向左移动
       位置: (0, 2) = 7

步骤 3: matrix[0][2] = 7 > 5，向左移动
       位置: (0, 1) = 4

步骤 4: matrix[0][1] = 4 < 5，向下移动
       位置: (1, 1) = 5

步骤 5: matrix[1][1] = 5 == 5，找到目标！
       返回 True
```

以示例 2 为例，`target = 20`：

```
初始位置: (0, 4) = 15

步骤 1: 15 < 20，向下 -> (1, 4) = 19
步骤 2: 19 < 20，向下 -> (2, 4) = 22
步骤 3: 22 > 20，向左 -> (2, 3) = 16
步骤 4: 16 < 20，向下 -> (3, 3) = 17
步骤 5: 17 < 20，向下 -> (4, 3) = 26
步骤 6: 26 > 20，向左 -> (4, 2) = 23
步骤 7: 23 > 20，向左 -> (4, 1) = 21
步骤 8: 21 > 20，向左 -> (4, 0) = 18
步骤 9: 18 < 20，向下 -> x = 5，超出边界

返回 False
```

**关键观察：**
- 每次比较都能排除一行或一列
- 最多移动 m + n 步

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(m*n) | O(1) | 遍历整个矩阵 |
| 逐行二分 | O(m*log n) | O(1) | 对每行分别二分查找 |
| Z字形搜索 | O(m+n) | O(1) | 从右上角开始，最优解法 |

---

## 易错点总结

### 1. 起始位置的选择

**错误做法：** 从左上角开始，无法确定移动方向。

**正确做法：** 从右上角（或左下角）开始，这两个位置具有"一行最大、一列最小"（或相反）的特性，可以确定移动方向。

### 2. 边界条件

```python
while x < m and y >= 0:  # 注意边界是 < m 和 >= 0
```

### 3. 移动方向的判断

```python
if matrix[x][y] > target:
    y -= 1   # 当前值太大，向左（减小）
else:
    x += 1   # 当前值太小，向下（增大）
```

### 4. 为什么不能从左上角开始？

从左上角开始，右边和下边都更大，无法确定搜索方向。

---

## 扩展思考

### 1. 相关题目

- [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/) - 矩阵整体有序，可以用两次二分
- [378. 有序矩阵中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) - 类似思路

### 2. 变体问题

**如果矩阵每行每列都严格递增，能否做到 O(log(m*n))？**

可以，使用两次二分查找：
1. 先二分找到目标可能所在的行
2. 再在该行内二分查找

但这种方法代码更复杂，实际面试中 Z字形搜索更常用。

### 3. 左下角开始同样有效

从左下角开始：
- 当前值 > target：向上移动（减小）
- 当前值 < target：向右移动（增大）
