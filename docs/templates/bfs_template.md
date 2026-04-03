---
title: BFS 模板
  category: 代码模板
  last_updated: 2026-02-25
---
# BFS（广度优先搜索）模板

# BFS 模板

## 1. 二叉树层序遍历

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
    """二叉树的层序遍历"""
    if not root:
        return []
  
    result = []
    queue = deque([root])
  
    while queue:
        level_size = len(queue)  # 当前层的节点数
        current_level = []
  
        # 处理当前层的所有节点
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

### C++

```cpp
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

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

## 2. 图的 BFS

### Python

```python
from collections import deque
from typing import Dict, List, Set

def bfs_graph(graph: Dict[int, List[int]], start: int) -> List[int]:
    """图的广度优先搜索"""
    visited = set([start])
    queue = deque([start])
    result = []
  
    while queue:
        node = queue.popleft()
        result.append(node)
  
        # 遍历所有邻居
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
  
    return result
```

### 带距离的 BFS

```python
def bfs_with_distance(graph: Dict[int, List[int]], 
                      start: int, 
                      end: int) -> int:
    """返回从 start 到 end 的最短距离"""
    if start == end:
        return 0
  
    visited = set([start])
    queue = deque([(start, 0)])  # (节点, 距离)
  
    while queue:
        node, distance = queue.popleft()
  
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return distance + 1
      
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
  
    return -1  # 不可达
```

## 3. 矩阵的 BFS

### Python

```python
from collections import deque
from typing import List, Tuple

def bfs_matrix(matrix: List[List[int]], 
               start: Tuple[int, int]) -> List[List[int]]:
    """
    矩阵的 BFS，返回每个位置到起点的距离
    0 表示可通过，1 表示障碍
    """
    if not matrix or not matrix[0]:
        return []
  
    rows, cols = len(matrix), len(matrix[0])
    distances = [[-1] * cols for _ in range(rows)]
  
    # 初始化
    start_row, start_col = start
    distances[start_row][start_col] = 0
    queue = deque([(start_row, start_col)])
  
    # 四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
    while queue:
        row, col = queue.popleft()
        current_dist = distances[row][col]
  
        # 遍历四个方向
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
      
            # 检查边界、障碍和访问状态
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                matrix[new_row][new_col] == 0 and
                distances[new_row][new_col] == -1):
          
                distances[new_row][new_col] = current_dist + 1
                queue.append((new_row, new_col))
  
    return distances
```

### C++

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> bfsMatrix(vector<vector<int>>& matrix, 
                               pair<int, int> start) {
    if (matrix.empty() || matrix[0].empty()) return {};
  
    int rows = matrix.size(), cols = matrix[0].size();
    vector<vector<int>> distances(rows, vector<int>(cols, -1));
  
    queue<pair<int, int>> q;
    q.push(start);
    distances[start.first][start.second] = 0;
  
    // 四个方向
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
  
    while (!q.empty()) {
        auto [row, col] = q.front();
        q.pop();
        int currentDist = distances[row][col];
  
        for (auto [dr, dc] : directions) {
            int newRow = row + dr;
            int newCol = col + dc;
      
            if (newRow >= 0 && newRow < rows && 
                newCol >= 0 && newCol < cols &&
                matrix[newRow][newCol] == 0 &&
                distances[newRow][newCol] == -1) {
          
                distances[newRow][newCol] = currentDist + 1;
                q.push({newRow, newCol});
            }
        }
    }
  
    return distances;
}
```

## 4. 多源 BFS

### Python

```python
from collections import deque
from typing import List

def multi_source_bfs(matrix: List[List[int]]) -> List[List[int]]:
    """
    多源 BFS
    从所有值为 1 的位置同时开始 BFS
    返回每个位置到最近的 1 的距离
    """
    if not matrix or not matrix[0]:
        return []
  
    rows, cols = len(matrix), len(matrix[0])
    distances = [[-1] * cols for _ in range(rows)]
    queue = deque()
  
    # 将所有源点加入队列
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                distances[i][j] = 0
                queue.append((i, j))
  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
    while queue:
        row, col = queue.popleft()
        current_dist = distances[row][col]
  
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
      
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                distances[new_row][new_col] == -1):
          
                distances[new_row][new_col] = current_dist + 1
                queue.append((new_row, new_col))
  
    return distances
```

## 5. N 叉树的层序遍历

### Python

```python
from collections import deque
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def levelOrder(root: Node) -> List[List[int]]:
    """N 叉树的层序遍历"""
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
      
            # 将所有子节点加入队列
            for child in node.children:
                queue.append(child)
  
        result.append(current_level)
  
    return result
```

## 使用说明

### 何时使用 BFS？

1. **层序遍历**：需要按层处理节点
2. **最短路径**：无权图中的最短路径
3. **连通性**：判断是否连通或找到所有连通节点
4. **最近距离**：找到最近的目标节点

### 关键要点

1. **使用队列**：FIFO，保证层序
2. **记录访问状态**：避免重复访问
3. **记录层数**：使用 `len(queue)` 确定当前层大小
4. **边界检查**：矩阵中要检查边界

### 常见错误

❌ 忘记标记已访问，导致死循环
❌ 在加入队列后才标记访问（应该加入时就标记）
❌ 矩阵中没有检查边界
❌ 忘记记录层数

## 相关资源

- [BFS 模式](../patterns/bfs)
- [二叉树](../topics/binary_tree)
- [图](../topics/graph)

## 练习题目

- TBD
- 岛屿数量
- 腐烂的橘子
- 单词接龙

## BFS 关键点

### 1. 何时使用 BFS

- ✅ 树的层序遍历
- ✅ 图的最短路径（无权图）
- ✅ 矩阵中的最短距离
- ✅ 拓扑排序

### 2. 数据结构

- **队列**：存储待访问的节点
- **集合**：记录已访问的节点（避免重复）

### 3. 时间复杂度

- 树/图：O(V + E)，V 是顶点数，E 是边数
- 矩阵：O(m * n)

### 4. 空间复杂度

- O(V) 或 O(m * n)，取决于队列和访问集合的大小

## 相关链接

- [BFS 模式](../patterns/bfs.md)
- [DFS 模板](dfs_template.md)
- [二叉树](../topics/binary_tree.md)
