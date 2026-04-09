---
title: 最长递增子序列
platform: LeetCode
difficulty: Medium
id: 300
url: https://leetcode.cn/problems/longest-increasing-subsequence/
tags:
  - 动态规划
  - 二分查找
  - 贪心
date_added: 2026-04-09
---

# 300. 最长递增子序列

## 题目描述

给你一个整数数组 `nums`，找到其中最长严格递增子序列的长度。

**子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

**示例 1：**

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
输入：nums = [0,1,0,3,2,3]
输出：4
```

**示例 3：**

```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

**提示：**
- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**进阶：**
- 你能将算法的时间复杂度降低到 `O(n log n)` 吗?

---

## 解题思路

### 第一步：理解问题本质

最长递增子序列（LIS, Longest Increasing Subsequence）是经典的动态规划问题。

关键理解：
- 子序列不要求连续，但要求相对顺序不变
- "严格递增"意味着后面的数必须大于前面的数

### 第二步：暴力解法

枚举所有子序列，检查是否为递增序列，记录最大长度。

```python
def lengthOfLIS_brute(nums):
    n = len(nums)
    max_len = 0
    
    # 枚举所有子集（用位运算）
    for mask in range(1 << n):
        subseq = []
        for i in range(n):
            if mask & (1 << i):
                subseq.append(nums[i])
        
        # 检查是否为递增序列
        is_increasing = True
        for i in range(1, len(subseq)):
            if subseq[i] <= subseq[i-1]:
                is_increasing = False
                break
        
        if is_increasing:
            max_len = max(max_len, len(subseq))
    
    return max_len
```

**为什么不够好？**
- 时间复杂度 O(2^n * n)，会超时
- 没有利用子问题的重叠性质

### 第三步：优化解法 - 动态规划 O(n^2)

**定义状态：** `dp[i]` 表示以 `nums[i]` 结尾的最长递增子序列长度

**状态转移：**
```
dp[i] = max(dp[j] + 1) 对于所有 j < i 且 nums[j] < nums[i]
```

**初始化：** `dp[i] = 1`（每个元素自身构成长度为 1 的序列）

### 第四步：最优解法 - 贪心 + 二分查找 O(n log n)

**核心思想：**
- 维护一个数组 `tails`，`tails[i]` 表示长度为 `i+1` 的递增子序列的最小末尾元素
- 对于每个新元素，用二分查找找到它应该替换的位置
- 如果比所有 `tails` 元素都大，就扩展序列长度

**为什么这样有效？**
- 更小的末尾元素更有利于后续扩展
- `tails` 数组始终保持有序，可以用二分查找

---

## 完整代码实现

```python
from typing import List
import bisect


class Solution:
    """
    300. 最长递增子序列 (LIS) - 动态规划 + 贪心优化

    问题定义：
    找到数组中最长的严格递增子序列的长度。
    子序列不要求连续，但要求相对顺序不变。

    解法一：动态规划 O(n^2)
    - dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
    - 转移方程：dp[i] = max(dp[j] + 1) 对于所有 j < i 且 nums[j] < nums[i]
    - 初始：dp[i] = 1（每个元素自身构成长度为 1 的序列）

    解法二：贪心 + 二分查找 O(n log n)
    - 维护一个数组 tails，tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素
    - 对于每个新元素，用二分查找找到它应该替换的位置
    - 如果比所有 tails 元素都大，就扩展序列长度

    时间复杂度:
    - DP: O(n^2)
    - 贪心+二分: O(n log n)

    空间复杂度: O(n) - DP数组或tails数组
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划解法 O(n^2)
        dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
        """
        if not nums:
            return 0

        n = len(nums)
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
        dp = [1] * n

        for i in range(n):
            # 检查所有在 i 之前的元素 j
            for j in range(i):
                if nums[i] > nums[j]:
                    # 如果 nums[i] 可以接在 nums[j] 后面，更新 dp[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        # 返回所有 dp 值中的最大值
        return max(dp)

    def lengthOfLIS_greedy(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找解法 O(n log n)
        tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素
        """
        if not nums:
            return 0

        tails = []  # tails[i] = 长度为 i+1 的递增子序列的最小末尾元素

        for num in nums:
            # 在 tails 中找到第一个 >= num 的位置
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                # num 比所有 tails 元素都大，可以扩展序列
                tails.append(num)
            else:
                # 替换 tails[idx] 为 num，保持更小的末尾元素
                tails[idx] = num

        return len(tails)
```

---

## 示例推演

以 `nums = [10, 9, 2, 5, 3, 7, 101, 18]` 为例：

### 动态规划法：

| i | nums[i] | j | nums[j] | nums[i]>nums[j]? | dp[j]+1 | dp[i] |
|---|---------|---|---------|------------------|---------|-------|
| 0 | 10 | - | - | - | - | 1 |
| 1 | 9 | 0 | 10 | 否 | - | 1 |
| 2 | 2 | 0,1 | 10,9 | 否 | - | 1 |
| 3 | 5 | 0,1,2 | 10,9,2 | 是(j=2) | 2 | 2 |
| 4 | 3 | 0,1,2,3 | 10,9,2,5 | 是(j=2) | 2 | 2 |
| 5 | 7 | ... | ... | 是(j=3,4) | 3,3 | 3 |
| 6 | 101 | ... | ... | 是(所有) | 最大4 | 4 |
| 7 | 18 | ... | ... | 是(j=3,4,5) | 3,3,4 | 4 |

最终结果：`max(dp) = 4`

### 贪心 + 二分查找法：

```
num=10: tails = [10]
num=9:  tails = [9]           (替换 10)
num=2:  tails = [2]           (替换 9)
num=5:  tails = [2, 5]        (5 > 2，扩展)
num=3:  tails = [2, 3]        (替换 5)
num=7:  tails = [2, 3, 7]     (7 > 3，扩展)
num=101: tails = [2, 3, 7, 101]  (扩展)
num=18: tails = [2, 3, 7, 18]    (替换 101)

结果: len(tails) = 4
```

**关键观察：**
- `tails` 数组始终保持有序
- 替换操作保持了"相同长度下末尾元素最小"的性质
- 最终 `tails` 的长度就是 LIS 的长度

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(2^n) | O(n) | 枚举所有子集 |
| 动态规划 | O(n^2) | O(n) | 经典 DP 解法 |
| 贪心+二分 | O(n log n) | O(n) | 最优解法 |

---

## 易错点总结

### 1. 严格递增 vs 非严格递增

**严格递增（本题）：**
```python
if nums[i] > nums[j]:  # 严格大于
    dp[i] = max(dp[i], dp[j] + 1)
```

**非严格递增（允许相等）：**
```python
if nums[i] >= nums[j]:  # 大于等于
    dp[i] = max(dp[i], dp[j] + 1)
```

### 2. 二分查找的选择

**正确做法：** 使用 `bisect_left` 找第一个 `>= num` 的位置。
```python
idx = bisect.bisect_left(tails, num)
```

**错误做法：** 使用 `bisect_right` 会导致错误。

### 3. 返回的是长度而非序列

`tails` 数组本身不一定是 LIS，只是用来计算长度的工具。

例如：`nums = [3, 1, 2]`，最终 `tails = [1, 2]`，但 `[1, 2]` 是 LIS。

但 `nums = [1, 2, 3, 0]`，最终 `tails = [0, 2, 3]`，`[0, 2, 3]` 不是原数组的子序列。

### 4. 边界条件

```python
if not nums:
    return 0
```

---

## 扩展思考

### 1. 相关题目

- [354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/) - 二维 LIS
- [673. 最长递增子序列的个数](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) - 统计个数
- [1626. 无矛盾的最佳球队](https://leetcode.cn/problems/best-team-with-no-conflicts/) - 排序后 LIS

### 2. 如何输出具体的 LIS？

使用 DP 方法，记录前驱节点：

```python
def lengthOfLIS_with_path(nums):
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n  # 记录前驱

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # 找到最大值的索引
    max_idx = max(range(n), key=lambda i: dp[i])

    # 重建路径
    path = []
    while max_idx != -1:
        path.append(nums[max_idx])
        max_idx = prev[max_idx]

    return path[::-1]  # 反转
```

### 3. 二维 LIS - 俄罗斯套娃信封

问题：信封 (w, h)，一个信封能放入另一个当且仅当 w 和 h 都更小。

解法：
1. 按宽度升序排序，宽度相同按高度降序排序
2. 对高度求 LIS

```python
def maxEnvelopes(envelopes):
    # 按宽度升序，宽度相同按高度降序
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    # 对高度求 LIS
    heights = [h for _, h in envelopes]
    return lengthOfLIS_greedy(heights)
```

### 4. 最长递减子序列

将数组取反，求 LIS 即可：
```python
def lengthOfLDS(nums):
    return lengthOfLIS([-x for x in nums])
```
