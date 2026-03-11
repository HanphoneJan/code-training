---
title: BFS 模式
category: 算法模式
difficulty: 简单-中等
applicable_to:
  - 树
  - 图
  - 矩阵
last_updated: 2026-02-25
---

# BFS（广度优先搜索）模式

## 模式概述

BFS 是一种图遍历算法，从起点开始，先访问所有相邻节点，再访问下一层的节点。

## 核心特点

- **层序遍历**：逐层访问
- **最短路径**：保证找到的是最短路径（无权图）
- **使用队列**：FIFO 数据结构

## 适用场景

1. **树的层序遍历**
2. **图的最短路径**（无权图）
3. **矩阵中的最短距离**
4. **拓扑排序**

## 基本模板

### 树的 BFS

```python
from collections import deque

def bfs_tree(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # 当前层的节点数
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # 将下一层节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

### 图的 BFS

```python
from collections import deque

def bfs_graph(start, graph):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        process(node)  # 处理当前节点
        
        # 遍历所有邻居
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 矩阵的 BFS

```python
from collections import deque

def bfs_matrix(matrix, start_row, start_col):
    rows, cols = len(matrix), len(matrix[0])
    visited = set([(start_row, start_col)])
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    
    # 四个方向
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col, dist = queue.popleft()
        
        # 检查是否是目标
        if is_target(row, col):
            return dist
        
        # 遍历四个方向
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # 检查边界和访问状态
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited and
                matrix[new_row][new_col] != obstacle):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1  # 未找到
```

## 实战案例

### 案例 1：二叉树的层序遍历

```python
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

**相关题目：**
- TBD

### 案例 2：图的最短路径

```python
def shortestPath(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        node, distance = queue.popleft()
        
        if node == end:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1
```

## BFS vs DFS

| 特性 | BFS | DFS |
|------|-----|-----|
| 数据结构 | 队列 | 栈/递归 |
| 遍历顺序 | 逐层 | 逐深度 |
| 最短路径 | ✅ 是 | ❌ 否 |
| 空间复杂度 | O(w) 宽度 | O(h) 高度 |
| 应用场景 | 最短路径、层序遍历 | 路径搜索、回溯 |

## 解题步骤

1. **初始化队列**：将起点加入队列
2. **初始化访问集合**：标记起点已访问
3. **循环处理队列**：
   - 取出队首元素
   - 处理当前元素
   - 将未访问的邻居加入队列
4. **返回结果**

## 常见变体

### 1. 多源 BFS

从多个起点同时开始。

```python
def multi_source_bfs(sources):
    queue = deque(sources)
    visited = set(sources)
    
    while queue:
        node = queue.popleft()
        # 处理逻辑
```

### 2. 双向 BFS

从起点和终点同时搜索。

### 3. 带层数的 BFS

记录每个节点的层数。

```python
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        # 处理当前层
```

## 时间与空间复杂度

- **时间复杂度**：O(V + E)，V 是顶点数，E 是边数
- **空间复杂度**：O(V)，队列和访问集合

## 相关知识点

- [树](../topics/tree)
- [二叉树](../topics/binary_tree)
- [图](../topics/graph)
- [DFS 模式](dfs)
- [BFS 模板](../templates/bfs_template)

## 练习题目

**简单：**
- [102. 二叉树的层序遍历](../problems/lc/102)
- N 叉树的层序遍历

**中等：**
- 二叉树的锯齿形层序遍历
- 腐烂的橘子
- 岛屿数量

**困难：**
- 单词接龙
- 最小基因变化

## 要点总结

- ✅ 使用队列实现
- ✅ 记录访问状态避免重复
- ✅ 适合求最短路径
- ✅ 层序遍历是 BFS 的典型应用
