---
title: 将有序数组转换为二叉搜索树
platform: LeetCode
difficulty: Easy
id: 108
url: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
tags:
  - 树
  - 二分查找
  - 二叉搜索树
  - 二叉树
date_added: 2026-03-25
---

# 108. 将有序数组转换为二叉搜索树

## 题目描述

给你一个整数数组 `nums` ，其中元素已经按**升序**排列，请你将其转换为一棵**高度平衡**二叉搜索树。

**高度平衡**二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

## 示例

**示例 1：**
```
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案
```

**示例 2：**
```
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树
```

---

## 解题思路

### 第一步：理解问题本质

- 二叉搜索树的中序遍历是有序数组
- 选择数组中间元素作为根节点，可以保证树的高度平衡

### 第二步：最优解法 —— 递归

**核心洞察**：
- 选择中间元素作为根节点
- 递归构建左右子树

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
    将有序数组转换为二叉搜索树 - 递归

    核心思想：
    选择数组中间元素作为根节点，可以保证树的高度平衡。
    然后递归构建左右子树。

    时间复杂度：O(n)
    空间复杂度：O(log n)
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(nums) - 1)
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| **递归（最优）** | **O(n)** | **O(log n)** |

---

## 相关题目

- [109. 有序链表转换二叉搜索树](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/)
- [1382. 将二叉搜索树变平衡](https://leetcode.cn/problems/balance-a-binary-search-tree/)
