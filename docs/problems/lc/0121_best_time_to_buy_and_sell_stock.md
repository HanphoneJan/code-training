---
title: 买卖股票的最佳时机
platform: LeetCode
difficulty: 简单
id: 121
url: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
tags:
  - 数组
  - 贪心
  - 动态规划
topics:
  - ../../topics/array.md
  - ../../topics/greedy.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../topics/dynamic_programming.md
date_added: 2026-04-03
date_reviewed: []
---

# 0121. 买卖股票的最佳时机

## 题目描述

给定一个数组 `prices`，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0`。

## 示例

**示例 1：**
```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5
```

**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成，所以最大利润为 0
```

---

## 解题思路

### 第一步：理解问题本质

目标是在最低点买入，最高点卖出（且卖出必须在买入之后）。

对于第 `i` 天，如果我在这一天卖出，那么最优的买入日一定是 `[0, i-1]` 中价格最低的那一天。

### 第二步：暴力解法

枚举所有「买入日 + 卖出日」的组合：

```python
def maxProfit(prices):
    n = len(prices)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, prices[j] - prices[i])
    return ans
```

- 时间复杂度：`O(n²)`
- 空间复杂度：`O(1)`

### 第三步：优化解法

既然对于每一天 `i`，我们只需要知道 `[0, i-1]` 的最小值，那可以一边遍历一边维护这个最小值。

```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    ans = 0
    pre_min = prices[0]
    for i in range(1, n):
        ans = max(ans, prices[i] - pre_min)
        pre_min = min(pre_min, prices[i])
    return ans
```

### 第四步：最优解法

上面的贪心解法已经是 optimal 了，时间复杂度 `O(n)`，空间复杂度 `O(1)`。

也可以理解为动态规划：
- `dp[i]` 表示前 `i` 天的最大利润
- `dp[i] = max(dp[i-1], prices[i] - pre_min)`

但本质上和贪心是一样的。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    121. 买卖股票的最佳时机 - 贪心/动态规划

    核心思想：
    遍历数组时，维护一个 "历史最低价格"，并计算 "今天卖出" 能获利的最大值。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        ans = 0
        pre_min = prices[0]

        for i in range(n):
            if prices[i] > pre_min:
                ans = max(ans, prices[i] - pre_min)
            else:
                pre_min = min(pre_min, prices[i])

        return ans
```

---

## 示例推演

以 `prices = [7, 1, 5, 3, 6, 4]` 为例：

| 天数 | 价格 | pre_min | 当天利润 | ans |
|------|------|---------|---------|-----|
| 0 | 7 | 7 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 5 | 1 | 4 | 4 |
| 3 | 3 | 1 | 2 | 4 |
| 4 | 6 | 1 | 5 | 5 |
| 5 | 4 | 1 | 3 | 5 |

最终答案：`5`（第 1 天买入价格 1，第 4 天卖出价格 6）

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 枚举所有买卖组合 |
| 贪心 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 利润不能为负

如果没有利润，必须返回 `0`（不能亏钱买入）。

### 2. 遍历顺序

`pre_min` 的更新必须在利润计算之后（或同时），否则会用当天的价格作为买入价，导致同一天买卖。

### 3. 特殊情况

`n <= 1` 时直接返回 `0`。

---

## 扩展思考

### 如果允许多次交易呢？

就是 [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)，贪心策略是「所有上涨波段都交易」。

### 如果最多交易 k 次呢？

需要用到动态规划，状态为 `dp[i][k][0/1]`。

## 相关题目

- [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)
- [123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/)
- [309. 最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
