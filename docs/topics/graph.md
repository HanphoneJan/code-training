---
title: 图
category: 数据结构
difficulty_range: [中等, 困难]
last_updated: 2026-03-10
---

# 图

## 知识点概述

图（Graph）由**顶点（Vertex）**与**边（Edge）**组成，是比线性表和树更复杂的数据结构。树是图的特例（无环连通图），链表是树的特例。

现实生活中到处都是图：社交网络（人与人的关系）、地图导航（路口与道路）、课程依赖（先修课关系）、网页链接等。

## 图的分类

| 分类标准 | 类型 | 说明 | 典型场景 |
|---------|------|------|---------|
| 边的方向 | 无向图 | 边没有方向，A→B 等价于 B→A | 社交关系、分子结构 |
| | 有向图 | 边有方向，A→B 不等于 B→A | 课程依赖、网页链接 |
| 边的权重 | 无权图 | 边只表示"相连"，没有额外信息 | 社交网络好友关系 |
| | 带权图 | 边上有数值，代表距离/费用/时间等 | 地图导航、网络路由 |
| 连通性 | 连通图 | 任意两个顶点之间都有路径 | 交通网络 |
| | 非连通图 | 存在无法到达的顶点对 | 多个独立社交圈 |

```
无向图（5个顶点，5条边）          有向图（DAG，课程依赖）
  0 —— 1                           数学 → 线代
  |    |                            |       |
  2 —— 3                           高数 → 线代
    \                               高数 → 概率
     4
```

> **新手常见困惑**：算法题中，图的输入通常是"边列表"（edges），例如 `edges = [[0,1],[1,2],[2,0]]`，需要自己手动构建邻接表。

---

## 图的存储

### 邻接表 vs 邻接矩阵

| 操作 | 邻接表 | 邻接矩阵 |
|------|--------|---------|
| 空间 | O(n + m) | O(n²) |
| 查询边 x→y 是否存在 | O(度(x)) | **O(1)** |
| 遍历 x 的所有邻居 | O(度(x)) | O(n) |
| 添加边 | O(1) | O(1) |
| 删除边 | O(度(x)) | O(1) |
| 适合场景 | **稀疏图**（m 远小于 n²） | 稠密图（m 接近 n²） |

> **核心结论**：算法题中绝大多数图都是稀疏图，**邻接表是首选**。

### 代码实现

```python
# ===== 无向无权图（最常见）=====
n = 5  # 节点数
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]

g = [[] for _ in range(n)]
for x, y in edges:
    g[x].append(y)
    g[y].append(x)  # 无向图：双向添加！

# g = [[1, 3, 2], [0, 2], [1, 3, 0], [2, 0], []]
# 含义：节点 0 的邻居是 [1, 3, 2]，节点 4 没有邻居

# ===== 有向无权图 =====
g = [[] for _ in range(n)]
for x, y in edges:
    g[x].append(y)  # 有向图：只添加单向边

# ===== 带权图 =====
# edges: [起点, 终点, 权重]
weighted_edges = [[0, 1, 2], [1, 2, 3], [0, 2, 5]]
g = [[] for _ in range(n)]
for x, y, w in weighted_edges:
    g[x].append((y, w))  # 邻居以 (节点, 权重) 元组存储
```

### 新手避坑

```python
# ❌ 错误：忘记无向图需要双向添加
g = [[] for _ in range(n)]
for x, y in edges:
    g[x].append(y)  # 漏了 g[y].append(x)，导致图不完整！

# ❌ 错误：用 [[0]*n]*n 初始化二维数组（浅拷贝问题）
grid = [['.']*cols]*rows  # 所有行引用同一个列表！
# 正确写法：
grid = [['.' for _ in range(cols)] for _ in range(rows)]
```

---

## BFS（广度优先搜索）

### 核心思想

BFS 使用**队列**，从起点开始，先访问所有距离为 1 的节点，再访问距离为 2 的节点……像水波纹一样逐层扩散。

```
BFS 遍历顺序（从节点 0 出发）：
    0
   / \
  1   2
 / \   \
3   4   5

队列变化过程：
[0] → [1, 2] → [2, 3, 4] → [3, 4, 5] → [4, 5] → [5] → []

访问顺序：0, 1, 2, 3, 4, 5（层序遍历）
```

### 为什么 BFS 能求最短路？

**BFS 是先访问近的，再访问远的，天然具有层序遍历特性。**

关键在于：BFS 保证**第一次到达某个节点时的路径就是最短的**。因为队列是 FIFO（先进先出），距离近的节点一定比距离远的节点先出队。

```
从 0 出发，到各节点的最短距离：
第 0 层：0          距离 0
第 1 层：1, 2       距离 1
第 2 层：3, 4, 5    距离 2

每个节点只在第一次被访问时记录距离，后续不会更新（因为第一次一定最短）。
```

> **注意**：BFS 求最短路仅适用于**无权图**（或所有边权相等）。带权图需要用 Dijkstra。

### BFS 单源最短路

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

    dis = [-1] * n          # -1 表示未访问（用 -1 而不是 0，因为距离可能是 0）
    dis[start] = 0           # 起点距离为 0
    q = deque([start])

    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:  # 未访问过
                dis[y] = dis[x] + 1  # 距离 = 父节点距离 + 1
                q.append(y)
    return dis
```

### 示例推演

**输入**：`n=5, edges=[[0,1],[0,2],[1,3],[1,4],[2,4]], start=0`

```
图的结构：
    0
   / \
  1   2
 / \ /
3   4

初始：dis = [-1, -1, -1, -1, -1], q = [0], dis[0] = 0

第 1 轮：弹出 0，邻居 1 和 2 未访问
  dis = [0, 1, 1, -1, -1], q = [1, 2]

第 2 轮：弹出 1，邻居 3 和 4 未访问
  dis = [0, 1, 1, 2, 2], q = [2, 3, 4]

第 3 轮：弹出 2，邻居 0 已访问，4 已访问 → 跳过
  dis = [0, 1, 1, 2, 2], q = [3, 4]

第 4 轮：弹出 3，邻居 1 已访问 → 跳过
第 5 轮：弹出 4，邻居 1 和 2 都已访问 → 跳过

最终结果：dis = [0, 1, 1, 2, 2]
```

### BFS 求最短路径的具体路径

如果需要输出具体路径而不只是距离，需要额外记录每个节点的前驱节点：

```python
def bfs_shortest_path_with_route(n, edges, start, end):
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    dis = [-1] * n
    prev = [-1] * n  # prev[x] 记录到达 x 的前驱节点
    dis[start] = 0
    q = deque([start])

    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:
                dis[y] = dis[x] + 1
                prev[y] = x  # 记录前驱
                q.append(y)

    if dis[end] < 0:
        return -1, []  # 不可达

    # 从 end 倒推回 start，再反转
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = prev[node]
    return dis[end], path[::-1]
```

---

## DFS（深度优先搜索）

### 核心思想

DFS 使用**递归**（或栈），从起点出发，沿着一条路径一直深入到底，无法继续时回溯，再尝试其他分支。像走迷宫一样，一条路走到黑，碰壁了再回头。

```
DFS 遍历顺序（从节点 0 出发）：
    0
   / \
  1   2
 / \   \
3   4   5

递归调用栈变化过程：
dfs(0) → dfs(1) → dfs(3) → 回溯 → dfs(4) → 回溯 → 回溯 → dfs(2) → dfs(5)

访问顺序：0, 1, 3, 4, 2, 5（前序遍历）
```

### BFS vs DFS 对比

| 特性 | BFS | DFS |
|------|-----|-----|
| 数据结构 | 队列（deque） | 递归栈（或手动栈） |
| 遍历方式 | 层序（一圈一圈扩散） | 深度（一条路走到底） |
| 最短路 | **天然支持**（无权图） | 不支持 |
| 适合场景 | 最短路、层序遍历、最小步数 | 连通性判断、拓扑排序、回溯搜索 |
| 空间复杂度 | O(n)（最坏时队列存所有节点） | O(n)（递归栈深度） |
| 代码模板 | `while q: x = q.popleft()` | `def dfs(x): for y in g[x]: dfs(y)` |

> **选 BFS 还是 DFS？**
> - 求最短路 / 最少步数 → BFS
> - 判断连通性 / 枚举所有路径 / 回溯 → DFS
> - 拓扑排序 → 两种都可以（BFS 用入度法，DFS 用后序遍历法）

### DFS 连通性判断

```python
def is_connected(n: int, edges: List[List[int]]) -> bool:
    """判断无向图是否连通（所有节点互相可达）"""
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    vis = [False] * n

    def dfs(x: int) -> None:
        vis[x] = True
        for y in g[x]:
            if not vis[y]:
                dfs(y)

    dfs(0)  # 从节点 0 出发
    return all(vis)  # 所有节点都被访问过 → 连通
```

---

## 网格图

**网格图是一种简化的图**：每个格子是一个顶点，相邻格子之间有边。默认是**无向无权图**。

### 为什么单独讲网格图？

网格图在实际算法题中出现频率极高（岛屿问题、迷宫问题、单词搜索等），但它的建图方式与一般图不同——不需要显式构建邻接表，**格子坐标本身就隐含了邻接关系**。

```
普通图：需要手动建邻接表
  g = [[] for _ in range(n)]
  for x, y in edges: g[x].append(y)

网格图：隐式建图（通过坐标偏移）
  (r, c) 的邻居是 (r-1,c), (r+1,c), (r,c-1), (r,c+1)
  不需要存储 edges，只需检查边界 + 条件
```

### 网格图 DFS vs 二叉树 DFS

| | 二叉树 | 网格图 |
|-----|-------|-------|
| 递归入口 | 根节点 | 网格图的某个格子 |
| 递归方向 | 左儿子和右儿子 | 一般为上下左右（4方向）或包含对角线（8方向） |
| 递归边界 | 空节点（`node is None`） | 出界、遇到障碍或已访问 |
| 标记已访问 | 不需要（树没有环） | **必须标记**（网格图可能有环） |

> **核心区别**：二叉树天然无环，不需要标记已访问；网格图需要防止重复访问（死循环）。

### 岛屿问题模板

[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

```python
def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0]) if grid else 0
    if rows == 0:
        return 0

    def dfs(r: int, c: int) -> None:
        # 递归边界：出界 + 不是陆地 + 已访问
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
            return
        grid[r][c] = '2'  # 标记为已访问（直接修改原数组，避免额外空间）
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

### 网格图常见变体

```python
# 四方向（上下左右，最常用）
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 八方向（包含对角线，如国际象棋）
directions_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# 使用示例
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        # 处理 (nr, nc)
```

### 网格图标记已访问的三种方式

```python
# 方式 1：直接修改原数组（最常用，省空间）
grid[r][c] = '2'  # 或 '0' 或 '#'

# 方式 2：使用 vis 数组（不修改原数组）
vis = [[False] * cols for _ in range(rows)]
vis[r][c] = True

# 方式 3：使用集合（适合稀疏访问）
visited = set()
visited.add((r, c))
```

> **方式 1 最常用**：因为它不需要额外空间，O(1) 标记。但如果原数组后续还需要使用，则用方式 2。

---

## 最短路径算法

### 如何选择最短路径算法？

```
边的权值有负数吗？
├── 是 → 有负环吗？
│       ├── 是 → Bellman-Ford / SPFA（检测负环）
│       └── 否 → Bellman-Ford / SPFA
└── 否 → 边权只有 0 和 1 吗？
        ├── 是 → 0-1 BFS（O(n + m)，比 Dijkstra 更快）
        └── 否 → Dijkstra（O((n + m) log m)，最常用）
```

### 各算法复杂度对比

| 算法 | 时间复杂度 | 适用条件 | 说明 |
|------|-----------|---------|------|
| BFS | O(n + m) | 无权图 | 最简单，面试首选 |
| 0-1 BFS | O(n + m) | 边权只有 0 和 1 | 用双端队列替代堆 |
| Dijkstra（堆优化） | O((n + m) log m) | 非负边权 | **最常用** |
| Bellman-Ford | O(n · m) | 允许负边权 | 可检测负环 |
| SPFA | O(n · m) 最坏 | 允许负边权 | Bellman-Ford 的队列优化 |
| Floyd | O(n³) | 多源最短路 | 任意两点间最短路 |

---

## Dijkstra 算法

### 适用条件

- **没有负数边权**（有负权边时结果不一定正确）
- 单源最短路（从一个起点到所有其他节点）

### 核心思想

**贪心**：每次选择距离起点**最近的未确定节点**，用该节点更新邻居的最短距离。

为什么贪心是对的？因为所有边权非负，一旦某个节点的最短距离确定了，就不可能通过其他更长的路径得到更短的距离。

```
类比：从北京出发，想找去各个城市的最短距离
1. 先确定最近的城市（比如天津），它的最短距离已经确定
2. 用天津去更新天津的邻居（比如唐山），因为通过天津到唐山可能是最短的
3. 再选择下一个最近的未确定城市，重复这个过程
```

### 堆优化 Dijkstra

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
    h = [(0, start)]  # (距离, 节点)，按距离排序的小顶堆

    while h:
        dx, x = heapq.heappop(h)  # 弹出距离最小的节点
        if dx > dis[x]:            # 已有更短的路径，跳过（关键！）
            continue
        for y, wt in g[x]:        # 用 x 更新所有邻居
            new_dis = dx + wt
            if new_dis < dis[y]:
                dis[y] = new_dis
                heapq.heappush(h, (new_dis, y))

    return dis
```

### 示例推演

**输入**：`n=5, edges=[[0,1,2],[0,2,5],[1,2,1],[1,3,4],[2,3,1],[2,4,3],[3,4,1]], start=0`

```
图的结构：
  0 --2-- 1 --4-- 3
  | 1/    | 1/    | 1\
  5       1       1
  |      /       |
  2 --3-- 4 ----+

初始：dis = [0, ∞, ∞, ∞, ∞], h = [(0, 0)]

第 1 轮：弹出 (0, 0)
  更新邻居：dis[1] = 0+2=2, dis[2] = 0+5=5
  h = [(2, 1), (5, 2)]

第 2 轮：弹出 (2, 1)
  更新邻居：
    1→2: new=2+1=3 < dis[2]=5 → dis[2]=3
    1→3: new=2+4=6 < dis[3]=∞ → dis[3]=6
  h = [(3, 2), (5, 2), (6, 3)]

第 3 轮：弹出 (3, 2)  ← 注意！堆里还有一个 (5,2)，弹出时 3 < 5 所以先弹这个
  更新邻居：
    2→3: new=3+1=4 < dis[3]=6 → dis[3]=4
    2→4: new=3+3=6 < dis[4]=∞ → dis[4]=6
  h = [(4, 3), (5, 2), (6, 3), (6, 4)]

第 4 轮：弹出 (4, 3)
  更新邻居：3→4: new=4+1=5 < dis[4]=6 → dis[4]=5
  h = [(5, 2), (5, 4), (6, 3), (6, 4)]

第 5 轮：弹出 (5, 2)
  检查：5 > dis[2]=3 → 跳过！（这就是 dx > dis[x] 的作用）

后续：弹出 (5, 4) 确定 4，弹出 (6, 3) 跳过（6 > dis[3]=4），弹出 (6, 4) 跳过

最终：dis = [0, 2, 3, 4, 5]
```

### 易错点：为什么需要 `if dx > dis[x]: continue`？

```python
# 同一个节点可能被多次加入堆（因为每次松弛都会 push）
# 例如：dis[2] 先被设为 5，后来更新为 3
# 堆里会有 (5, 2) 和 (3, 2) 两条记录
# 弹出 (3, 2) 时正常处理，弹出 (5, 2) 时应该跳过
if dx > dis[x]:  # 说明这个节点的最短路已经被其他路径确定了
    continue
```

> **面试技巧**：如果面试官问"同一个节点可能多次入堆吗？"，回答"是的，但通过 `dx > dis[x]` 跳过重复，不影响正确性，且每个节点最多被有效处理一次。"

### Dijkstra 为什么不能处理负权边？

```
反例：start=0
  0 --1-- 1 --(-5)-- 2
  |                  |
  +--------4---------+

正无穷 + (-5) < 正无穷，所以通过负权边可能找到更短的路径
但 Dijkstra 是贪心的，一旦确定节点 1 的最短路（距离 1），就不再回头
实际上 0→1→2→1 的路径可能比 0→1 更短，但 Dijkstra 已经"确定"了节点 1
```

---

## 0-1 BFS

### 什么时候用？

边权只有 **0 和 1** 时，可以用双端队列代替优先队列，将复杂度从 O((n+m) log m) 降到 O(n + m)。

### 核心思想

与 BFS 类似，但区别在于：
- 边权为 0 时，将新节点插入**队首**（因为距离没有增加，应该优先处理）
- 边权为 1 时，将新节点插入**队尾**（距离增加了 1，稍后处理）

```
类比：普通 BFS 就像排大队，所有人都是一步一步走
0-1 BFS 就像可以"传送"，走传送门（边权 0）不用排队，直接到队首
```

```python
from collections import deque

def zero_one_bfs(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    边权只有 0 和 1 的最短路
    edges 格式：[起点, 终点, 权重]，权重只能是 0 或 1
    时间复杂度 O(n + m)
    """
    g = [[] for _ in range(n)]
    for x, y, w in edges:
        g[x].append((y, w))

    dis = [-1] * n
    dis[start] = 0
    dq = deque([start])

    while dq:
        x = dq.popleft()
        for y, w in g[x]:
            new_dis = dis[x] + w
            if dis[y] < 0 or new_dis < dis[y]:
                dis[y] = new_dis
                if w == 0:
                    dq.appendleft(y)  # 边权为 0，放队首（优先处理）
                else:
                    dq.append(y)       # 边权为 1，放队尾
    return dis
```

### 为什么 0-1 BFS 能替代 Dijkstra？

在 Dijkstra 中，优先队列保证每次弹出最小距离节点。在 0-1 BFS 中：
- 队首的节点距离 ≤ 队尾的节点距离（队首差值为 0，队尾差值为 1）
- 双端队列天然维护了这个单调性，不需要 log 的堆操作

---

## 拓扑排序

### 什么是拓扑排序？

**拓扑排序是对有向无环图（DAG）中所有节点的一种线性排序**，使得对于图中的每一条边 `u → v`，在排序中 `u` 都排在 `v` 的前面。

```
现实例子：课程依赖
  数学 → 线代
  高数 → 线代
  高数 → 概率

拓扑序之一：[数学, 高数, 线代, 概率] 或 [高数, 数学, 线代, 概率]
（必须满足：数学在线代前面，高数在线代和概率前面）
```

> **关键**：只有**有向无环图（DAG）**才有拓扑排序。如果图中有环，说明存在循环依赖（A 依赖 B，B 依赖 A），无法排出顺序。

### 适用条件

- 图必须是**有向图**
- 图必须**没有环**（DAG）

### 两种实现方式

#### 方法 1：BFS + 入度表（Kahn 算法，推荐）

**核心思想**：不断找到入度为 0 的节点（没有任何前置依赖），加入结果，然后删除该节点并更新邻居的入度。

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
        in_deg[y] += 1  # y 的入度 +1

    topo_order = []
    q = deque([i for i, d in enumerate(in_deg) if d == 0])  # 入度为 0 的节点入队

    while q:
        x = q.popleft()
        topo_order.append(x)
        for y in g[x]:
            in_deg[y] -= 1  # 删除 x 后，y 的入度 -1
            if in_deg[y] == 0:
                q.append(y)

    return topo_order if len(topo_order) == n else []
```

#### 示例推演

**输入**：`n=6, edges=[[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]`

```
图的结构：
  5 → 2 → 3 → 1
  ↓         ↑
  0 ← 4 → 1

初始入度：in_deg = [2, 2, 1, 1, 0, 0]
  节点 0：被 5 和 4 指向 → 入度 2
  节点 1：被 4 和 3 指向 → 入度 2
  节点 2：被 5 指向 → 入度 1
  节点 3：被 2 指向 → 入度 1
  节点 4：无入边 → 入度 0
  节点 5：无入边 → 入度 0

初始队列：q = [4, 5]

第 1 轮：弹出 4
  topo = [4]
  4→0: in_deg[0] = 2-1 = 1
  4→1: in_deg[1] = 2-1 = 1
  q = [5]

第 2 轮：弹出 5
  topo = [4, 5]
  5→2: in_deg[2] = 1-1 = 0 → 入队
  5→0: in_deg[0] = 1-1 = 0 → 入队
  q = [2, 0]

第 3 轮：弹出 2
  topo = [4, 5, 2]
  2→3: in_deg[3] = 1-1 = 0 → 入队
  q = [0, 3]

第 4 轮：弹出 0
  topo = [4, 5, 2, 0]
  0 没有出边
  q = [3]

第 5 轮：弹出 3
  topo = [4, 5, 2, 0, 3]
  3→1: in_deg[1] = 1-1 = 0 → 入队
  q = [1]

第 6 轮：弹出 1
  topo = [4, 5, 2, 0, 3, 1]
  1 没有出边
  q = []

len(topo) == 6 == n → 无环，返回 [4, 5, 2, 0, 3, 1]
```

#### 方法 2：DFS + 后序遍历

```python
def topological_sort_dfs(n: int, edges: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)

    vis = [0] * n  # 0=未访问, 1=访问中, 2=已完成
    order = []

    def dfs(x: int) -> bool:
        vis[x] = 1  # 标记为"正在访问"
        for y in g[x]:
            if vis[y] == 1:
                return False  # 遇到"正在访问"的节点 → 有环！
            if vis[y] == 0 and not dfs(y):
                return False
        vis[x] = 2
        order.append(x)  # 后序：所有邻居处理完后再加入
        return True

    for i in range(n):
        if vis[i] == 0:
            if not dfs(i):
                return []  # 有环

    return order[::-1]  # 反转得到拓扑序
```

> **DFS 方法理解**：DFS 的后序遍历天然保证了"被依赖的节点排在前面"。例如 `A→B→C`，DFS 访问顺序是 A→B→C，后序加入顺序是 [C, B, A]，反转得到 [A, B, C]，这就是正确的拓扑序。

### 拓扑排序的经典应用

#### 1. 课程表问题

[207. 课程表](https://leetcode.cn/problems/course-schedule/)

```python
# 判断能否完成所有课程（即判断有向图是否有环）
def canFinish(n, prerequisites):
    # 构建有向图
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in prerequisites:
        g[x].append(y)
        in_deg[y] += 1

    q = deque([i for i in range(n) if in_deg[i] == 0])
    count = 0
    while q:
        x = q.popleft()
        count += 1
        for y in g[x]:
            in_deg[y] -= 1
            if in_deg[y] == 0:
                q.append(y)
    return count == n  # 所有课程都能完成 ↔ 无环
```

#### 2. 拓扑排序 + DP（求最长路径）

在 DAG 上求最长路径（如最长课程链），先拓扑排序，再按拓扑序 DP：

```python
def longest_path_in_dag(n, edges):
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in edges:
        g[x].append(y)
        in_deg[y] += 1

    q = deque([i for i in range(n) if in_deg[i] == 0])
    dp = [1] * n  # dp[x] = 以 x 结尾的最长路径长度

    while q:
        x = q.popleft()
        for y in g[x]:
            dp[y] = max(dp[y], dp[x] + 1)  # 拓扑序保证了 dp[x] 已计算完毕
            in_deg[y] -= 1
            if in_deg[y] == 0:
                q.append(y)

    return max(dp)
```

---

## 连通分量

### 什么是连通分量？

无向图中，**互相可达的节点组成的最大集合**称为一个连通分量。连通分量之间没有任何边相连。

```
图中有 3 个连通分量：
  0-1-2    3-4    5

连通分量 1: {0, 1, 2}
连通分量 2: {3, 4}
连通分量 3: {5}
```

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
        size = 1  # 当前节点算 1 个
        for y in g[x]:
            if not vis[y]:
                size += dfs(y)  # 累加子树大小
        return size

    ans = []
    for i in range(n):
        if not vis[i]:
            ans.append(dfs(i))  # 每个未访问的节点都是一个新连通块的起点
    return ans  # 返回每个连通块的大小
```

> **与岛屿问题的关系**：岛屿数量本质上就是在网格图上数连通分量。岛屿面积就是连通块大小。

---

## 环检测

### 无向图环检测

使用 DFS，如果遇到一个**已访问且不是父节点**的邻居，说明有环：

```python
def has_cycle_undirected(n, edges):
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    vis = [False] * n

    def dfs(x, parent):
        vis[x] = True
        for y in g[x]:
            if not vis[y]:
                if dfs(y, x):
                    return True
            elif y != parent:  # 已访问且不是父节点 → 有环
                return True
        return False

    for i in range(n):
        if not vis[i]:
            if dfs(i, -1):
                return True
    return False
```

### 有向图环检测

见上方"拓扑排序"部分——如果拓扑排序的结果长度 < n，说明有环。或者用 DFS 的三色标记法。

---

## 易错点总结

### 1. 无向图忘记双向添加边

```python
# ❌ 最常见的错误
g[x].append(y)  # 漏了 g[y].append(x)

# ✅ 无向图必须双向添加
g[x].append(y)
g[y].append(x)
```

### 2. 图的节点编号不一定是 0 到 n-1

```python
# 有些题目的节点编号是 1 到 n，或者任意整数
# 用字典代替列表来存储邻接表
g = defaultdict(list)
for x, y in edges:
    g[x].append(y)
    g[y].append(x)
```

### 3. BFS 用 list 当队列导致 O(n²)

```python
# ❌ 慢：list.pop(0) 是 O(n)
q = [start]
x = q.pop(0)

# ✅ 快：deque.popleft() 是 O(1)
from collections import deque
q = deque([start])
x = q.popleft()
```

### 4. 网格图忘记标记已访问导致死循环

```python
# ❌ 忘记标记 → 无限递归 / 死循环
def dfs(r, c):
    for nr, nc in directions:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
            dfs(nr, nc)  # 没有标记已访问！(nr,nc) 会被重复访问

# ✅ 先标记再递归
def dfs(r, c):
    grid[r][c] = '2'  # 先标记
    for nr, nc in directions:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
            dfs(nr, nc)
```

### 5. Dijkstra 在有负权边时给出错误结果

Dijkstra 的贪心策略依赖"边权非负"。如果存在负权边，可能过早"确定"某个节点的最短距离。

### 6. 拓扑排序忘记检查是否有环

```python
# ❌ 直接返回 topo_order，不管是否有环
return topo_order

# ✅ 检查长度
return topo_order if len(topo_order) == n else []
```

---

## 相关题目

### BFS
- [1091. 二进制矩阵中的最短路径](https://leetcode.cn/problems/shortest-path-in-binary-matrix/)
- [752. 打开转盘锁](https://leetcode.cn/problems/open-the-lock/)
- [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/)

### DFS / 网格图
- [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- [695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)
- [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)
- [79. 单词搜索](https://leetcode.cn/problems/word-search/)

### 最短路径
- [743. 网络延迟时间](https://leetcode.cn/problems/network-delay-time/)（Dijkstra）
- [787. K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/)（Dijkstra + 限制步数）
- [1514. 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)

### 拓扑排序
- [207. 课程表](https://leetcode.cn/problems/course-schedule/)
- [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)
- [1136. 并行课程](https://leetcode.cn/problems/parallel-courses/)

### 连通分量
- [323. 无向图中连通分量的数目](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)
- [547. 省份数量](https://leetcode.cn/problems/number-of-provinces/)
