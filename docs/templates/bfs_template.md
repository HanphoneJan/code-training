------










































































































































































































































































































- [102. 二叉树的层序遍历](../problems/lc/0102_level_order.md)## 应用题目- [二叉树](../topics/binary_tree.md)- [DFS 模板](dfs_template.md)- [BFS 模式](../patterns/bfs.md)## 相关链接- O(V) 或 O(m * n)，取决于队列和访问集合的大小### 4. 空间复杂度- 矩阵：O(m * n)- 树/图：O(V + E)，V 是顶点数，E 是边数### 3. 时间复杂度- **集合**：记录已访问的节点（避免重复）- **队列**：存储待访问的节点### 2. 数据结构- ✅ 拓扑排序- ✅ 矩阵中的最短距离- ✅ 图的最短路径（无权图）- ✅ 树的层序遍历### 1. 何时使用 BFS## BFS 关键点```    return 0            steps += 1        begin_set = next_set                                word_list.discard(next_word)                        next_set.add(next_word)                    if next_word in word_list:                                            return steps + 1                    if next_word in end_set:                    # 如果在另一端找到了                                        next_word = word[:i] + c + word[i+1:]                for c in 'abcdefghijklmnopqrstuvwxyz':            for i in range(len(word)):            # 尝试所有可能的变换        for word in begin_set:                next_set = set()                    begin_set, end_set = end_set, begin_set        if len(begin_set) > len(end_set):        # 优化：总是从较小的集合开始    while begin_set and end_set:        steps = 1        word_list.discard(end)    word_list.discard(start)    end_set = {end}    begin_set = {start}    # 从两端同时开始            return 0    if end not in word_list:    """    用于单词接龙等问题    双向 BFS：从起点和终点同时搜索    """def bidirectional_bfs(start: str, end: str, word_list: Set[str]) -> int:from typing import Setfrom collections import deque```python## 双向 BFS```    return max_time if fresh_count == 0 else -1                    queue.append((new_row, new_col, time + 1))                fresh_count -= 1                matrix[new_row][new_col] = 2  # 变腐烂                                matrix[new_row][new_col] == 1):  # 新鲜的橘子                0 <= new_col < cols and             if (0 <= new_row < rows and                         new_row, new_col = row + dr, col + dc        for dr, dc in directions:                max_time = max(max_time, time)        row, col, time = queue.popleft()    while queue:        max_time = 0                    fresh_count += 1            elif matrix[r][c] == 1:  # 新鲜的橘子                queue.append((r, c, 0))            if matrix[r][c] == 2:  # 腐烂的橘子        for c in range(cols):    for r in range(rows):    # 找到所有源点（腐烂的橘子）        fresh_count = 0    queue = deque()        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]    rows, cols = len(matrix), len(matrix[0])    """    例如：腐烂的橘子问题    从多个源点开始的 BFS    """def multi_source_bfs(matrix: List[List[int]]) -> List[List[int]]:from typing import Listfrom collections import deque```python## 多源 BFS```    return result            result.append(current_level)                        queue.append(child)            for child in node.children:            # 将所有子节点加入队列                        current_level.append(node.val)            node = queue.popleft()        for _ in range(level_size):                current_level = []        level_size = len(queue)    while queue:        queue = deque([root])    result = []            return []    if not root:    """    N 叉树的层序遍历    """def level_order_n_ary(root: Node) -> List[List[int]]:        self.children = children if children is not None else []        self.val = val    def __init__(self, val=None, children=None):class Node:from typing import Listfrom collections import deque```python## N 叉树的层序遍历```    return False    # 根据具体问题实现    """判断是否是目标位置"""def is_target(row: int, col: int) -> bool:    return -1                    queue.append((new_row, new_col, dist + 1))                visited.add((new_row, new_col))                                matrix[new_row][new_col] != -1):  # -1 表示障碍物                (new_row, new_col) not in visited and                0 <= new_col < cols and             if (0 <= new_row < rows and             # 边界检查 + 访问检查 + 障碍物检查                        new_row, new_col = row + dr, col + dc        for dr, dc in directions:        # 遍历四个方向                    return dist        if is_target(row, col):        # 检查是否是目标                row, col, dist = queue.popleft()    while queue:        queue = deque([(start[0], start[1], 0)])  # (row, col, distance)    visited = set([start])        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上    rows, cols = len(matrix), len(matrix[0])            return 0    if not matrix or not matrix[0]:    """    空间复杂度：O(m * n)    时间复杂度：O(m * n)    矩阵中的 BFS    """def bfs_matrix(matrix: List[List[int]], start: Tuple[int, int]) -> int:from typing import List, Tuplefrom collections import deque```python## 矩阵的 BFS```    return -1  # 未找到路径                    queue.append((neighbor, distance + 1))                visited.add(neighbor)            if neighbor not in visited:                            return distance + 1            if neighbor == end:        for neighbor in graph.get(node, []):        # 遍历所有邻居                node, distance = queue.popleft()    while queue:        queue = deque([(start, 0)])  # (节点, 距离)    visited = set([start])            return 0    if start == end:    """    空间复杂度：O(V)    时间复杂度：O(V + E)    无权图的最短路径    """def shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> int:from typing import Dict, List, Setfrom collections import deque```python## 图的 BFS（最短路径）```    return result            result.append(current_level)                        queue.append(node.right)            if node.right:                queue.append(node.left)            if node.left:            # 将下一层节点加入队列                        current_level.append(node.val)            node = queue.popleft()        for _ in range(level_size):        # 遍历当前层的所有节点                current_level = []        level_size = len(queue)  # 当前层的节点数    while queue:        queue = deque([root])    result = []            return []    if not root:    """    空间复杂度：O(n)    时间复杂度：O(n)    二叉树的层序遍历    """def level_order(root: Optional[TreeNode]) -> List[List[int]]:        self.right = right        self.left = left        self.val = val    def __init__(self, val=0, left=None, right=None):class TreeNode:from typing import Optional, Listfrom collections import deque```python## 树的层序遍历# BFS（广度优先搜索）模板---last_updated: 2026-02-25category: 算法模板title: BFS 模板title: BFS 模板
category: 代码模板
related_pattern: ../patterns/bfs.md
last_updated: 2026-02-25
---

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

- [102. 二叉树的层序遍历](../problems/lc/102)
- 岛屿数量
- 腐烂的橘子
- 单词接龙
