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
- [102. 二叉树的层序遍历](../problems/lc/0102_level_order.md)

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

## 相关知识点

- [树](tree.md)
- [BFS 模式](../patterns/bfs.md)
- [DFS 模式](../patterns/dfs.md)
- [BFS 模板](../templates/bfs_template.md)
- [DFS 模板](../templates/dfs_template.md)

## 题目列表

**中等：**
- [102. 二叉树的层序遍历](../problems/lc/0102_level_order.md)

## 重点提示

- 理解递归的本质：处理当前节点 + 递归子问题
- 区分前中后序的处理时机
- 层序遍历一定用 BFS（队列）
- 深度优先用 DFS（递归或栈）
