---
title: 课程表
platform: LeetCode
difficulty: Medium
id: 207
url: https://leetcode.cn/problems/course-schedule/
tags:
  - 深度优先搜索
  - 广度优先搜索
  - 图
  - 拓扑排序
topics:
  - ../../topics/graph.md
  - ../../topics/topological-sort.md
patterns:
  - ../../patterns/graph-cycle-detection.md
date_added: 2026-04-09
date_reviewed: []
---

# 207. 课程表

## 题目描述

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses-1`。

在选修某些课程之前需要一些先修课程。先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]`，表示如果要学习课程 `ai` 则必须先学习课程 `bi`。

请你判断是否可能完成所有课程的学习？

## 示例

**示例 1：**
```
输入: numCourses = 2, prerequisites = [[1,0]]
输出: true
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。这是可能的。
```

**示例 2：**
```
输入: numCourses = 2, prerequisites = [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0；并且要学习课程 0，你还需要先完成课程 1。这是不可能的。
```

---

## 解题思路

### 第一步：理解问题本质

本题本质是**判断有向图中是否存在环**：
- 课程作为节点
- 先修关系作为有向边（`bi -> ai` 表示必须先学 `bi` 才能学 `ai`）
- 如果能完成所有课程，说明图中无环（存在拓扑排序）

### 第二步：暴力解法 - 暴力枚举

枚举所有可能的课程学习顺序，检查是否满足先修要求。

**为什么不够好**：时间复杂度 O(n!)，不可行。

### 第三步：优化解法 - DFS + 三色标记法

使用 DFS 遍历图，用三种颜色标记节点状态：
- **0（白色）**：未访问
- **1（灰色）**：正在访问中（在当前 DFS 路径上）
- **2（黑色）**：已访问完毕

如果发现指向灰色节点的边，说明存在后向边，即存在环。

### 第四步：最优解法 - 拓扑排序

两种实现方式：
1. **DFS 版**：上述三色标记法
2. **Kahn 算法（BFS）**：不断移除入度为 0 的节点

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    课程表 - 拓扑排序（DFS判环）

    核心思路：
    本题本质上是判断有向图中是否存在环。
    使用三色标记法进行 DFS：
    - 0（白色）：未访问
    - 1（灰色）：正在访问中
    - 2（黑色）：已访问完毕

    时间复杂度：O(V + E)
    空间复杂度：O(V + E)
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建邻接表
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)  # b -> a 的边

        colors = [0] * numCourses  # 0: 未访问, 1: 访问中, 2: 已访问

        def dfs(x: int) -> bool:
            """返回 True 表示找到了环"""
            colors[x] = 1  # 标记为访问中

            for y in g[x]:
                if colors[y] == 1:  # 发现指向访问中节点的边，有环
                    return True
                if colors[y] == 0 and dfs(y):  # 未访问，递归检查
                    return True

            colors[x] = 2  # 标记为已访问完毕
            return False

        for i in range(numCourses):
            if colors[i] == 0 and dfs(i):
                return False  # 有环

        return True  # 无环
```

---

## 示例推演

以 `numCourses = 4, prerequisites = [[1,0],[2,1],[3,2]]` 为例：

**构建图**：
```
0 -> 1 -> 2 -> 3
```

**DFS 过程**：

| 步骤 | 操作 | colors | 说明 |
|------|------|--------|------|
| 初始 | - | [0,0,0,0] | 全部未访问 |
| 1 | dfs(0) | [1,0,0,0] | 访问 0 |
| 2 | dfs(1) | [1,1,0,0] | 从 0 到 1 |
| 3 | dfs(2) | [1,1,1,0] | 从 1 到 2 |
| 4 | dfs(3) | [1,1,1,1] | 从 2 到 3 |
| 5 | 3 无邻居 | [1,1,1,2] | 3 访问完毕 |
| 6 | 返回 2 | [1,1,2,2] | 2 访问完毕 |
| 7 | 返回 1 | [1,2,2,2] | 1 访问完毕 |
| 8 | 返回 0 | [2,2,2,2] | 0 访问完毕 |

无环，返回 `True`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力枚举 | O(n!) | O(n) | 不可行 |
| DFS 三色标记 | O(V + E) | O(V + E) | V 为节点数，E 为边数 |
| Kahn 算法 | O(V + E) | O(V + E) | BFS 版本 |

---

## 易错点总结

### 1. 建图方向错误

**错误**：`g[a].append(b)`

**正确**：`g[b].append(a)`（b 是 a 的先修课程，边从 b 指向 a）

### 2. 三色标记判断条件

```python
# 正确：先判断是否为灰色（环），再递归判断白色
if colors[y] == 1 or (colors[y] == 0 and dfs(y)):
    return True
```

### 3. 孤立节点处理

```python
# 必须遍历所有节点，因为可能有孤立节点
for i in range(numCourses):
    if colors[i] == 0 and dfs(i):
        return False
```

---

## 扩展思考

### 1. 如何输出一个合法的学习顺序？

[210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)：输出拓扑排序序列。

在 DFS 中，当节点标记为黑色时，将其加入结果列表（逆序）。

### 2. 如何找到所有可能的顺序？

需要记录所有拓扑排序，可以使用回溯法。

### 3. 相关题目

- [207. 课程表](https://leetcode.cn/problems/course-schedule/) - 判断是否能完成
- [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/) - 输出学习顺序
- [630. 课程表 III](https://leetcode.cn/problems/course-schedule-iii/) - 带时间的课程安排

---

## 相关题目

- [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)
- [630. 课程表 III](https://leetcode.cn/problems/course-schedule-iii/)
- [802. 找到最终的安全状态](https://leetcode.cn/problems/find-eventual-safe-states/)
