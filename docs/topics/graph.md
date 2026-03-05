---
title: 图
category: 数据结构
difficulty_range: [中等, 困难]
last_updated: 2026-03-05
---

# 图

## 知识点概述

图由顶点与边组成，常见表示为**邻接表**或**邻接矩阵**。

- **邻接表**：数组存储所有顶点，每个顶点对应一个链表记录邻接顶点，空间省，适合稀疏图
- **邻接矩阵**：二维数组存储边的权值，查询边 O(1)，适合稠密图

## 常见考点

- BFS 与 DFS
- 最短路径与拓扑排序
- 连通分量

## 图的存储

```python
# 邻接表（推荐，用列表实现）
g = [[] for _ in range(n)]  # n个节点
for x, y in edges:
    g[x].append(y)
    g[y].append(x)  # 无向图需要双向添加

# 带权图的邻接表
g = [[] for _ in range(n)]
for x, y, w in edges:
    g[x].append((y, w))
```

## 网格图

**网格图是一种简化的图，默认是无向无权图。**

### 岛屿问题模板

[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

```python
def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0]) if grid else 0
    if rows == 0:
        return 0

    def dfs(r: int, c: int) -> None:
        # 边界检查 + 是否已访问
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
            return
        grid[r][c] = '2'  # 标记为已访问
        # 遍历四个方向
        dfs(r - 1, c)  # 上
        dfs(r + 1, c)  # 下
        dfs(r, c - 1)  # 左
        dfs(r, c + 1)  # 右

    def bfs(r: int, c: int) -> None:
        from collections import deque
        queue = deque([(r, c)])
        grid[r][c] = '2'
        while queue:
            cr, cc = queue.popleft()
            for nr, nc in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '2'
                    queue.append((nr, nc))

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                ans += 1
                dfs(r, c)  # 或 bfs(r, c)
    return ans
```

### 网格图 DFS vs 二叉树 DFS

| | 二叉树 | 网格图 |
|-----|-------|-------|
| 递归入口 | 根节点 | 网格图的某个格子 |
| 递归方向 | 左儿子和右儿子 | 一般为左右上下的相邻格子 |
| 递归边界 | 空节点 | 出界、遇到障碍或者已访问 |

## BFS 单源最短路

**BFS 是先访问近的，再访问远的，天然具有层序遍历特性，适合求最短路径。**

```python
from collections import deque

def bfs_shortest_path(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    计算从 start 到各个节点的最短路长度
    如果节点不可达，最短路长度为 -1
    节点编号从 0 到 n-1，边权均为 1
    """
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    dis = [-1] * n
    dis[start] = 0
    q = deque([start])

    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:  # 未访问
                dis[y] = dis[x] + 1
                q.append(y)
    return dis
```

## Dijkstra 算法

**适用条件**：没有负数边权。

**核心思想**：贪心，每次选择距离起点最近的未确定节点，用该节点更新邻居的最短距离。

### 堆优化 Dijkstra（适合稀疏图）

```python
import heapq

def dijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    返回从起点 start 到每个点的最短路长度 dis
    如果节点 x 不可达，则 dis[x] = math.inf
    时间复杂度 O((n + m) log m)
    """
    g = [[] for _ in range(n)]
    for x, y, wt in edges:
        g[x].append((y, wt))

    dis = [float('inf')] * n
    dis[start] = 0
    h = [(0, start)]  # (距离, 节点)

    while h:
        dx, x = heapq.heappop(h)
        if dx > dis[x]:  # 已经处理过，跳过
            continue
        for y, wt in g[x]:
            new_dis = dx + wt
            if new_dis < dis[y]:
                dis[y] = new_dis
                heapq.heappush(h, (new_dis, y))

    return dis
```

### 0-1 BFS

边权只有 0 和 1 时，可以用双端队列优化：

```python
from collections import deque

def zero_one_bfs(grid: List[List[int]], health: int) -> bool:
    """
    示例：穿越网格图的安全路径
    grid[i][j] = 0 或 1 表示边权
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    dist[0][0] = health - grid[0][0]
    dq = deque([(0, 0)])

    while dq:
        r, c = dq.popleft()
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = dist[r][c] - grid[nr][nc]
                if new_dist > dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))  # 边权为0，放队首
                    else:
                        dq.append((nr, nc))      # 边权为1，放队尾
    return dist[rows-1][cols-1] >= 0
```

## 拓扑排序

**适用条件**：有向无环图（DAG）。

**核心思想**：将入度为 0 的节点依次入队，处理完一个节点后将其邻居的入度减 1。

```python
from collections import deque

def topological_sort(n: int, edges: List[List[int]]) -> List[int]:
    """
    返回有向无环图（DAG）的其中一个拓扑序
    如果图中有环，返回空列表
    """
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in edges:
        g[x].append(y)
        in_deg[y] += 1

    topo_order = []
    q = deque([i for i, d in enumerate(in_deg) if d == 0])

    while q:
        x = q.popleft()
        topo_order.append(x)
        for y in g[x]:
            in_deg[y] -= 1
            if in_deg[y] == 0:
                q.append(y)

    return topo_order if len(topo_order) == n else []
```

## 连通块计算

### DFS 计算每个连通块的大小

```python
def count_components(n: int, edges: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    vis = [False] * n

    def dfs(x: int) -> int:
        vis[x] = True
        size = 1
        for y in g[x]:
            if not vis[y]:
                size += dfs(y)
        return size

    ans = []
    for i in range(n):
        if not vis[i]:
            ans.append(dfs(i))
    return ans
```
