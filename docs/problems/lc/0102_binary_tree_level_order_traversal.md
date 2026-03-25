---
title: 二叉树的层序遍历
platform: LeetCode
difficulty: Medium
id: 102
url: https://leetcode.cn/problems/binary-tree-level-order-traversal/
tags:
  - 树
  - BFS
  - 二叉树
date_added: 2026-03-25
---

# 102. 二叉树的层序遍历

## 题目描述

给你二叉树的根节点 `root`，返回其节点值的**层序遍历**。（即逐层地，从左到右访问所有节点）。

## 示例

**示例 1：**
```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```

**示例 2：**
```
输入：root = [1]
输出：[[1]]
```

**示例 3：**
```
输入：root = []
输出：[]
```

---

## 解题思路

### 第一步：理解问题本质

层序遍历就是按层从左到右访问节点。这是典型的**BFS（广度优先搜索）**问题。

### 第二步：最优解法 —— BFS

**核心洞察**：
- 使用队列存储当前层的节点
- 每次处理一层的所有节点
- 将子节点加入队列，供下一轮处理

---

## 完整代码实现

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    二叉树的层序遍历 - BFS

    核心思想：
    使用队列（BFS）按层遍历二叉树。

    时间复杂度：O(n)
    空间复杂度：O(n)
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        cur = deque([root])

        while cur:
            value = []
            for _ in range(len(cur)):
                node = cur.popleft()
                value.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(value)

        return res
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **BFS（最优）** | **O(n)** | **O(n)** |

---

## 相关题目

- [107. 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)
- [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
