---
title: 岛屿数量
platform: LeetCode
difficulty: Medium
id: 200
url: https://leetcode.cn/problems/number-of-islands/
tags:
  - 深度优先搜索
  - 广度优先搜索
  - 并查集
  - 数组
  - 矩阵
topics:
  - ../../topics/graph.md
  - ../../topics/dfs.md
  - ../../topics/bfs.md
patterns:
  - ../../patterns/flood-fill.md
date_added: 2026-04-09
date_reviewed: []
---

# 200. 岛屿数量

## 题目描述

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由**水平方向和/或竖直方向上相邻的陆地**连接形成。此外，你可以假设该网格的四条边均被水包围。

## 示例

**示例 1：**
```
输入: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出: 1
```

**示例 2：**
```
输入: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出: 3
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的** Flood Fill（洪水填充）**问题。核心思想是：

1. 遍历整个网格，找到一块未访问的陆地 `'1'`
2. 从这块陆地开始，使用 DFS 或 BFS 将所有相连的陆地标记为已访问
3. 每发现一块未访问的陆地，岛屿数量 +1

**关键**：只能上下左右四个方向移动，对角线不算相邻。

### 第二步：暴力解法 - 并查集

使用并查集维护连通分量：
1. 初始时，每个陆地是一个独立的集合
2. 遍历网格，如果两个相邻格子都是陆地，合并它们
3. 最后统计集合数量

```python
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    # 并查集实现...
    # 时间复杂度较高，代码较复杂
```

**为什么不够好**：并查集适合动态连通性问题，本题用 DFS/BFS 更直观。

### 第三步：优化解法 - DFS

递归深度优先搜索，遇到陆地就"淹没"整个岛屿。

```python
def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
        return
    grid[r][c] = '2'  # 标记为已访问
    dfs(grid, r-1, c)
    dfs(grid, r+1, c)
    dfs(grid, r, c-1)
    dfs(grid, r, c+1)
```

### 第四步：最优解法 - DFS/BFS + 原地标记

DFS 和 BFS 都可以，选择取决于：
- **DFS**：代码简洁，但递归深度可能过大
- **BFS**：用队列实现，避免栈溢出

---

## 完整代码实现

```python
from typing import List
from collections import deque

class Solution:
    """
    岛屿数量 - DFS/BFS

    核心思路：
    遍历整个网格，当遇到 '1'（未访问的陆地）时，发现一个新岛屿。
    然后使用 DFS 或 BFS 将与这块陆地相连的所有陆地标记为已访问。

    时间复杂度：O(m×n)
    空间复杂度：O(m×n)
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    self._dfs(grid, r, c)

        return count

    def _dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        """DFS 标记与 (r, c) 相连的所有陆地"""
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return

        grid[r][c] = '2'  # 标记为已访问

        # 四个方向递归
        self._dfs(grid, r - 1, c)  # 上
        self._dfs(grid, r + 1, c)  # 下
        self._dfs(grid, r, c - 1)  # 左
        self._dfs(grid, r, c + 1)  # 右
```

---

## 示例推演

以示例 2 为例：

```
初始网格：
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

步骤 1: 在 (0,0) 发现 '1'，岛屿数=1，DFS 标记整个岛屿
2 2 0 0 0
2 2 0 0 0
0 0 1 0 0
0 0 0 1 1

步骤 2: 在 (2,2) 发现 '1'，岛屿数=2，DFS 标记
2 2 0 0 0
2 2 0 0 0
0 0 2 0 0
0 0 0 1 1

步骤 3: 在 (3,3) 发现 '1'，岛屿数=3，DFS 标记
2 2 0 0 0
2 2 0 0 0
0 0 2 0 0
0 0 0 2 2

遍历结束，共 3 个岛屿
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 并查集 | O(m×n × α(m×n)) | O(m×n) | α 为阿克曼函数的反函数 |
| DFS | O(m×n) | O(m×n) | 递归栈空间 |
| BFS | O(m×n) | O(min(m,n)) | 队列空间 |

其中 m 为行数，n 为列数。

---

## 易错点总结

### 1. 对角线不算相邻

**错误**：检查 8 个方向

**正确**：只检查上下左右 4 个方向

```python
# 正确：四个方向
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```

### 2. 边界条件检查

```python
# 必须先检查边界，再检查 grid[r][c]
if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
    return
```

### 3. 标记方式

```python
# 标记为 '2' 而不是 '0'
# '0' 表示水，'2' 表示已访问的陆地，语义更清晰
grid[r][c] = '2'
```

---

## 扩展思考

### 1. 岛屿的最大面积？

[695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)：在 DFS 时统计每个岛屿的格子数。

### 2. 岛屿的周长？

[463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/)：统计每个陆地格子与水或边界相邻的边数。

### 3. 被围绕的区域？

[130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)：从边界开始 DFS，标记所有与边界相连的 'O'。

### 4. 相关题目

- [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- [695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)
- [463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/)
- [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)
- [417. 太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/)

---

## 相关题目

- [695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)
- [463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/)
- [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)
- [417. 太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/)
- [827. 最大人工岛](https://leetcode.cn/problems/making-a-large-island/)
