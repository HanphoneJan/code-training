---
title: 翻转二叉树
platform: LeetCode
difficulty: Easy
id: 226
url: https://leetcode.cn/problems/invert-binary-tree/
tags:
  - 树
  - 深度优先搜索
  - 广度优先搜索
  - 二叉树
topics:
  - ../../topics/binary-tree.md
  - ../../topics/dfs.md
  - ../../topics/bfs.md
patterns:
  - ../../patterns/tree-traversal.md
date_added: 2026-04-09
date_reviewed: []
---

# 226. 翻转二叉树

## 题目描述

给你一棵二叉树的根节点 `root`，翻转这棵二叉树，并返回其根节点。

**翻转**：交换每个节点的左右子树。

## 示例

**示例 1：**
```
输入: root = [4,2,7,1,3,6,9]
输出: [4,7,2,9,6,3,1]

     4              4
    / \            / \
   2   7    ->    7   2
  / \  / \        / \  / \
 1  3 6  9      9  6 3  1
```

**示例 2：**
```
输入: root = [2,1,3]
输出: [2,3,1]
```

---

## 解题思路

### 第一步：理解问题本质

翻转二叉树 = 交换每个节点的左右子节点。

这是一个**递归结构**的问题：整棵树的翻转 = 左子树翻转 + 右子树翻转 + 交换左右子树。

### 第二步：暴力解法 - 复制新树

遍历原树，创建新树，左右子树交换位置。

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    new_root = TreeNode(root.val)
    new_root.left = self.invertTree(root.right)
    new_root.right = self.invertTree(root.left)
    return new_root
```

**为什么不够好**：需要创建新节点，空间复杂度 O(n)。

### 第三步：优化解法 - 原地递归

直接修改原树的指针，无需创建新节点。

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    # 先递归翻转
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    # 再交换
    root.left = right
    root.right = left
    return root
```

### 第四步：最优解法 - 递归或迭代

递归最简洁，迭代（BFS）可以避免栈溢出。

---

## 完整代码实现

```python
from typing import Optional

class Solution:
    """
    翻转二叉树 - 递归法

    核心思路：
    递归地翻转左右子树，然后交换它们。

    时间复杂度：O(n)
    空间复杂度：O(h) - h 为树高度
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # 递归翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 交换左右子树
        root.left = right
        root.right = left

        return root
```

---

## 示例推演

以 `[4,2,7,1,3,6,9]` 为例：

```
     4
    / \
   2   7
  / \  / \
 1  3 6  9
```

**递归过程**：

1. `invertTree(4)`
   - `invertTree(2)`
     - `invertTree(1)` -> 返回 1
     - `invertTree(3)` -> 返回 3
     - 交换：2 的左=3，右=1
     - 返回 2
   - `invertTree(7)`
     - `invertTree(6)` -> 返回 6
     - `invertTree(9)` -> 返回 9
     - 交换：7 的左=9，右=6
     - 返回 7
   - 交换：4 的左=7，右=2
   - 返回 4

**结果**：
```
     4
    / \
   7   2
  / \  / \
 9  6 3  1
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 复制新树 | O(n) | O(n) | 需要额外空间 |
| 原地递归 | O(n) | O(h) | h 为树高度 |
| BFS 迭代 | O(n) | O(w) | w 为树的最大宽度 |

---

## 易错点总结

### 1. 忘记返回 root

**错误**：
```python
self.invertTree(root.left)
self.invertTree(root.right)
# 没有 return root
```

**正确**：
```python
return root  # 必须返回根节点
```

### 2. 交换顺序错误

先交换再递归也可以，但要保持一致：

```python
# 方案一：先递归，后交换
left = self.invertTree(root.left)
right = self.invertTree(root.right)
root.left, root.right = right, left

# 方案二：先交换，后递归
root.left, root.right = root.right, root.left
self.invertTree(root.left)
self.invertTree(root.right)
```

### 3. 空节点处理

```python
if not root:
    return None  # 不是 return root
```

---

## 扩展思考

### 1. 翻转 N 叉树

[559. N 叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/) 类似思路，交换 children 列表。

### 2. 相关题目

- [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/) - 判断树是否对称
- [100. 相同的树](https://leetcode.cn/problems/same-tree/) - 判断两棵树是否相同
- [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) - 本题

---

## 相关题目

- [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)
- [100. 相同的树](https://leetcode.cn/problems/same-tree/)
- [572. 另一棵树的子树](https://leetcode.cn/problems/subtree-of-another-tree/)
