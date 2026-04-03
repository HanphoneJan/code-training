---
title: 二叉树中的最大路径和
platform: LeetCode
difficulty: 困难
id: 124
url: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
tags:
  - 二叉树
  - 深度优先搜索
  - 动态规划
topics:
  - ../../topics/binary_tree.md
  - ../../topics/dfs.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../patterns/tree_traversal.md
date_added: 2026-04-03
date_reviewed: []
---

# 0124. 二叉树中的最大路径和

## 题目描述

二叉树中的 **路径** 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 **至多出现一次**。该路径 **至少包含一个** 节点，且不一定经过根节点。

**路径和** 是路径中各节点值的总和。

给你一个二叉树的根节点 `root`，返回其 **最大路径和**。

## 示例

**示例 1：**
```
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```

**示例 2：**
```
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
```

---

## 解题思路

### 第一步：理解路径的两种形态

对于任意一个节点，以它为 "最高点" 的路径有两种可能：
1. **链式路径**（向上连接父节点）：只能选左子树或右子树中的一条分支
2. **完整路径**（不向上连接）：可以同时包含左子树 + 当前节点 + 右子树

递归函数只能返回链式路径，因为父节点只能接受一个分支。完整路径用来更新全局最大值。

### 第二步：暴力解法

枚举所有节点对，检查它们的路径和。但二叉树中找两节点路径本身就很复杂，时间复杂度太高。

### 第三步：优化思路

对于每个节点，计算经过它的最大路径和：
- 左子树最大贡献（负数取 0）
- 右子树最大贡献（负数取 0）
- 当前节点值

同时返回以当前节点为端点的最大链式路径和。

### 第四步：最优解法 - 后序 DFS

用后序遍历（先处理子节点，再处理根节点）：
1. 递归获取左右子树的最大贡献值
2. 计算经过当前节点的完整路径和，更新全局最大值
3. 返回以当前节点为端点的最大链式路径和

关键：如果子树贡献为负，不如不选（取 `max(贡献, 0)`）。

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
    124. 二叉树中的最大路径和 - 深度优先搜索（后序遍历）

    核心思想：
    同时维护两个值：
    1. 以当前节点为端点的最大链式路径和（返回给父节点）
    2. 经过当前节点的完整路径和（更新全局最大值）

    时间复杂度：O(n)
    空间复杂度：O(h)，h 为树高
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = root.val

        def findPath(root: TreeNode) -> int:
            nonlocal res
            if not root:
                return 0

            left_s = max(findPath(root.left), 0)
            right_s = max(findPath(root.right), 0)

            ans = left_s + right_s + root.val
            res = max(ans, res)

            return max(left_s, right_s) + root.val

        findPath(root)
        return res
```

---

## 示例推演

以 `root = [-10, 9, 20, null, null, 15, 7]` 为例：

```
        -10
       /    \
      9      20
            /  \
           15   7
```

**节点 9**：左右都是 null，贡献 0。完整路径 = 9。`res = max(-10, 9) = 9`。返回链式路径 = 9。

**节点 15**：完整路径 = 15。返回链式路径 = 15。

**节点 7**：完整路径 = 7。返回链式路径 = 7。

**节点 20**：
- 左贡献 = 15，右贡献 = 7
- 完整路径 = 15 + 20 + 7 = 42，`res = max(9, 42) = 42`
- 返回链式路径 = max(15, 7) + 20 = 35

**节点 -10**：
- 左贡献 = 9，右贡献 = 35
- 完整路径 = 9 + (-10) + 35 = 34，`res` 保持 42
- 返回链式路径 = max(9, 35) + (-10) = 25

最终答案：`42`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(h) | 枚举所有节点对 |
| 后序 DFS | O(n) | O(h) | **最优解** |

---

## 易错点总结

### 1. 负数子树的处理

必须用 `max(子树贡献, 0)`，因为负数子树不如不选。

### 2. 返回值的含义

递归函数返回的是**链式路径和**（只能选一个分支），不是完整路径和。

### 3. 全局变量初始值

初始化为 `root.val`，因为路径至少包含一个节点。如果用 0，当所有节点都是负数时会出错。

### 4. 只有一个节点的情况

如果根节点是唯一的节点，答案就是根节点的值。

---

## 扩展思考

### 如果路径必须经过根节点？

那就只需要计算根节点的完整路径和即可。

### 如果要求输出具体的路径？

需要在递归时记录左右子树贡献最大的那条路径，最后回溯重构。

## 相关题目

- [112. 路径总和](https://leetcode.cn/problems/path-sum/)
- [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)
- [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)
