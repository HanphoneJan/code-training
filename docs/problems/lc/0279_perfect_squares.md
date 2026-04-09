---
title: 完全平方数
platform: LeetCode
difficulty: Medium
id: 279
url: https://leetcode.cn/problems/perfect-squares/
tags:
  - 动态规划
  - 数学
  - 完全背包
date_added: 2026-04-09
---

# 279. 完全平方数

## 题目描述

给你一个整数 `n`，返回和为 `n` 的完全平方数的最少数量。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

**示例 1：**

```
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4
```

**示例 2：**

```
输入: n = 13
输出: 2
解释: 13 = 4 + 9
```

**提示：**
- `1 <= n <= 10^4`

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的"完全背包"问题：
- 物品：完全平方数 1, 4, 9, 16, 25, ...（无限个）
- 背包容量：n
- 目标：用最少的物品填满背包

### 第二步：暴力解法 - BFS

将问题看作在图上求最短路径：从 0 开始，每次加一个完全平方数，求到达 n 的最少步数。

```python
from collections import deque

def numSquares_bfs(n):
    squares = [i * i for i in range(1, int(n**0.5) + 1)]
    queue = deque([(0, 0)])  # (当前和, 步数)
    visited = {0}
    
    while queue:
        cur, steps = queue.popleft()
        for sq in squares:
            nxt = cur + sq
            if nxt == n:
                return steps + 1
            if nxt < n and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, steps + 1))
    return -1
```

**为什么不够好？**
- 时间复杂度高，需要遍历大量状态
- 空间复杂度也高，需要存储 visited 集合

### 第三步：优化解法 - 记忆化搜索

定义 `dfs(i, j)`：从前 i 个完全平方数中选，组成和为 j 的最少个数。

**状态转移：**
- 不选第 i 个完全平方数：`dfs(i-1, j)`
- 选第 i 个完全平方数：`dfs(i, j - i*i) + 1`（可以重复选，所以第一个参数还是 i）

```python
from functools import cache
from math import inf, isqrt

@cache
def dfs(i, j):
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)

def numSquares(n):
    return dfs(isqrt(n), n)
```

**复杂度分析：**
- 时间复杂度 O(n * sqrt(n)) - 状态数为 sqrt(n) * n
- 空间复杂度 O(n * sqrt(n)) - 递归栈和缓存空间

### 第四步：最优解法 - 完全背包 DP

使用自底向上的动态规划，避免递归开销。

**定义：** `f[j]` 表示组成和为 j 的最少完全平方数个数

**初始化：**
- `f[0] = 0`（组成 0 需要 0 个数）
- `f[1..n] = inf`（初始不可达）

**状态转移：**
对于每个完全平方数 `i*i`，更新所有 `j >= i*i`：
```
f[j] = min(f[j], f[j - i*i] + 1)
```

---

## 完整代码实现

```python
from functools import cache
from math import inf, isqrt


# 写在外面，多个测试数据之间可以共享，减少计算量
@cache
def dfs(i: int, j: int) -> int:
    """
    记忆化搜索：从前 i 个完全平方数中选择，组成和为 j 的最少个数
    i: 考虑前 i 个完全平方数 (1^2, 2^2, ..., i^2)
    j: 目标和
    返回: 最少需要的完全平方数个数
    """
    if i == 0:
        return inf if j else 0
    if j < i * i:
        # 当前完全平方数 i^2 太大，只能不选
        return dfs(i - 1, j)
    # 状态转移：不选 i^2 vs 选 i^2（选的话可以继续选，所以是 dfs(i, ...)）
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)


class Solution:
    """
    279. 完全平方数 - 动态规划/记忆化搜索

    问题本质：
    给定 n，求最少的完全平方数个数，使得它们的和等于 n。
    这是一个经典的"完全背包"问题。

    解法一：记忆化搜索（自顶向下）
    - 定义 dfs(i, j)：从前 i 个完全平方数中选，组成和为 j 的最少个数
    - 状态转移：min(不选 i^2, 选 i^2 + 1)
    - 使用 @cache 避免重复计算

    解法二：递推/完全背包（自底向上）
    - f[j] 表示组成和为 j 的最少完全平方数个数
    - 初始化：f[0] = 0, f[1..n] = inf
    - 转移：f[j] = min(f[j], f[j - i*i] + 1) 对于所有 i*i <= j

    数学定理（拉格朗日四平方和定理）：
    每个正整数都可以表示为最多 4 个完全平方数的和。
    因此答案只可能是 1, 2, 3, 4。

    时间复杂度: O(n * sqrt(n))
    空间复杂度: O(n)
    """

    def numSquares(self, n: int) -> int:
        """使用记忆化搜索求解"""
        return dfs(isqrt(n), n)
```

**完全背包递推版本：**

```python
class Solution:
    def numSquares(self, n: int) -> int:
        """完全背包 DP 解法"""
        f = [0] + [inf] * n
        
        # 外层循环：每种完全平方数
        for i in range(1, isqrt(n) + 1):
            sq = i * i
            # 内层循环：从 sq 到 n
            for j in range(sq, n + 1):
                f[j] = min(f[j], f[j - sq] + 1)
        
        return f[n]
```

---

## 示例推演

以 `n = 12` 为例：

完全平方数：1, 4, 9

**DP 数组初始化：** `f = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]`

**i = 1, sq = 1：**
```
j = 1:  f[1] = min(inf, f[0] + 1) = 1
j = 2:  f[2] = min(inf, f[1] + 1) = 2
j = 3:  f[3] = min(inf, f[2] + 1) = 3
...
j = 12: f[12] = min(inf, f[11] + 1) = 12
```

**i = 2, sq = 4：**
```
j = 4:  f[4] = min(4, f[0] + 1) = 1      # 12 = 4
j = 5:  f[5] = min(5, f[1] + 1) = 2      # 5 = 4 + 1
j = 6:  f[6] = min(6, f[2] + 1) = 3      # 6 = 4 + 1 + 1
j = 7:  f[7] = min(7, f[3] + 1) = 4      # 7 = 4 + 1 + 1 + 1
j = 8:  f[8] = min(8, f[4] + 1) = 2      # 8 = 4 + 4
...
j = 12: f[12] = min(12, f[8] + 1) = 3    # 12 = 4 + 4 + 4
```

**i = 3, sq = 9：**
```
j = 9:  f[9] = min(9, f[0] + 1) = 1      # 9 = 9
j = 10: f[10] = min(6, f[1] + 1) = 2     # 10 = 9 + 1
j = 11: f[11] = min(7, f[2] + 1) = 3     # 11 = 9 + 1 + 1
j = 12: f[12] = min(3, f[3] + 1) = 3     # 12 = 4 + 4 + 4（不变）
```

**最终结果：** `f[12] = 3`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| BFS | O(n * sqrt(n)) | O(n) | 图搜索，需要 visited 集合 |
| 记忆化搜索 | O(n * sqrt(n)) | O(n * sqrt(n)) | 递归 + 缓存 |
| 完全背包 DP | O(n * sqrt(n)) | O(n) | 自底向上，最优 |

---

## 易错点总结

### 1. 完全背包 vs 01 背包

**错误做法（01 背包）：**
```python
for i in range(1, isqrt(n) + 1):
    for j in range(n, i*i - 1, -1):  # 倒序
        f[j] = min(f[j], f[j - i*i] + 1)
```

**正确做法（完全背包）：**
```python
for i in range(1, isqrt(n) + 1):
    for j in range(i*i, n + 1):  # 正序，可以重复选
        f[j] = min(f[j], f[j - i*i] + 1)
```

### 2. 初始化值

```python
f = [0] + [inf] * n  # f[0] = 0，其余为无穷大
```

### 3. 循环顺序

外层循环是完全平方数，内层循环是目标值：
```python
for i in range(1, isqrt(n) + 1):      # 完全平方数
    for j in range(i*i, n + 1):        # 目标值
        f[j] = min(f[j], f[j - i*i] + 1)
```

---

## 扩展思考

### 1. 数学定理 - 拉格朗日四平方和定理

**定理内容：** 每个正整数都可以表示为最多 4 个完全平方数的和。

**推论：** 这道题的答案只可能是 1, 2, 3, 4。

**判断方法：**
- 答案为 1：n 是完全平方数
- 答案为 4：n = 4^a * (8b + 7) 的形式
- 答案为 2：n 可以表示为两个完全平方数之和
- 否则答案为 3

### 2. 相关题目

- [322. 零钱兑换](https://leetcode.cn/problems/coin-change/) - 完全背包模板题
- [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/) - 求方案数
- [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/) - 完全背包

### 3. 预处理优化

如果多次查询，可以预处理所有答案：

```python
N = 10000
f = [0] + [inf] * N
for i in range(1, isqrt(N) + 1):
    for j in range(i * i, N + 1):
        f[j] = min(f[j], f[j - i * i] + 1)

class Solution:
    def numSquares(self, n: int) -> int:
        return f[n]
```
