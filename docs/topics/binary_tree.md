---
title: 二叉树
category: 数据结构
parent_topic: tree.md
difficulty_range: [简单, 困难]
last_updated: 2026-02-25
---

# 二叉树

## 知识点概述

二叉树是每个节点最多有两个子节点的树结构，是最常见的树形结构。

### 节点定义

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
```

## 二叉树类型

### 1. 满二叉树

每层节点都达到最大值，深度为 k 的满二叉树有 2^k - 1 个节点。

### 2. 完全二叉树

除最后一层外，其他层的节点数都达到最大，最后一层的节点都靠左排列。

### 3. 二叉搜索树（BST）

- 左子树所有节点值 < 根节点值
- 右子树所有节点值 > 根节点值
- 左右子树也都是 BST

### 4. 平衡二叉树

任意节点的左右子树高度差不超过 1。

## 常见操作

### 遍历模板

参考 [树](tree.md) 的遍历方法。

### 层序遍历（BFS）

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

## 常见题型

### 1. 递归遍历

- 前序、中序、后序遍历
- 树的深度和高度

### 2. 层序遍历

- BFS 遍历
- 右视图
- 之字形遍历

**相关题目：**
- TBD

### 3. 路径问题

- 路径和
- 最长路径
- 路径是否存在

### 4. 构造与修改

- 翻转二叉树
- 从遍历序列构造
- 合并二叉树

## 解题技巧

### 技巧 1：递归模板

```python
def traverse(root):
    # 1. 终止条件
    if not root:
        return
    
    # 2. 处理当前节点（前序位置）
    process(root)
    
    # 3. 递归左子树
    traverse(root.left)
    
    # 4. 处理当前节点（中序位置）
    process(root)
    
    # 5. 递归右子树
    traverse(root.right)
    
    # 6. 处理当前节点（后序位置）
    process(root)
```

### 技巧 2：层序遍历模板

使用队列，记录每层大小。

### 技巧 3：路径问题

使用回溯 + DFS。

## DFS 的两种思路

### 自顶向下 DFS（先序遍历）

在「递」的过程中维护值，从根节点向下传递信息。

```python
# 求二叉树最大深度（自顶向下思路）
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    # 当前节点深度 = 1 + max(左子树深度, 右子树深度)
    return self.maxDepth(root.left) + self.maxDepth(root.right) + 1
```

### 自底向上 DFS（后序遍历）

在「归」的过程中计算，先递归处理子节点，再处理当前节点。

```python
# 合并二叉树
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    return TreeNode(
        root1.val + root2.val,
        self.mergeTrees(root1.left, root2.left),
        self.mergeTrees(root1.right, root2.right)
    )
```

## 二叉搜索树（BST）

### 性质

- 节点的左子树仅包含键**小于**节点键的节点
- 节点的右子树仅包含键**大于**节点键的节点
- 左右子树也必须是二叉搜索树

**平衡的二叉搜索树插入、查找的时间复杂度都是 O(logn)**

### 验证 BST

```python
def isValidBST(self, root: Optional[TreeNode], left=float('-inf'), right=float('inf')) -> bool:
    if root is None:
        return True
    x = root.val
    return left < x < right and \
           self.isValidBST(root.left, left, x) and \
           self.isValidBST(root.right, x, right)
```

### BST 转累加树

遍历顺序：**右 → 根 → 左**（降序遍历）

```python
def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    s = 0
    def dfs(node: TreeNode) -> None:
        if node is None:
            return
        dfs(node.right)  # 先遍历右子树
        nonlocal s
        s += node.val
        node.val = s
        dfs(node.left)
    dfs(root)
    return root
```

### 有序数组转平衡 BST

**关键**：BST 中序遍历后变成升序数组！

```python
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def dfs(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = dfs(left, mid - 1)
        root.right = dfs(mid + 1, right)
        return root
    return dfs(0, len(nums) - 1)
```

## 二叉树与链表

### 二叉树展开为链表

```python
def flatten(self, root: TreeNode) -> None:
    """将二叉树原地展开为链表（使用先右后左的前序遍历）"""
    curr = root
    while curr:
        if curr.left:
            # 找到左子树的最右节点
            predecessor = curr.left
            while predecessor.right:
                predecessor = predecessor.right
            # 将右子树接到最右节点
            predecessor.right = curr.right
            # 左子树移到右边
            curr.right = curr.left
            curr.left = None
        curr = curr.right
```

## 相关知识点

- [树](tree.md)
- [BFS 模式](../patterns/bfs.md)
- [DFS 模式](../patterns/dfs.md)
- [BFS 模板](../templates/bfs_template.md)
- [DFS 模板](../templates/dfs_template.md)

## 题目列表

**中等：**
- TBD

## 重点提示

- 理解递归的本质：处理当前节点 + 递归子问题
- 区分前中后序的处理时机
- 层序遍历一定用 BFS（队列）
- 深度优先用 DFS（递归或栈）
