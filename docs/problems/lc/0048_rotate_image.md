---
title: 旋转图像
platform: LeetCode
difficulty: Medium
id: 48
url: https://leetcode.cn/problems/rotate-image/
tags:
  - 数组
  - 矩阵
  - 数学
date_added: 2026-03-25
---

# 48. 旋转图像

## 题目描述

给定一个 n × n 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在**原地**旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

## 示例

**示例 1：**
```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**
```
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

---

## 解题思路

### 第一步：理解问题本质

顺时针旋转 90 度的坐标变换：
- 原位置 `(i, j)` → 新位置 `(j, n-1-i)`

观察这个变换，可以发现它可以通过两个基本操作的组合实现：
1. **转置**：`(i, j)` → `(j, i)`
2. **行翻转**：`(j, i)` → `(j, n-1-i)`

### 第二步：原地旋转法

**思路**：一圈一圈地旋转，从外到内。

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top < bottom and left < right:
            for i in range(right - left):
                # 保存上边元素
                tmp = matrix[top][left + i]
                # 左边 -> 上边
                matrix[top][left + i] = matrix[bottom - i][left]
                # 下边 -> 左边
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # 右边 -> 下边
                matrix[bottom][right - i] = matrix[top + i][right]
                # 上边 -> 右边
                matrix[top + i][right] = tmp

            top += 1
            bottom -= 1
            left += 1
            right -= 1
```

**优点**：原地修改，空间复杂度 O(1)
**缺点**：代码较复杂，容易出错

### 第三步：最优解法 —— 转置 + 行翻转

**核心洞察**：
- 转置：行列互换
- 行翻转：每行逆序
- 这两个操作的组合等价于顺时针旋转 90 度

**算法步骤**：
1. 转置矩阵：`matrix[i][j]` 和 `matrix[j][i]` 交换
2. 每行翻转：反转每一行

**为什么正确**：
```
原始：          转置后：        行翻转后（结果）：
1 2 3           1 4 7           7 4 1
4 5 6     ->    2 5 8     ->    8 5 2
7 8 9           3 6 9           9 6 3
```

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    旋转图像 - 转置 + 行翻转

    核心思想：
    顺时针旋转 90 度 = 转置 + 行翻转

    坐标变换：
    (i, j) → (j, i) 【转置】→ (j, n-1-i) 【行翻转】

    算法步骤：
    1. 转置矩阵：遍历对角线上方元素，与对称位置交换
    2. 行翻转：反转每一行

    时间复杂度：O(n²)，需要访问每个元素两次
    空间复杂度：O(1)，原地修改
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 第一步：转置矩阵
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：每行翻转
        for i in range(n):
            matrix[i].reverse()
```

---

## 示例推演

以 `matrix = [[1,2,3],[4,5,6],[7,8,9]]` 为例：

**初始状态**：
```
1 2 3
4 5 6
7 8 9
```

**第一步：转置**
```
1 4 7
2 5 8
3 6 9
```

**第二步：行翻转**
```
7 4 1
8 5 2
9 6 3
```

**结果**：顺时针旋转 90 度成功

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 原地旋转 | O(n²) | O(1) | 代码复杂 |
| **转置+翻转（最优）** | **O(n²)** | **O(1)** | 代码简洁 |

---

## 易错点总结

### 1. 转置时的遍历范围

```python
for j in range(i + 1, n):  # 正确，只遍历对角线上方
for j in range(n):         # 错误，会交换两次，相当于没交换
```

### 2. 逆时针旋转 90 度？

转置 + 列翻转（或行翻转 + 转置）

### 3. 旋转 180 度？

行翻转 + 列翻转（或转置两次）

---

## 扩展思考

### 1. 如果要求逆时针旋转 90 度？

```python
# 方法1：转置 + 列翻转
for j in range(n // 2):
    for i in range(n):
        matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# 方法2：行翻转 + 转置
```

### 2. 顺时针旋转 90 度的坐标变换公式？
```
new_i = j
new_j = n - 1 - i
```

---

## 相关题目

- [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)
- [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)
