---
title: 二叉树的最近公共祖先
platform: LeetCode
difficulty: Medium
id: 236
url: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
tags:
  - 树
  - 深度优先搜索
  - 二叉树
topics:
  - ../../topics/binary-tree.md
  - ../../topics/dfs.md
patterns:
  - ../../patterns/tree-traversal.md
date_added: 2026-04-09
date_reviewed: []
---

# 236. 二叉树的最近公共祖先

## 题目描述

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

**最近公共祖先的定义**：对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

**题目保证**：
- 所有 Node.val 互不相同
- p != q
- p 和 q 均存在于给定的二叉树中

## 示例

**示例 1：**
```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```

**示例 2：**
```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。
```

---

## 解题思路

### 第一步：理解问题本质

最近公共祖先（LCA）是 p 和 q 的所有公共祖先中深度最大的那个。

**关键观察**：
- 如果 p 和 q 分别在当前节点的左右子树中，当前节点就是 LCA
- 如果 p 和 q 都在左子树（或右子树），LCA 也在那一边
- 如果当前节点是 p 或 q，当前节点就是 LCA（一个节点可以是自己的祖先）

### 第二步：暴力解法 - 存储父节点

遍历树，记录每个节点的父节点。然后从 p 开始，记录所有祖先。再从 q 开始，找到第一个公共祖先。

```python
def lowestCommonAncestor(self, root, p, q):
    parent = {root: None}
    stack = [root]
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]
    return q
```

**分析**：时间 O(n)，空间 O(n)。

### 第三步：优化解法 - 递归

递归遍历，利用返回值判断 LCA 位置。

### 第四步：最优解法 - 递归（简洁版）

---

## 完整代码实现

```python
class Solution:
    """
    二叉树的最近公共祖先 - 递归法

    核心思路：
    递归遍历树，对于每个节点：
    1. 如果当前节点是 p 或 q，返回当前节点
    2. 递归在左子树和右子树中查找 p 和 q
    3. 如果左右子树都找到了，说明当前节点是 LCA
    4. 如果只有一边找到，返回那一边的结果

    时间复杂度：O(n)
    空间复杂度：O(h)
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止条件
        if not root or root == p or root == q:
            return root

        # 递归在左右子树中查找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都找到了，当前节点是 LCA
        if left and right:
            return root

        # 返回非空的结果
        return left if left else right
```

---

## 示例推演

以示例 1 为例：`p = 5, q = 1`

```
        3
       / \
      5   1
     / \  / \
    6  2 0  8
       / \
      7   4
```

**递归过程**：

1. `LCA(3, 5, 1)`
   - `LCA(5, 5, 1)` -> 返回 5（找到 p）
   - `LCA(1, 5, 1)` -> 返回 1（找到 q）
   - 左右都找到，返回 3

结果：3

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 存储父节点 | O(n) | O(n) | 需要额外空间 |
| 递归 | O(n) | O(h) | h 为树高度 |

---

## 易错点总结

### 1. 终止条件

```python
if not root or root == p or root == q:
    return root
```

包含三种情况：空节点、找到 p、找到 q。

### 2. 返回值处理

```python
# 简洁写法
return left if left else right

# 等价于
if left and right:
    return root
if left:
    return left
return right
```

### 3. BST 的 LCA

如果是二叉搜索树，可以利用大小关系：

```python
if p.val < root.val > q.val:
    return self.lowestCommonAncestor(root.left, p, q)
if p.val > root.val < q.val:
    return self.lowestCommonAncestor(root.right, p, q)
return root
```

---

## 扩展思考

### 1. 二叉搜索树的 LCA

[235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)，利用 BST 性质可以更快解决。

### 2. 相关题目

- [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
- [235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [1644. 二叉树的最近公共祖先 II](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/) - p 或 q 可能不存在
- [1650. 二叉树的最近公共祖先 III](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/) - 有父指针

---

## 相关题目

- [235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [1644. 二叉树的最近公共祖先 II](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/)
- [1650. 二叉树的最近公共祖先 III](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/)
- [1676. 二叉树的最近公共祖先 IV](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv/)
