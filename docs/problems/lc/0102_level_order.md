---
title: 二叉树的层序遍历
platform: LeetCode
difficulty: 中等
id: 102
url: https://leetcode.cn/problems/binary-tree-level-order-traversal/
tags:
  - 树
  - 广度优先搜索
  - 二叉树
topics:
  - ../../topics/tree.md
  - ../../topics/binary_tree.md
patterns:
  - ../../patterns/bfs.md
templates:
  - ../../templates/bfs_template.md
date_added: 2026-02-25
date_reviewed: []
---

# 0102. 二叉树的层序遍历

## 题目描述

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。（即逐层地，从左到右访问所有节点）。

## 解题思路

### 方法一：BFS（广度优先搜索）

使用队列实现层序遍历：
1. 将根节点加入队列
2. 当队列不为空时：
   - 记录当前层的节点数
   - 遍历当前层的所有节点
   - 将下一层的节点加入队列

- 时间复杂度：O(n)
- 空间复杂度：O(n)

## 代码实现

### Python

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
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

### C++

```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    
    vector<vector<int>> result;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        result.push_back(currentLevel);
    }
    
    return result;
}
```

## 相关题目

- [0103. 二叉树的锯齿形层序遍历](103)


## 笔记

- BFS 的核心是使用队列
- 层序遍历的关键是记录每层的节点数
- 参考 [BFS 模板](../../templates/bfs_template.md)
