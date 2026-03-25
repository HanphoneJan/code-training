---
title: 二叉树展开为链表
platform: LeetCode
difficulty: Medium
id: 114
url: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
tags:
  - 树
  - 链表
  - 二叉树
date_added: 2026-03-25
---

# 114. 二叉树展开为链表

## 题目描述

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树**先序遍历**顺序相同。

## 示例

**示例 1：**
```
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
```

**示例 2：**
```
输入：root = []
输出：[]
```

**示例 3：**
```
输入：root = [0]
输出：[0]
```

---

## 解题思路

### 第一步：理解问题本质

将二叉树按前序遍历顺序展开为链表，要求使用 O(1) 额外空间。

### 第二步：最优解法 —— Morris 遍历变种

**核心洞察**：
- 对于当前节点，如果它有左子树：
  1. 找到左子树的最右节点（前驱节点）
  2. 将当前节点的右子树接到前驱节点的右边
  3. 将左子树移到右边，左子树置空

---

## 完整代码实现

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    二叉树展开为链表 - O(1)空间复杂度

    核心思想：
    使用 Morris 遍历的变种，将二叉树原地展开为链表。

    算法步骤：
    1. 对于当前节点curr，如果它有左子树：
       a. 找到左子树的最右节点（前驱节点）
       b. 将curr的右子树接到前驱节点的右边
       c. 将curr的左子树变为右子树，左子树置空
    2. curr移动到右子节点

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # 将右子树接到前驱节点右边
                predecessor.right = curr.right

                # 左子树移到右边
                curr.right = curr.left
                curr.left = None

            curr = curr.right
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 递归 | O(n) | O(n) |
| **Morris遍历（最优）** | **O(n)** | **O(1)** |

---

## 相关题目

- [430. 扁平化多级双向链表](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/)
