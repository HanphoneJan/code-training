---
title: 从前序与中序遍历序列构造二叉树
platform: LeetCode
difficulty: Medium
id: 105
url: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
tags:
  - 树
  - 递归
  - 数组
  - 二叉树
date_added: 2026-03-25
---

# 105. 从前序与中序遍历序列构造二叉树

## 题目描述

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**前序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

## 示例

**示例 1：**
```
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```

**示例 2：**
```
输入: preorder = [-1], inorder = [-1]
输出: [-1]
```

---

## 解题思路

### 第一步：理解问题本质

- 前序遍历：根节点 -> 左子树 -> 右子树
- 中序遍历：左子树 -> 根节点 -> 右子树

前序遍历的第一个元素是根节点，在中序遍历中找到该根节点，其左边是左子树，右边是右子树。

### 第二步：最优解法 —— 递归

**核心洞察**：
1. 前序遍历的第一个元素是根节点
2. 在中序遍历中找到根节点位置，确定左子树大小
3. 递归构建左右子树

---

## 完整代码实现

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    从前序与中序遍历序列构造二叉树 - 递归

    核心思想：
    前序遍历的第一个元素是根节点，在中序遍历中找到该根节点的位置，
    其左边是左子树，右边是右子树。然后递归构建左右子树。

    时间复杂度：O(n²)
    空间复杂度：O(n)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        left_size = inorder.index(root_val)

        left = self.buildTree(preorder[1:1 + left_size], inorder[:left_size])
        right = self.buildTree(preorder[1 + left_size:], inorder[left_size + 1:])

        return TreeNode(root_val, left, right)
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **递归（最优）** | **O(n²)** | **O(n)** |

---

## 相关题目

- [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
- [889. 根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)
