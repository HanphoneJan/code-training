---
title: 打家劫舍
platform: LeetCode
difficulty: Medium
id: 198
url: https://leetcode.cn/problems/house-robber/
tags:
  - 动态规划
  - 数组
topics:
  - ../../topics/dynamic-programming.md
patterns:
  - ../../patterns/dp-linear.md
date_added: 2026-04-09
date_reviewed: []
---

# 198. 打家劫舍

## 题目描述

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你今晚不触动警报装置的情况下，能够偷窃到的最高金额。

## 示例

**示例 1：**
```
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**
```
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**动态规划**问题。核心约束是：**不能偷窃相邻的两间房屋**。

对于每一间房屋，小偷只有两种选择：
1. **偷**：获得当前房屋的金额，但不能偷上一间
2. **不偷**：保持之前的状态

### 第二步：暴力解法 - 递归

对于第 i 间房屋，递归考虑偷或不偷：

```python
def rob(self, nums: List[int]) -> int:
    def dfs(i):
        if i < 0:
            return 0
        # 选择1：偷第i间，则不能偷第i-1间
        # 选择2：不偷第i间
        return max(dfs(i - 2) + nums[i], dfs(i - 1))

    return dfs(len(nums) - 1)
```

**为什么不够好**：时间复杂度 O(2^n)，存在大量重复计算。

### 第三步：优化解法 - 记忆化搜索

用数组保存已计算的结果，避免重复计算：

```python
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    memo = [-1] * n

    def dfs(i):
        if i < 0:
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dfs(i - 2) + nums[i], dfs(i - 1))
        return memo[i]

    return dfs(n - 1)
```

**分析**：时间复杂度 O(n)，空间复杂度 O(n)。

### 第四步：最优解法 - 动态规划（空间优化）

**状态定义**：`dp[i]` 表示偷窃前 i 间房屋能获得的最高金额。

**状态转移方程**：
```
dp[i] = max(dp[i-2] + nums[i], dp[i-1])
```

**空间优化**：
由于 `dp[i]` 只依赖于 `dp[i-1]` 和 `dp[i-2]`，可以用两个变量代替数组。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    打家劫舍 - 动态规划

    核心思路：
    对于第 i 间房屋，有两种选择：
    1. 偷：则不能偷第 i-1 间，最大金额 = dp[i-2] + nums[i]
    2. 不偷：最大金额 = dp[i-1]

    状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    时间复杂度：O(n)
    空间复杂度：O(1) - 只使用两个变量
    """

    def rob(self, nums: List[int]) -> int:
        # f0 表示 dp[i-2]，f1 表示 dp[i-1]
        f0 = f1 = 0
        for num in nums:
            # 更新：新的 f0 = 旧的 f1，新的 f1 = max(偷当前, 不偷当前)
            f0, f1 = f1, max(f0 + num, f1)

        return f1
```

---

## 示例推演

以 `nums = [2, 7, 9, 3, 1]` 为例：

| 步骤 | 房屋 | 金额 | f0 (dp[i-2]) | f1 (dp[i-1]) | 偷当前 | 不偷当前 | 选择 |
|------|------|------|--------------|--------------|--------|----------|------|
| 初始 | - | - | 0 | 0 | - | - | - |
| i=0 | 第1间 | 2 | 0 | max(0+2, 0)=2 | 2 | 0 | 偷 |
| i=1 | 第2间 | 7 | 0→2 | max(0+7, 2)=7 | 7 | 2 | 偷 |
| i=2 | 第3间 | 9 | 2→7 | max(2+9, 7)=11 | 11 | 7 | 偷 |
| i=3 | 第4间 | 3 | 7→11 | max(7+3, 11)=11 | 10 | 11 | 不偷 |
| i=4 | 第5间 | 1 | 11→11 | max(11+1, 11)=12 | 12 | 11 | 偷 |

最终结果：`f1 = 12`

**偷窃方案**：第1间(2) + 第3间(9) + 第5间(1) = 12

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力递归 | O(2^n) | O(n) | 递归栈空间，大量重复计算 |
| 记忆化搜索 | O(n) | O(n) | 需要 memo 数组和递归栈 |
| 动态规划 | O(n) | O(n) | 需要 dp 数组 |
| 空间优化DP | O(n) | O(1) | 只用两个变量，最优 |

---

## 易错点总结

### 1. 状态转移方程写错

**错误**：`dp[i] = max(dp[i-1] + nums[i], dp[i-2])`

**正确**：`dp[i] = max(dp[i-2] + nums[i], dp[i-1])`

解释：如果偷第 i 间，就不能偷第 i-1 间，所以是 `dp[i-2] + nums[i]`。

### 2. 边界条件处理

```python
# 初始化时，f0 = f1 = 0 表示没有房屋时金额为0
# 这样处理空数组时直接返回 0，无需特殊判断
f0 = f1 = 0
```

### 3. 变量更新顺序

```python
# 正确：同时更新
f0, f1 = f1, max(f0 + num, f1)

# 错误：顺序更新会导致 f0 被覆盖
f0 = f1          # f0 已经改变
f1 = max(f0 + num, f1)  # 这里用的 f0 是新的，错误！
```

---

## 扩展思考

### 1. 如果房屋围成一圈？

这是 [213. 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) 的问题。

由于首尾相邻，需要分两种情况：
- 不偷第一间：对 `[1:]` 进行普通打家劫舍
- 不偷最后一间：对 `[:-1]` 进行普通打家劫舍
- 取两种情况的最大值

### 2. 如果房屋形成二叉树结构？

这是 [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/) 的问题。

需要使用树形 DP，每个节点返回两个值：偷当前节点的最大金额、不偷当前节点的最大金额。

### 3. 相关题目

- [198. 打家劫舍](https://leetcode.cn/problems/house-robber/) - 线性数组
- [213. 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) - 环形数组
- [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/) - 二叉树
- [740. 删除并获得点数](https://leetcode.cn/problems/delete-and-earn/) - 类似思路

---

## 相关题目

- [213. 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/)
- [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/)
- [740. 删除并获得点数](https://leetcode.cn/problems/delete-and-earn/)
- [2560. 打家劫舍 IV](https://leetcode.cn/problems/house-robber-iv/)
