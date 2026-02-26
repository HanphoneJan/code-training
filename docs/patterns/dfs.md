---
title: DFS 模式
category: 算法模式
difficulty: 简单-困难
applicable_to:
  - 树
  - 图
  - 回溯
last_updated: 2026-02-25
---

# DFS（深度优先搜索）模式

## 模式概述

DFS 是一种图遍历算法，沿着一条路径尽可能深入，直到无法继续，再回溯到上一节点继续探索。

## 核心特点

- **深度优先**：先访问子节点
- **使用递归或栈**：LIFO 数据结构
- **回溯思想**：探索完一条路径后返回

## 适用场景

1. **树的遍历**（前序、中序、后序）
2. **图的遍历**
3. **路径搜索**
4. **排列组合**
5. **回溯算法**

## 基本模板

### 递归 DFS（树）

```python
def dfs_tree(root):
    # 1. 终止条件
    if not root:
        return
    
    # 2. 前序位置：处理当前节点
    process(root)
    
    # 3. 递归左子树
    dfs_tree(root.left)
    
    # 4. 中序位置
    process(root)
    
    # 5. 递归右子树
    dfs_tree(root.right)
    
    # 6. 后序位置
    process(root)
```

### 迭代 DFS（栈）

```python
def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        process(node)
        
        # 注意：先右后左，保证左子树先被处理
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 图的 DFS

```python
def dfs_graph(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    process(node)
    
    for neighbor in graph[node]:
        dfs_graph(neighbor, visited)
```

### 矩阵的 DFS

```python
def dfs_matrix(matrix, row, col, visited):
    rows, cols = len(matrix), len(matrix[0])
    
    # 边界检查
    if (row < 0 or row >= rows or 
        col < 0 or col >= cols or 
        (row, col) in visited or
        matrix[row][col] == obstacle):
        return
    
    visited.add((row, col))
    process(row, col)
    
    # 四个方向递归
    dfs_matrix(matrix, row + 1, col, visited)  # 下
    dfs_matrix(matrix, row - 1, col, visited)  # 上
    dfs_matrix(matrix, row, col + 1, visited)  # 右
    dfs_matrix(matrix, row, col - 1, visited)  # 左
```

## 实战案例

### 案例 1：二叉树的前序遍历

```python
def preorder(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)  # 前序：根
        dfs(node.left)           # 左
        dfs(node.right)          # 右
    
    dfs(root)
    return result
```

### 案例 2：求树的最大深度

```python
def maxDepth(root):
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1
```

### 案例 3：路径和

```python
def hasPathSum(root, target):
    if not root:
        return False
    
    # 叶子节点
    if not root.left and not root.right:
        return root.val == target
    
    # 递归左右子树
    return (hasPathSum(root.left, target - root.val) or
            hasPathSum(root.right, target - root.val))
```

## DFS 的三种位置

```python
def traverse(root):
    if not root:
        return
    
    # 【前序位置】
    # - 刚进入节点时
    # - 适合：复制节点、记录路径
    
    traverse(root.left)
    
    # 【中序位置】
    # - 左子树处理完
    # - 适合：BST 的有序遍历
    
    traverse(root.right)
    
    # 【后序位置】
    # - 左右子树都处理完
    # - 适合：计算子树信息、删除节点
```

## 回溯模板

```python
def backtrack(path, choices):
    # 终止条件
    if satisfy_condition:
        result.append(path[:])  # 记录答案
        return
    
    # 遍历所有选择
    for choice in choices:
        # 做选择
        path.append(choice)
        
        # 递归
        backtrack(path, next_choices)
        
        # 撤销选择（回溯）
        path.pop()
```

## BFS vs DFS

| 特性 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈/递归 | 队列 |
| 遍历顺序 | 深度优先 | 广度优先 |
| 路径搜索 | ✅ 是 | ❌ 不适合 |
| 最短路径 | ❌ 否 | ✅ 是 |
| 空间复杂度 | O(h) 高度 | O(w) 宽度 |

## 解题步骤

1. **确定递归函数签名**
   - 参数：当前节点、必要的状态
   - 返回值：需要的结果类型

2. **确定终止条件**
   - 空节点
   - 叶子节点
   - 找到答案

3. **确定单层逻辑**
   - 处理当前节点
   - 递归子问题
   - 合并结果

4. **选择遍历位置**
   - 前序：需要向下传递信息
   - 后序：需要向上返回信息

## 常见模式

### 1. 分治

将问题分解为子问题，合并子问题的解。

```python
def divide_conquer(root):
    if not root:
        return base_case
    
    left = divide_conquer(root.left)
    right = divide_conquer(root.right)
    
    return merge(left, right, root.val)
```

### 2. 回溯

探索所有可能的路径。

### 3. 记忆化搜索

使用缓存避免重复计算。

```python
memo = {}

def dfs_with_memo(state):
    if state in memo:
        return memo[state]
    
    result = compute(state)
    memo[state] = result
    return result
```

## 时间与空间复杂度

- **时间复杂度**：O(V + E)，V 是顶点数，E 是边数
- **空间复杂度**：O(h)，h 是递归深度

## 相关知识点

- [树](../topics/tree)
- [二叉树](../topics/binary_tree)
- [BFS 模式](bfs)
- [回溯模式](backtracking)
- [DFS 模板](../templates/dfs_template)

## 练习题目

**简单：**
- 二叉树的前序遍历
- 二叉树的最大深度
- 路径总和

**中等：**
- 二叉树的所有路径
- 岛屿数量
- 全排列

**困难：**
- N 皇后
- 单词搜索 II

## 要点总结

- ✅ 递归是最常用的实现方式
- ✅ 理解前中后序的位置含义
- ✅ 回溯 = DFS + 撤销操作
- ✅ 注意递归终止条件
- ✅ 空间复杂度取决于递归深度
