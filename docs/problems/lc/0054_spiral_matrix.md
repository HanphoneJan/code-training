---
title: 螺旋矩阵
platform: LeetCode
difficulty: 中等
id: 54
url: https://leetcode.cn/problems/spiral-matrix/
tags:
  - 数组
  - 矩阵
  - 模拟
topics:
  - ../../topics/array.md
  - ../../topics/matrix.md
patterns:
  - ../../patterns/matrix_traversal.md
date_added: 2026-03-23
date_reviewed: []
---

# 0054. 螺旋矩阵

## 题目描述

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

## 示例

**示例 1：**
```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**
```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## 解题思路

### 第一步：理解问题本质

**顺时针螺旋顺序**：
1. 从左到右遍历上边
2. 从上到下遍历右边
3. 从右到左遍历下边
4. 从下到上遍历左边
5. 重复 1-4，直到遍历完所有元素

**关键问题**：
- 如何表示方向？
- 如何判断是否需要转向？
- 如何标记已访问的元素？

### 第二步：方向数组法（模拟法）

**方向定义**（顺时针）：
```
右: (0, 1)   -> 列增加
下: (1, 0)   -> 行增加
左: (0, -1)  -> 列减少
上: (-1, 0)  -> 行减少
```

**转向条件**：
1. 超出矩阵边界
2. 遇到已访问的元素

**实现方式**：
- 用 `visited` 数组标记已访问
- 用 `directions` 数组表示四个方向
- 用 `direction_idx` 表示当前方向索引

### 第三步：边界收缩法（优化）

不需要 `visited` 数组，用四个变量记录边界：
- `top, bottom`：上下边界
- `left, right`：左右边界

每遍历完一条边，收缩对应的边界。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        螺旋矩阵 - 边界收缩法（推荐）

        核心思想：用四个边界变量，遍历完一条边就收缩边界
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        ans = []

        # 定义四个边界
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # 从左到右遍历上边
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1  # 上边界下移

            # 从上到下遍历右边
            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1  # 右边界左移

            # 从右到左遍历下边（需要检查是否还有行）
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1  # 下边界上移

            # 从下到上遍历左边（需要检查是否还有列）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1  # 左边界右移

        return ans

    def spiralOrderSimulate(self, matrix: List[List[int]]) -> List[int]:
        """
        方向数组模拟法
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols

        # visited 数组标记已访问的位置
        visited = [[False] * cols for _ in range(rows)]

        # 四个方向：右、下、左、上（顺时针）
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0

        ans = []
        row, col = 0, 0

        for _ in range(total):
            ans.append(matrix[row][col])
            visited[row][col] = True

            # 计算下一个位置
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]

            # 检查是否需要转向
            if not (0 <= next_row < rows and
                    0 <= next_col < cols and
                    not visited[next_row][next_col]):
                direction_idx = (direction_idx + 1) % 4
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]

            row, col = next_row, next_col

        return ans
```

---

## 示例推演

**示例**：`matrix = [[1,2,3],[4,5,6],[7,8,9]]`

**初始化**：
- `top=0, bottom=2, left=0, right=2`

**第一轮**：
1. 上边（从左到右）：`[1,2,3]`，`top` 变为 1
2. 右边（从上到下）：`[6,9]`，`right` 变为 1
3. 下边（从右到左）：`[8,7]`，`bottom` 变为 1
4. 左边（从下到上）：`[4]`，`left` 变为 1

此时 `top=1, bottom=1, left=1, right=1`，中间还剩元素 5

**第二轮**：
1. 上边：`[5]`，`top` 变为 2

此时 `top=2 > bottom=1`，循环结束。

**结果**：`[1,2,3,6,9,8,7,4,5]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 方向模拟 | O(m×n) | O(m×n) | 需要 visited 数组 |
| 边界收缩 | O(m×n) | O(1) | **推荐**，空间更优 |

---

## 易错点总结

### 1. 边界检查

```python
if top <= bottom:   # 遍历下边前要检查
    # 遍历下边

if left <= right:   # 遍历左边前要检查
    # 遍历左边
```

对于奇数行/列的矩阵，最后可能只剩一行或一列，避免重复遍历。

### 2. 边界更新顺序

```python
# 上边遍历后，top 加 1
# 右边遍历后，right 减 1
# 下边遍历后，bottom 减 1
# 左边遍历后，left 加 1
```

顺序不能错，否则会导致遍历错误。

### 3. 反向遍历的范围

```python
for col in range(right, left - 1, -1):  # 注意是 left-1，且步长为 -1
```

### 4. 空矩阵处理

```python
if not matrix or not matrix[0]:
    return []
```

---

## 扩展思考

### 1. 逆时针螺旋遍历

改变遍历顺序：右→上→左→下

### 2. 按层遍历

这道题本质上是按层遍历矩阵，从外到内一层一层处理。

### 3. 螺旋填充

给定数字 n，生成 n×n 的螺旋矩阵。思路类似，只是从读取变成写入。

---

## 相关题目

- [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)
- [885. 螺旋矩阵 III](https://leetcode.cn/problems/spiral-matrix-iii/)
- [2326. 螺旋矩阵 IV](https://leetcode.cn/problems/spiral-matrix-iv/)
