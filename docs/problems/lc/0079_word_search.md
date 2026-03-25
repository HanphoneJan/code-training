---
title: 单词搜索
platform: LeetCode
difficulty: Medium
id: 79
url: https://leetcode.cn/problems/word-search/
tags:
  - 数组
  - 回溯
  - 矩阵
date_added: 2026-03-25
---

# 79. 单词搜索

## 题目描述

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word`。如果 `word` 存在于网格中，返回 `true`；否则，返回 `false`。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

## 示例

**示例 1：**
```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**
```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
```

**示例 3：**
```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**回溯/DFS**问题。需要从每个格子出发，搜索是否存在一条路径能组成目标单词。

### 第二步：最优解法 —— 回溯（DFS）

**核心洞察**：
- 从每个格子开始尝试
- 标记已访问的格子（避免重复使用）
- 四个方向搜索
- 恢复现场（回溯）

**优化技巧**：
1. 字母频率预检
2. 首尾优化：从出现次数较少的字母端开始

---

## 完整代码实现

```python
from typing import List
from collections import Counter

class Solution:
    """
    单词搜索 - 回溯算法（DFS）

    核心思想：
    从矩阵的每个位置出发，使用 DFS 搜索是否存在一条路径能组成目标单词。

    回溯的关键：
    1. 标记已访问：将访问过的格子标记为空字符串，避免重复使用
    2. 恢复现场：回溯时将格子恢复原值，供其他路径使用
    3. 四个方向搜索：上下左右

    优化技巧：
    1. 字母频率预检：如果 board 中某字母数量少于 word，直接返回 False
    2. 首尾优化：从出现次数较少的字母端开始搜索

    时间复杂度：O(m * n * 3^L)，L 是单词长度
    空间复杂度：O(L)，递归栈深度
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 优化一：字母频率预检
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):
            return False

        # 优化二：首尾字母优化
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            board[i][j] = ''  # 标记已访问
            for x, y in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k+1):
                    return True
            board[i][j] = word[k]  # 恢复现场
            return False

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 暴力 | O(m*n*4^L) | O(L) |
| **回溯+优化（最优）** | **O(m*n*3^L)** | **O(L)** |

---

## 相关题目

- [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/)
