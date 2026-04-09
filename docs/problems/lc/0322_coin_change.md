---
title: 零钱兑换
platform: LeetCode
difficulty: Medium
id: 322
url: https://leetcode.cn/problems/coin-change/
tags:
  - 动态规划
  - 完全背包
  - 记忆化搜索
date_added: 2026-04-09
---

# 322. 零钱兑换

## 题目描述

给你一个整数数组 `coins`，表示不同面额的硬币；以及一个整数 `amount`，表示总金额。

计算并返回可以凑成总金额所需的**最少的硬币个数**。如果没有任何一种硬币组合能组成总金额，返回 `-1`。

你可以认为每种硬币的数量是无限的。

**示例 1：**

```
输入：coins = [1,2,5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0
```

**提示：**
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**完全背包**问题：
- **物品**：硬币，每种硬币可以无限次使用
- **背包容量**：amount
- **目标**：用最少的物品（硬币）填满背包

与 01 背包的区别：每种硬币可以选多次。

### 第二步：暴力解法 - 回溯

枚举所有可能的组合，记录使用硬币数最少的方案。

```python
from math import inf

def coinChange_brute(coins, amount):
    coins.sort(reverse=True)
    res = inf

    def dfs(start, count, remaining):
        nonlocal res
        if remaining < 0:
            return
        if count >= res:  # 剪枝
            return
        if remaining == 0:
            res = min(res, count)
            return
        for i in range(start, len(coins)):
            dfs(i, count + 1, remaining - coins[i])

    dfs(0, 0, amount)
    return -1 if res == inf else int(res)
```

**为什么不够好？**
- 时间复杂度指数级，会超时
- 本质是回溯，没有利用子问题的重叠性质

### 第三步：优化解法 - 记忆化搜索

定义 `dfs(i, c)`：从前 i 种硬币中选，组成金额 c 的最少硬币数。

**状态转移：**
```
dfs(i, c) = min(
    dfs(i-1, c),           # 不选第 i 种硬币
    dfs(i, c-coins[i]) + 1  # 选第 i 种硬币（可以重复选）
)
```

使用 `@cache` 避免重复计算。

### 第四步：最优解法 - 完全背包 DP

使用自底向上的动态规划。

**定义：** `f[c]` 表示组成金额 c 所需的最少硬币数

**初始化：**
- `f[0] = 0`（组成 0 需要 0 个硬币）
- `f[1..amount] = inf`（初始不可达）

**状态转移：**
```
对于每种硬币 coin:
    对于每个金额 cur 从 coin 到 amount:
        f[cur] = min(f[cur], f[cur-coin] + 1)
```

**为什么外层循环是硬币？**
- 确保每种硬币可以被重复使用
- 如果外层是金额，内层是硬币，会变成排列问题（顺序不同算不同方案）

---

## 完整代码实现

```python
from typing import List
from math import inf
from functools import cache


class Solution:
    """
    322. 零钱兑换 - 完全背包问题

    问题本质：
    给定不同面额的硬币 coins 和总金额 amount，求组成该金额所需的最少硬币个数。
    每个硬币可以无限次使用，这是一个经典的"完全背包"问题。

    解法一：记忆化搜索（自顶向下）
    - 定义 dfs(i, c)：从前 i 种硬币中选，组成金额 c 的最少硬币数
    - 状态转移：min(不选 coin[i], 选 coin[i] + 1)
    - 使用 @cache 避免重复计算
    - 缺点：递归有额外开销，缓存访问不连续

    解法二：动态规划/完全背包（自底向上）
    - f[c] 表示组成金额 c 所需的最少硬币数
    - 初始化：f[0] = 0, f[1..amount] = inf
    - 转移：对于每种硬币，遍历所有可以组成的金额
            f[cur] = min(f[cur], f[cur - coin] + 1)
    - 外层循环硬币，内层循环金额（完全背包的标准写法）

    为什么外层循环是硬币？
    - 确保每种硬币可以被重复使用
    - 如果外层是金额，内层是硬币，会超时（变成排列问题）

    时间复杂度: O(n * amount) - n 为硬币种类数
    空间复杂度: O(amount) - DP 数组空间
    """

    # 解法一：记忆化搜索
    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        """
        记忆化搜索解法
        dfs(i, c) 表示从前 i 种硬币中选，组成金额 c 的最少硬币数
        """
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                # 没有硬币可选，只有金额为 0 时才可行
                return 0 if c == 0 else inf
            if c < coins[i]:
                # 当前硬币面值太大，只能不选
                return dfs(i - 1, c)
            # 状态转移：不选当前硬币 vs 选当前硬币（可以继续选，所以是 dfs(i, ...)）
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

    # 解法二：完全背包（最优解法）
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        完全背包动态规划解法
        f[c] 表示组成金额 c 所需的最少硬币数
        """
        # 初始化：f[0] = 0（组成金额 0 需要 0 个硬币）
        # 其余初始化为无穷大，表示暂时不可达
        f = [0] + [inf] * amount

        # 外层循环：每种硬币
        for coin in coins:
            # 内层循环：从 coin 到 amount
            # 从 coin 开始是因为更小的金额无法使用该硬币
            for cur in range(coin, amount + 1):
                # 状态转移：不使用当前硬币 vs 使用当前硬币（数量 +1）
                f[cur] = min(f[cur], f[cur - coin] + 1)

        ans = f[amount]
        return ans if ans < inf else -1
```

---

## 示例推演

以 `coins = [1, 2, 5], amount = 11` 为例：

**初始化：** `f = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]`

**coin = 1：**
```
cur=1:  f[1] = min(inf, f[0]+1) = 1
cur=2:  f[2] = min(inf, f[1]+1) = 2
cur=3:  f[3] = min(inf, f[2]+1) = 3
...
cur=11: f[11] = 11
```

**coin = 2：**
```
cur=2:  f[2] = min(2, f[0]+1) = 1      # 2 = 2
cur=3:  f[3] = min(3, f[1]+1) = 2      # 3 = 2 + 1
cur=4:  f[4] = min(4, f[2]+1) = 2      # 4 = 2 + 2
cur=5:  f[5] = min(5, f[3]+1) = 3      # 5 = 2 + 2 + 1
...
cur=11: f[11] = min(11, f[9]+1) = 6    # 11 = 2*5 + 1
```

**coin = 5：**
```
cur=5:  f[5] = min(3, f[0]+1) = 1      # 5 = 5
cur=6:  f[6] = min(3, f[1]+1) = 2      # 6 = 5 + 1
cur=7:  f[7] = min(4, f[2]+1) = 2      # 7 = 5 + 2
cur=8:  f[8] = min(4, f[3]+1) = 3      # 8 = 5 + 2 + 1
cur=9:  f[9] = min(5, f[4]+1) = 3      # 9 = 5 + 2 + 2
cur=10: f[10] = min(5, f[5]+1) = 2     # 10 = 5 + 5
cur=11: f[11] = min(6, f[6]+1) = 3     # 11 = 5 + 5 + 1
```

**最终结果：** `f[11] = 3`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 回溯 | O(amount^n) | O(n) | 指数级，超时 |
| 记忆化搜索 | O(n * amount) | O(n * amount) | 递归 + 缓存 |
| 完全背包 DP | O(n * amount) | O(amount) | 最优解法 |

---

## 易错点总结

### 1. 完全背包 vs 01 背包

**错误做法（01 背包）：**
```python
for coin in coins:
    for cur in range(amount, coin - 1, -1):  # 倒序
        f[cur] = min(f[cur], f[cur - coin] + 1)
```

**正确做法（完全背包）：**
```python
for coin in coins:
    for cur in range(coin, amount + 1):  # 正序，可以重复选
        f[cur] = min(f[cur], f[cur - coin] + 1)
```

### 2. 初始化值

```python
f = [0] + [inf] * amount  # f[0] = 0，其余为无穷大
```

**错误做法：**
```python
f = [inf] * (amount + 1)  # 错误！f[0] 应该是 0
```

### 3. 无解情况

```python
ans = f[amount]
return ans if ans < inf else -1  # 注意返回 -1
```

### 4. 循环顺序

外层循环硬币，内层循环金额：
```python
for coin in coins:              # 硬币
    for cur in range(coin, amount + 1):  # 金额
        f[cur] = min(f[cur], f[cur - coin] + 1)
```

如果反过来，会变成排列问题（顺序不同算不同方案）。

---

## 扩展思考

### 1. 相关题目

- [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/) - 求方案数
- [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/) - 完全背包
- [377. 组合总和 IV](https://leetcode.cn/problems/combination-sum-iv/) - 排列问题

### 2. 零钱兑换 II（求方案数）

```python
def change(amount: int, coins: List[int]) -> int:
    f = [1] + [0] * amount
    for coin in coins:
        for cur in range(coin, amount + 1):
            f[cur] += f[cur - coin]
    return f[amount]
```

注意：
- 初始化 `f[0] = 1`（组成金额 0 有 1 种方案：什么都不选）
- 状态转移用加法而非取最小值

### 3. 输出具体方案

使用回溯记录路径：

```python
def coinChange_with_path(coins, amount):
    f = [0] + [inf] * amount
    parent = [-1] * (amount + 1)  # 记录用了哪个硬币

    for coin in coins:
        for cur in range(coin, amount + 1):
            if f[cur - coin] + 1 < f[cur]:
                f[cur] = f[cur - coin] + 1
                parent[cur] = coin

    if f[amount] == inf:
        return -1, []

    # 重建路径
    path = []
    cur = amount
    while cur > 0:
        path.append(parent[cur])
        cur -= parent[cur]

    return f[amount], path
```

### 4. 空间优化

当前解法已经是最优空间复杂度 O(amount)。

如果 amount 很大但硬币种类很少，可以考虑使用 BFS 或 Dijkstra 算法。
