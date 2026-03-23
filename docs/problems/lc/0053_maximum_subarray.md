---
title: 最大子数组和
platform: LeetCode
difficulty: 中等
id: 53
url: https://leetcode.cn/problems/maximum-subarray/
tags:
  - 数组
  - 动态规划
  - 分治
topics:
  - ../../topics/array.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../patterns/kadane_algorithm.md
date_added: 2026-03-23
date_reviewed: []
---

# 0053. 最大子数组和

## 题目描述

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

## 示例

**示例 1：**
```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**
```
输入：nums = [1]
输出：1
```

**示例 3：**
```
输入：nums = [5,4,-1,7,8]
输出：23
解释：整个数组的和最大，为 23 。
```

---

## 解题思路

### 第一步：理解问题本质

**子数组**：数组中连续的一段。

**暴力思路**：枚举所有子数组，计算和，取最大。
- 时间复杂度：O(n³) 或优化到 O(n²)
- 空间复杂度：O(1)

对于每个子数组 `[i, j]`，需要计算 `sum(nums[i:j+1])`。

### 第二步：动态规划思路

**核心观察**：
以位置 `i` 结尾的子数组，要么只包含 `nums[i]`，要么包含以 `i-1` 结尾的最优子数组加上 `nums[i]`。

**状态定义**：
`dp[i]` = 以第 `i` 个元素结尾的最大子数组和

**状态转移**：
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

**解释**：
- 如果 `dp[i-1] < 0`，说明前面的子数组对当前是负贡献，不如从 `i` 重新开始
- 如果 `dp[i-1] >= 0`，可以延续前面的子数组

### 第三步：空间优化

注意到 `dp[i]` 只依赖 `dp[i-1]`，可以用一个变量代替数组。

这就是 **Kadane 算法**。

---

## 完整代码实现

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子数组和 - Kadane算法

        核心思想：维护以当前位置结尾的最大子数组和
        """
        # 当前子数组和（以当前元素结尾的最大子数组和）
        current_sum = nums[0]
        # 全局最大子数组和
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # 关键决策：
            # 如果当前子数组和 < 0，说明前面的子数组对后面是负贡献
            # 不如从当前元素重新开始
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]

            # 更新全局最大值
            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubArrayDP(self, nums: List[int]) -> int:
        """
        标准动态规划写法，更容易理解
        """
        n = len(nums)
        # dp[i] = 以 nums[i] 结尾的最大子数组和
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            # 状态转移：要么重新开始，要么延续前面的子数组
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum
```

---

## 示例推演

**示例**：`nums = [-2,1,-3,4,-1,2,1,-5,4]`

| i | nums[i] | current_sum | 决策 | max_sum |
|---|---------|-------------|------|---------|
| 0 | -2 | -2 | 初始化 | -2 |
| 1 | 1 | 1 | -2<0，重新开始 | 1 |
| 2 | -3 | -2 | 1>=0，延续 | 1 |
| 3 | 4 | 4 | -2<0，重新开始 | 4 |
| 4 | -1 | 3 | 4>=0，延续 | 4 |
| 5 | 2 | 5 | 3>=0，延续 | 5 |
| 6 | 1 | 6 | 5>=0，延续 | **6** |
| 7 | -5 | 1 | 6>=0，延续 | 6 |
| 8 | 4 | 5 | 1>=0，延续 | 6 |

**结果**：`max_sum = 6`，对应子数组 `[4,-1,2,1]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 枚举所有子数组 |
| DP数组 | O(n) | O(n) | 需要额外数组 |
| Kadane | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 初始值设置

```python
current_sum = max_sum = nums[0]
```
不要初始化为0，因为数组可能全是负数。

### 2. 决策逻辑

```python
if current_sum < 0:      # 不是 <= 0
    current_sum = nums[i]
```
等于0时可以延续，不影响结果但可能得到更长的子数组。

### 3. 遍历范围

```python
for i in range(1, n):   # 从1开始，0已经初始化
```

### 4. 更新顺序

```python
current_sum = ...        # 先更新当前值
max_sum = max(max_sum, current_sum)  # 再更新最大值
```

---

## 扩展思考

### 1. 如何返回子数组的起止位置？

```python
def maxSubArrayWithRange(self, nums):
    current_sum = max_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i  # 重新开始的位置
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end
```

### 2. 分治法解法

可以将数组分成左右两半，最大子数组可能：
- 完全在左半部分
- 完全在右半部分
- 跨越中间

时间复杂度 O(n log n)，主要作为分治思想的学习。

### 3. 如果要求子数组长度至少为 k？

需要用单调队列优化，或者前缀和 + 单调队列。

---

## 相关题目

- [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/)
- [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/)
- [974. 和可被 K 整除的子数组](https://leetcode.cn/problems/subarray-sums-divisible-by-k/)
