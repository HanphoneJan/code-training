---
title: DFS 模板
category: 算法模板
last_updated: 2026-02-25
---

# DFS（深度优先搜索）模板

## 二叉树遍历（递归）

### 前序遍历

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    前序遍历：根 -> 左 -> 右
    时间复杂度：O(n)
    空间复杂度：O(h)，h 是树的高度
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)  # 访问根节点
        dfs(node.left)           # 遍历左子树
        dfs(node.right)          # 遍历右子树
    
    dfs(root)
    return result
```

### 中序遍历

```python
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    中序遍历：左 -> 根 -> 右
    BST 的中序遍历是有序的
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)          # 遍历左子树
        result.append(node.val) # 访问根节点
        dfs(node.right)         # 遍历右子树
    
    dfs(root)
    return result
```

### 后序遍历

```python
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    后序遍历：左 -> 右 -> 根
    适合需要先处理子树的问题
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)          # 遍历左子树
        dfs(node.right)         # 遍历右子树
        result.append(node.val) # 访问根节点
    
    dfs(root)
    return result
```

## 二叉树遍历（迭代）

### 前序遍历（迭代）

```python
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    使用栈实现前序遍历
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # 先右后左，保证左子树先被处理
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

### 中序遍历（迭代）

```python
def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    使用栈实现中序遍历
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        # 一直往左走
        while current:
            stack.append(current)
            current = current.left
        
        # 处理栈顶节点
        current = stack.pop()
        result.append(current.val)
        
        # 转向右子树
        current = current.right
    
    return result
```

## 图的 DFS

```python
from typing import Dict, List, Set

def dfs_graph(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    图的深度优先搜索
    时间复杂度：O(V + E)
    空间复杂度：O(V)
    """
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        result.append(node)
        
        # 遍历所有邻居
        for neighbor in graph.get(node, []):
            dfs(neighbor)
    
    dfs(start)
    return result
```

## 矩阵的 DFS

```python
from typing import List

def dfs_matrix(matrix: List[List[int]], row: int, col: int) -> int:
    """
    矩阵的深度优先搜索
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    def dfs(r, c):
        # 边界检查
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            (r, c) in visited or
            matrix[r][c] == -1):  # -1 表示障碍物
            return 0
        
        visited.add((r, c))
        
        # 处理当前格子
        count = 1
        
        # 四个方向递归
        count += dfs(r + 1, c)  # 下
        count += dfs(r - 1, c)  # 上
        count += dfs(r, c + 1)  # 右
        count += dfs(r, c - 1)  # 左
        
        return count
    
    return dfs(row, col)
```

## 回溯模板

```python
from typing import List

def backtrack_template(nums: List[int]) -> List[List[int]]:
    """
    回溯算法通用模板
    用于排列、组合、子集等问题
    """
    result = []
    path = []
    
    def backtrack(start_index):
        # 1. 终止条件
        if satisfy_condition():
            result.append(path[:])  # 记录答案（需要拷贝）
            return
        
        # 2. 遍历所有选择
        for i in range(start_index, len(nums)):
            # 剪枝
            if should_prune(i):
                continue
            
            # 3. 做选择
            path.append(nums[i])
            
            # 4. 递归
            backtrack(i + 1)  # 或 i（可重复选择）
            
            # 5. 撤销选择（回溯）
            path.pop()
    
    backtrack(0)
    return result

def satisfy_condition() -> bool:
    """判断是否满足终止条件"""
    return True

def should_prune(i: int) -> bool:
    """判断是否需要剪枝"""
    return False
```

## 全排列

```python
def permute(nums: List[int]) -> List[List[int]]:
    """
    全排列：不重复元素
    时间复杂度：O(n * n!)
    """
    result = []
    path = []
    used = [False] * len(nums)
    
    def backtrack():
        # 终止条件：路径长度等于数组长度
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            # 剪枝：跳过已使用的元素
            if used[i]:
                continue
            
            # 做选择
            path.append(nums[i])
            used[i] = True
            
            # 递归
            backtrack()
            
            # 撤销选择
            path.pop()
            used[i] = False
    
    backtrack()
    return result
```

## 组合

```python
def combine(n: int, k: int) -> List[List[int]]:
    """
    组合：从 1...n 中选 k 个数
    """
    result = []
    path = []
    
    def backtrack(start):
        # 终止条件：路径长度等于 k
        if len(path) == k:
            result.append(path[:])
            return
        
        # 剪枝：剩余元素不够了
        for i in range(start, n + 1):
            if n - i + 1 < k - len(path):
                break
            
            # 做选择
            path.append(i)
            
            # 递归：从 i+1 开始（避免重复）
            backtrack(i + 1)
            
            # 撤销选择
            path.pop()
    
    backtrack(1)
    return result
```

## 子集

```python
def subsets(nums: List[int]) -> List[List[int]]:
    """
    子集：返回所有子集
    """
    result = []
    path = []
    
    def backtrack(start):
        # 每个节点都是一个答案
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
    
    backtrack(0)
    return result
```

## 岛屿问题

```python
def num_islands(grid: List[List[str]]) -> int:
    """
    岛屿数量：计算连通区域个数
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        # 边界检查
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
        
        # 标记为已访问
        grid[r][c] = '0'
        
        # 四个方向递归
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    
    return count
```

## 路径和

```python
def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    路径和：判断是否存在根到叶节点的路径，和为 target
    """
    if not root:
        return False
    
    # 叶子节点
    if not root.left and not root.right:
        return root.val == target
    
    # 递归左右子树
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))
```

## DFS 关键点

### 1. 何时使用 DFS

- ✅ 树的遍历
- ✅ 图的遍历
- ✅ 路径搜索
- ✅ 排列组合
- ✅ 回溯问题

### 2. 递归三要素

1. **递归函数的参数和返回值**
2. **终止条件**
3. **单层递归逻辑**

### 3. 前中后序的选择

- **前序**：需要向下传递信息
- **中序**：BST 的有序遍历
- **后序**：需要向上返回信息

### 4. 回溯关键

- 做选择 → 递归 → 撤销选择
- 一定要撤销选择，恢复状态

## 相关链接

- [DFS 模式](../patterns/dfs.md)
- [BFS 模板](bfs_template.md)
- [回溯模式](../patterns/backtracking.md)

## 时间与空间复杂度

- **时间复杂度**：O(V + E) 或 O(n)
- **空间复杂度**：O(h)，h 是递归深度
