---
title: 对称二叉树
platform: LeetCode
difficulty: Easy
id: 101
url: https://leetcode.cn/problems/symmetric-tree/
tags:
  - 树
  - 递归
  - 二叉树
date_added: 2026-03-25
---

# 101. 对称二叉树

## 题目描述

给你一个二叉树的根节点 `root`，检查它是否轴对称。

## 示例

**示例 1：**
```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

**示例 2：**
```
输入：root = [1,2,2,null,3,null,3]
输出：false
```

---

## 解题思路

### 第一步：理解问题本质

二叉树对称的条件：
- 根节点的左右子树镜像对称
- 左子树的左子树 == 右子树的右子树
- 左子树的右子树 == 右子树的左子树

### 第二步：最优解法 —— 递归

**核心洞察**：
- 将"相同的树"的判断改为"镜像相同"的判断
- `isSameTree(p, q)` 改为比较 `p.left` 和 `q.right`，`p.right` 和 `q.left`

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
    对称二叉树 - 递归

    核心思想：
    二叉树对称的条件是根节点的左右子树镜像对称。

    判断镜像对称：
    - 两个根节点的值相等
    - 左子树的左子树 == 右子树的右子树
    - 左子树的右子树 == 右子树的左子树

    时间复杂度：O(n)
    空间复杂度：O(h)，h 是树的高度
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **递归（最优）** | **O(n)** | **O(h)** |

---

## 相关题目

- [100. 相同的树](https://leetcode.cn/problems/same-tree/)
- [572. 另一棵树的子树](https://leetcode.cn/problems/subtree-of-another-tree/)
