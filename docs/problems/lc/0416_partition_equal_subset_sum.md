---
title: 分割等和子集
platform: LeetCode
difficulty: Medium
id: 416
url: https://leetcode.cn/problems/partition-equal-subset-sum/
tags:
  - 数组
  - 动态规划
  - 背包问题
topics:
  - ../../topics/dynamic-programming.md
  - ../../topics/knapsack.md
patterns:
  - ../../patterns/0-1-knapsack.md
date_added: 2026-04-09
date_reviewed: []
---

# 416. 分割等和子集

## 题目描述

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

**示例 1：**
```
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1,5,5] 和 [11]
```

**示例 2：**
```
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集
```

**提示：**
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

---

## 解题思路

### 第一步：理解问题本质

这道题可以转化为一个经典的**0/1 背包问题**：

1. 计算数组总和 `sum`
2. 如果 `sum` 是奇数，无法平分，直接返回 `False`
3. 问题转化为：能否从数组中选出一些数，使它们的和等于 `sum / 2`

这就是 0/1 背包问题：背包容量为 `target = sum / 2`，每个物品（数字）可以选或不选，问能否恰好装满背包。

### 第二步：暴力解法 - 回溯

**思路：** 枚举每个数字选或不选，检查是否存在一种选择使和为 target。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        n = len(nums)

        def backtrack(i, current_sum):
            if current_sum == target:
                return True
            if current_sum > target or i >= n:
                return False
            # 选或不选第 i 个数
            return backtrack(i + 1, current_sum + nums[i]) or \
                   backtrack(i + 1, current_sum)

        return backtrack(0, 0)
```

**为什么不够好？** 时间复杂度 O(2^n)，会超时。

### 第三步：优化解法 - 记忆化搜索

**关键洞察：** 递归过程中有大量重复子问题，如 `dfs(2, 10)` 可能被多次计算。

**优化：** 用 `@cache` 缓存已经计算过的状态。

```python
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        n = len(nums)

        @cache
        def dfs(i, remain):
            if remain == 0:
                return True
            if remain < 0 or i >= n:
                return False
            return dfs(i + 1, remain - nums[i]) or dfs(i + 1, remain)

        return dfs(0, target)
```

### 第四步：最优解法 - 动态规划

**关键洞察：** 这是标准的 0/1 背包问题，可以用 DP 解决。

**状态定义：** `dp[j]` 表示能否用数组中的数凑出和为 `j`

**状态转移：**
```
dp[j] = dp[j] or dp[j - nums[i]]
```
- `dp[j]`：不选第 i 个数
- `dp[j - nums[i]]`：选第 i 个数

**空间优化：** 使用一维数组，倒序遍历避免重复计算。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [True] + [False] * target

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True

        return dp[target]
```

---

## 完整代码实现

```python
from typing import List
from functools import cache

class Solution:
    """
    分割等和子集 - 记忆化搜索解法

    核心思路：
    1. 计算数组总和，如果是奇数直接返回 False
    2. 问题转化为：能否凑出和为总和一半的子集
    3. 使用记忆化搜索，dfs(i, remain) 表示从第 i 个数开始能否凑出 remain

    时间复杂度: O(n * target)
    空间复杂度: O(n * target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        @cache
        def dfs(start: int, remain: int) -> bool:
            if remain == 0:
                return True
            if remain < 0 or start >= n:
                return False
            return dfs(start + 1, remain - nums[start]) or \
                   dfs(start + 1, remain)

        return dfs(0, target)
```

---

## 示例推演

以 `nums = [1, 5, 11, 5]` 为例：

**第一步：预处理**
- 总和 = 1 + 5 + 11 + 5 = 22
- target = 11

**第二步：DP 过程**

| 步骤 | 当前数字 | dp 数组（下标 0-11） |
|------|----------|---------------------|
| 初始 | - | [T,F,F,F,F,F,F,F,F,F,F,F] |
| 1 | 1 | [T,T,F,F,F,F,F,F,F,F,F,F] |
| 2 | 5 | [T,T,F,F,F,T,T,F,F,F,F,F] |
| 3 | 11 | [T,T,F,F,F,T,T,F,F,F,F,T] |
| 4 | 5 | [T,T,F,F,F,T,T,F,F,F,T,T] |

**结果：** `dp[11] = True`，可以分割

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力回溯 | O(2^n) | O(n) | 枚举所有子集 |
| 记忆化搜索 | O(n × target) | O(n × target) | target = sum/2 |
| 动态规划 | O(n × target) | O(target) | 空间优化版 |

**说明：**
- n 是数组长度
- target 是数组总和的一半
- 由于 nums[i] <= 100 且 n <= 200，target <= 10000，DP 完全可行

---

## 易错点总结

### 1. 总和为奇数的判断

```python
# 必须先判断总和是否为奇数
if sum(nums) % 2:
    return False
```

### 2. DP 数组的遍历方向

```python
# 必须倒序遍历！
for j in range(target, num - 1, -1):
    dp[j] = dp[j] or dp[j - num]

# 正序遍历会导致重复计算（完全背包）
```

### 3. 递归的边界条件

```python
# 注意判断顺序
if remain == 0:      # 先判断是否凑出目标
    return True
if remain < 0:       # 再判断是否超出
    return False
```

---

## 扩展思考

### 1. 如何输出具体的分割方案？

可以用 DP 记录路径，或使用回溯记录选择的数字。

### 2. 如果要求两个子集的大小也相等？

需要二维 DP：`dp[i][j]` 表示能否用 i 个数凑出和为 j。

### 3. 相关题目

- [494. 目标和](https://leetcode.cn/problems/target-sum/) - 变形背包问题
- [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/) - 类似的分割问题
- [474. 一和零](https://leetcode.cn/problems/ones-and-zeroes/) - 二维费用背包

---

## 相关题目

- [494. 目标和](https://leetcode.cn/problems/target-sum/)
- [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/)
- [474. 一和零](https://leetcode.cn/problems/ones-and-zeroes/)
