---
title: N 皇后
platform: LeetCode
difficulty: 困难
id: 51
url: https://leetcode.cn/problems/n-queens/
tags:
  - 回溯
  - 数组
topics:
  - ../../topics/array.md
  - ../../topics/backtracking.md
patterns:
  - ../../patterns/backtracking_constraint.md
date_added: 2026-03-23
date_reviewed: []
---

# 0051. N 皇后

## 题目描述

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n 皇后问题** 的解决方案。

每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

## 示例

**示例 1：**
```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**
```
输入：n = 1
输出：[["Q"]]
```

---

## 解题思路

### 第一步：理解问题本质

**皇后的攻击范围**：
1. 同一行
2. 同一列
3. 同一对角线（左上到右下、右上到左下）

**约束条件**：
- 每行恰好放一个皇后（否则行内冲突）
- 每列恰好放一个皇后（列冲突检查）
- 对角线不能重复（对角线冲突检查）

### 第二步：回溯思路

**逐行放置**：
- 第 0 行：尝试在第 0, 1, 2, ..., n-1 列放置
- 第 1 行：在剩余的安全位置放置
- ...
- 第 n-1 行：放置最后一个皇后

**关键问题**：如何快速判断冲突？

### 第三步：对角线的数学表示

**主对角线**（左上到右下）：
- 特点：`row - col` 是常数
- 范围：`-(n-1)` 到 `n-1`
- 索引转换：`row - col + (n-1)` → `[0, 2n-2]`

**副对角线**（右上到左下）：
- 特点：`row + col` 是常数
- 范围：`0` 到 `2n-2`
- 直接使用 `row + col` 作为索引

**冲突标记数组**：
- `used_cols[col]`：第 col 列是否已有皇后
- `diag1[row + col]`：副对角线是否已有皇后
- `diag2[row - col + n - 1]`：主对角线是否已有皇后

---

## 完整代码实现

```python
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        N 皇后 - 回溯算法

        核心思想：逐行放置皇后，用三个标记数组检查冲突
        """
        ans = []
        queens = [0] * n  # queens[row] = col，表示第 row 行第 col 列放置皇后

        # 冲突标记数组
        used_cols = [False] * n          # 列占用标记
        diag1 = [False] * (n * 2 - 1)    # 副对角线（row + col）
        diag2 = [False] * (n * 2 - 1)    # 主对角线（row - col + n - 1）

        def dfs(row: int) -> None:
            """
            在第 row 行放置皇后
            """
            # 结束条件：所有行都放置完毕
            if row == n:
                # 根据 queens 数组构建棋盘表示
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - 1 - col))
                ans.append(board)
                return

            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                d1 = row + col           # 副对角线索引
                d2 = row - col + n - 1   # 主对角线索引

                # 检查冲突
                if not used_cols[col] and not diag1[d1] and not diag2[d2]:
                    # 做选择
                    queens[row] = col
                    used_cols[col] = diag1[d1] = diag2[d2] = True

                    # 递归处理下一行
                    dfs(row + 1)

                    # 撤销选择（回溯）
                    used_cols[col] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return ans
```

---

## 示例推演

**示例**：`n = 4`

**对角线索引计算**（4×4棋盘）：

| 位置 | row+col (diag1) | row-col+3 (diag2) |
|------|-----------------|-------------------|
| (0,0) | 0 | 3 |
| (0,1) | 1 | 2 |
| (0,2) | 2 | 1 |
| (0,3) | 3 | 0 |
| (1,0) | 1 | 4 |
| (1,1) | 2 | 3 |
| ... | ... | ... |

**DFS 搜索过程**：

| 步骤 | row | 尝试 col | 冲突检查 | 结果 |
|------|-----|----------|----------|------|
| 1 | 0 | 0 | 无冲突 | 放置成功，继续 row=1 |
| 2 | 1 | 0 | col=0 已用 | 冲突，跳过 |
| 3 | 1 | 1 | diag1=2 冲突 | 冲突，跳过 |
| 4 | 1 | 2 | 无冲突 | 放置成功，继续 row=2 |
| 5 | 2 | ... | 所有位置都冲突 | 回溯到 row=1 |
| 6 | 1 | 3 | 无冲突 | 放置成功，继续 row=2 |
| 7 | 2 | 1 | 无冲突 | 放置成功，继续 row=3 |
| 8 | 3 | ... | col=0 diag冲突 | ... |
| 9 | 3 | 2 | 无冲突 | 放置成功！得到一个解 |

**第一个解**：`[1,3,0,2]` → `[".Q..","...Q","Q...","..Q."]`

继续回溯搜索，得到第二个解：`[2,0,3,1]`

---

## 复杂度分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| 时间 | O(n!) | 最坏情况需要尝试 n! 种排列 |
| 空间 | O(n) | 递归深度 + 标记数组 |

实际由于剪枝，远小于 n!。

---

## 易错点总结

### 1. 对角线索引计算

```python
d1 = row + col           # 副对角线（和为常数）
d2 = row - col + n - 1   # 主对角线（差为常数，需要偏移避免负数）
```
不要混淆两个对角线！

### 2. 棋盘构建

```python
'.' * col + 'Q' + '.' * (n - 1 - col)
```
- `col` 个 `.` 在左边
- 中间是 `Q`
- `n-1-col` 个 `.` 在右边

### 3. 标记数组大小

```python
diag1 = [False] * (n * 2 - 1)
diag2 = [False] * (n * 2 - 1)
```
对角线索引范围是 `[0, 2n-2]`，共 `2n-1` 个。

### 4. 多变量同时赋值

```python
used_cols[col] = diag1[d1] = diag2[d2] = True
```
可以链式赋值，但撤销时也要同时撤销。

---

## 扩展思考

### 1. 只返回解的个数

```python
def solveNQueensCount(self, n: int) -> int:
    count = 0
    # ... 初始化 ...
    def dfs(row: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        # ... 递归 ...
    dfs(0)
    return count
```

### 2. 位运算优化

对于 n <= 32，可以用整数位来表示列和对角线，进一步加速。

### 3. N 皇后问题的数学性质

- n = 1：1 个解
- n = 2, 3：无解
- n = 4：2 个解
- n = 8：92 个解

---

## 相关题目

- [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/)（只返回个数）
- [37. 解数独](https://leetcode.cn/problems/sudoku-solver/)
- [46. 全排列](https://leetcode.cn/problems/permutations/)
