---
title: 二叉搜索树中第 K 小的元素
platform: LeetCode
difficulty: Medium
id: 230
url: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
tags:
  - 树
  - 深度优先搜索
  - 二叉搜索树
  - 二叉树
topics:
  - ../../topics/binary-search-tree.md
  - ../../topics/dfs.md
patterns:
  - ../../patterns/inorder-traversal.md
date_added: 2026-04-09
date_reviewed: []
---

# 230. 二叉搜索树中第 K 小的元素

## 题目描述

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（从 1 开始计数）。

## 示例

**示例 1：**
```
输入: root = [3,1,4,null,2], k = 1
输出: 1
```

**示例 2：**
```
输入: root = [5,3,6,2,4,null,null,1], k = 3
输出: 3
```

---

## 解题思路

### 第一步：理解问题本质

**二叉搜索树（BST）的性质**：
- 左子树所有节点值 < 根节点值
- 右子树所有节点值 > 根节点值
- **中序遍历结果是升序序列**

因此，第 k 小的元素 = 中序遍历的第 k 个元素。

### 第二步：暴力解法 - 中序遍历转数组

遍历完整棵树，将中序结果存入数组，返回第 k-1 个元素。

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result[k - 1]
```

**为什么不够好**：需要 O(n) 空间，且遍历完整棵树。

### 第三步：优化解法 - 提前终止

不需要遍历完整棵树，找到第 k 个就可以停止。

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.count = 0
    self.result = 0

    def dfs(node):
        if not node:
            return False
        if dfs(node.left):
            return True
        self.count += 1
        if self.count == k:
            self.result = node.val
            return True
        return dfs(node.right)

    dfs(root)
    return self.result
```

### 第四步：最优解法 - 迭代中序遍历

使用栈模拟递归，找到第 k 个就停止，避免递归栈开销。

---

## 完整代码实现

```python
from typing import Optional

class Solution:
    """
    二叉搜索树中第 K 小的元素 - 中序遍历

    核心思路：
    二叉搜索树的中序遍历结果是升序序列。
    因此，第 k 小的元素 = 中序遍历的第 k 个元素。

    优化：不需要遍历完整棵树，找到第 k 个就可以停止。

    时间复杂度：O(h + k)
    空间复杂度：O(h)
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.count = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            """中序遍历，返回 True 表示已找到"""
            if not node:
                return False

            # 遍历左子树
            if dfs(node.left):
                return True

            # 访问当前节点
            self.count += 1
            if self.count == k:
                self.result = node.val
                return True

            # 遍历右子树
            return dfs(node.right)

        dfs(root)
        return self.result
```

---

## 示例推演

以 `root = [5,3,6,2,4,null,null,1], k = 3` 为例：

```
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

**中序遍历过程**：

| 步骤 | 操作 | count | 说明 |
|------|------|-------|------|
| 1 | 走到最左（1） | 1 | 访问 1 |
| 2 | 返回父节点（2） | 2 | 访问 2 |
| 3 | 返回父节点（3） | 3 | 访问 3，count == k，返回 3 |

结果：3

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 中序转数组 | O(n) | O(n) | 遍历整棵树 |
| 递归提前终止 | O(h + k) | O(h) | h 为树高度 |
| 迭代提前终止 | O(h + k) | O(h) | 栈空间 |

**进阶优化**：如果频繁查询，可以给每个节点增加子树大小字段，实现 O(h) 查询。

---

## 易错点总结

### 1. k 从 1 开始计数

**错误**：`if self.count == k - 1`

**正确**：`if self.count == k`

### 2. 忘记提前终止

```python
# 错误：遍历完整棵树
inorder(node.left)
result.append(node.val)  # 继续遍历
inorder(node.right)

# 正确：找到就返回
if dfs(node.left):
    return True
# ...
return dfs(node.right)
```

### 3. 第 k 大怎么求？

**方法**：右-中-左遍历（降序），或者找第 n-k+1 小。

---

## 扩展思考

### 1. 频繁查询的优化

给每个节点增加 `size` 字段（子树节点数）：
- 左子树大小 >= k：第 k 小在左子树
- 左子树大小 + 1 == k：当前节点就是第 k 小
- 否则：第 k 小在右子树，找第 k - left_size - 1 小

### 2. 相关题目

- [230. 二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)
- [538. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/) - 右-中-左遍历
- [703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)

---

## 相关题目

- [538. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)
- [783. 二叉搜索树节点最小距离](https://leetcode.cn/problems/minimum-distance-between-bst-nodes/)
- [1038. 从二叉搜索树到更大和树](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/)
