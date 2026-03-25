---
title: 二叉树的最大深度
platform: LeetCode
difficulty: Easy
id: 104
url: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
tags:
  - 树
  - 递归
  - DFS
  - 二叉树
date_added: 2026-03-25
---

# 104. 二叉树的最大深度

## 题目描述

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明**：叶子节点是指没有子节点的节点。

## 示例

**示例 1：**
```
输入：root = [3,9,20,null,null,15,7]
输出：3
```

**示例 2：**
```
输入：root = [1,null,2]
输出：2
```

---

## 解题思路

### 第一步：理解问题本质

二叉树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1

### 第二步：最优解法 —— 递归

**核心洞察**：
- 空节点的深度为 0
- 当前节点的深度 = 左右子树最大深度 + 1

---

## 完整代码实现

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    二叉树的最大深度 - 递归/DFS

    核心思想：
    二叉树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1

    时间复杂度：O(n)
    空间复杂度：O(h)
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **递归（最优）** | **O(n)** | **O(h)** |

---

## 相关题目

- [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)
- [559. N 叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/)
