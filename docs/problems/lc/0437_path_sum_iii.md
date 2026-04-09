---
title: 路径总和 III
platform: LeetCode
difficulty: Medium
id: 437
url: https://leetcode.cn/problems/path-sum-iii/
tags:
  - 树
  - 深度优先搜索
  - 哈希表
  - 前缀和
topics:
  - ../../topics/binary-tree.md
  - ../../topics/prefix-sum.md
patterns:
  - ../../patterns/tree-dfs.md
date_added: 2026-04-09
date_reviewed: []
---

# 437. 路径总和 III

## 题目描述

给定一个二叉树的根节点 `root`，和一个整数 `targetSum`，求该二叉树里节点值之和等于 `targetSum` 的路径的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

**示例 1：**
```
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条：
      5 -> 3
      5 -> 2 -> 1
      -3 -> 11
```

**示例 2：**
```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
```

---

## 解题思路

### 第一步：理解问题本质

这道题与「路径总和 I/II」的区别在于：
- 路径**不需要从根节点开始**
- 路径**不需要在叶子节点结束**
- 路径方向必须是向下的

这意味着**任意两个节点之间的向下的路径**都可能是答案。

### 第二步：暴力解法 - 双重 DFS

**思路：** 以每个节点为起点，向下搜索所有可能的路径。

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        # 以当前节点为起点的路径数 + 以左右子树任意节点为起点的路径数
        return self.countFromRoot(root, targetSum) + \
               self.pathSum(root.left, targetSum) + \
               self.pathSum(root.right, targetSum)
    
    def countFromRoot(self, node, remain):
        if not node:
            return 0
        count = 0
        if node.val == remain:
            count += 1
        count += self.countFromRoot(node.left, remain - node.val)
        count += self.countFromRoot(node.right, remain - node.val)
        return count
```

**为什么不够好？** 时间复杂度 O(n^2)，最坏情况下（链表）会超时。

### 第三步：优化解法 - 前缀和 + 哈希表

**关键洞察：** 这道题可以转化为「和为 K 的子数组」的树上版本。

**前缀和定义：** 从根节点到当前节点的路径和。

**核心思想：**
- 如果存在两个节点的前缀和之差等于 targetSum，则这两个节点之间的路径和为 targetSum
- 即：`prefix[j] - prefix[i] = targetSum`，则 `prefix[i] = prefix[j] - targetSum`

**算法步骤：**
1. 用哈希表记录每个前缀和出现的次数
2. 遍历树时，计算当前前缀和 `curr_sum`
3. 以当前节点为终点的有效路径数 = `cnt[curr_sum - targetSum]`
4. 将当前前缀和加入哈希表，递归处理子树
5. **回溯**时恢复哈希表状态

```python
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 前缀和为 0 的路径有 1 条
        ans = 0
        
        def dfs(node, curr_sum):
            nonlocal ans
            if not node:
                return
            
            curr_sum += node.val
            ans += cnt[curr_sum - targetSum]
            
            cnt[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            cnt[curr_sum] -= 1  # 回溯
        
        dfs(root, 0)
        return ans
```

---

## 完整代码实现

```python
from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    路径总和 III - 前缀和 + 哈希表

    核心思路：
    利用前缀和的思想。定义从根节点到当前节点的路径和为 curr_sum，
    如果存在某个祖先节点的前缀和为 curr_sum - targetSum，
    则从该祖先节点到当前节点的路径和为 targetSum。

    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 前缀和为 0 的路径有 1 条（空路径）
        ans = 0

        def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
            nonlocal ans
            if not node:
                return

            curr_sum += node.val
            ans += cnt[curr_sum - targetSum]
            cnt[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            cnt[curr_sum] -= 1  # 回溯

        dfs(root, 0)
        return ans
```

---

## 示例推演

以 `root = [10,5,-3,3,2,null,11], targetSum = 8` 为例：

**树结构：**
```
      10
     /  \
    5   -3
   / \    \
  3   2   11
```

**DFS 过程：**

| 节点 | 当前前缀和 | cnt[curr_sum-8] | 有效路径 | 哈希表状态 |
|------|-----------|-----------------|----------|-----------|
| 10 | 10 | cnt[2]=0 | 0 | {0:1, 10:1} |
| 5 | 15 | cnt[7]=0 | 0 | {0:1, 10:1, 15:1} |
| 3 | 18 | cnt[10]=1 | 1 | {0:1, 10:1, 15:1, 18:1} |
| 2 | 17 | cnt[9]=0 | 0 | {0:1, 10:1, 15:1, 17:1} |
| -3 | 7 | cnt[-1]=0 | 0 | {0:1, 10:1, 7:1} |
| 11 | 18 | cnt[10]=1 | 1 | {0:1, 10:1, 7:1, 18:1} |

**最终结果：** 3 条路径
- 5 -> 3（和为 8）
- 5 -> 2 -> 1（和为 8）
- -3 -> 11（和为 8）

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 双重 DFS | O(n^2) | O(n) | 最坏情况退化为链表 |
| 前缀和+哈希 | O(n) | O(n) | 每个节点只访问一次 |

**说明：**
- n 是树的节点数
- 前缀和解法的时间复杂度是 O(n)，因为每个节点只访问一次
- 空间复杂度包括哈希表和递归栈

---

## 易错点总结

### 1. 哈希表初始值

```python
# 必须初始化 cnt[0] = 1
cnt = defaultdict(int)
cnt[0] = 1  # 表示从根节点到当前节点的路径和恰好等于 targetSum
```

### 2. 回溯的时机

```python
# 在递归子树之前增加计数
cnt[curr_sum] += 1
dfs(node.left, curr_sum)
dfs(node.right, curr_sum)
cnt[curr_sum] -= 1  # 回溯时必须减 1
```

### 3. 前缀和的计算顺序

```python
# 先计算当前前缀和
curr_sum += node.val
# 再查询以当前节点为终点的有效路径数
ans += cnt[curr_sum - targetSum]
# 最后将当前前缀和加入哈希表
cnt[curr_sum] += 1
```

---

## 扩展思考

### 1. 与「和为 K 的子数组」的关系

这道题是 [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) 的树上版本，核心思想完全相同。

### 2. 如果需要返回具体的路径？

可以用栈记录当前路径，当找到有效路径时复制路径加入结果。

### 3. 相关题目

- [112. 路径总和](https://leetcode.cn/problems/path-sum/) - 路径必须从根到叶子
- [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/) - 返回所有路径
- [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) - 数组版本

---

## 相关题目

- [112. 路径总和](https://leetcode.cn/problems/path-sum/)
- [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/)
- [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
