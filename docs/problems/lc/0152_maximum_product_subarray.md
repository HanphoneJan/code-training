---
title: 乘积最大子数组
platform: LeetCode
difficulty: 中等
id: 152
url: https://leetcode.cn/problems/maximum-product-subarray/
tags:
  - 数组
  - 动态规划
topics:
  - ../../topics/array.md
  - ../../topics/dynamic_programming.md
patterns:
  - ../../topics/dynamic_programming.md
date_added: 2026-04-03
date_reviewed: []
---

# 0152. 乘积最大子数组

## 题目描述

给你一个整数数组 `nums`，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 **32-位** 整数。

**示例 1：**
```
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
```

**示例 2：**
```
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

---

## 解题思路

### 第一步：为什么不是最大子数组和的翻版？

[53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/) 只需要维护以当前元素结尾的最大和。

但乘积不同：负数乘以负数会变成正数，而且正是最大值。所以**最小值在下一秒可能变成最大值**。

### 第二步：暴力解法

枚举所有子数组，计算乘积：

```python
def maxProduct(nums):
    n = len(nums)
    ans = nums[0]
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            ans = max(ans, prod)
    return ans
```

- 时间复杂度：`O(n²)`
- 空间复杂度：`O(1)`

### 第三步：动态规划

同时维护两个状态：
- `f_max`：以当前位置结尾的子数组的最大乘积
- `f_min`：以当前位置结尾的子数组的最小乘积

为什么需要 `f_min`？因为当前元素如果是负数，`f_min * x` 可能变成最大值。

状态转移：
```
f_max = max(f_max * x, f_min * x, x)
f_min = min(f_max * x, f_min * x, x)
```

注意：Python 中可以通过元组解包同时更新两个值。

---

## 完整代码实现

```python
from typing import List
from math import inf

class Solution:
    """
    152. 乘积最大子数组 - 动态规划

    核心思想：
    由于负数的存在，最小值可能转瞬变成最大值。
    所以需要同时维护以当前位置结尾的最大乘积和最小乘积。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        f_max = 1
        f_min = 1

        for x in nums:
            # 同时更新最大和最小乘积
            f_max, f_min = max(f_max * x, f_min * x, x), \
                           min(f_max * x, f_min * x, x)
            ans = max(ans, f_max)

        return int(ans)
```

---

## 示例推演

以 `nums = [2, 3, -2, 4]` 为例：

| 元素 | f_max | f_min | ans |
|------|-------|-------|-----|
| 2 | max(2, 2, 2) = 2 | min(2, 2, 2) = 2 | 2 |
| 3 | max(6, 6, 3) = 6 | min(6, 6, 3) = 3 | 6 |
| -2 | max(-12, -6, -2) = -2 | min(-12, -6, -2) = -12 | 6 |
| 4 | max(-8, -48, 4) = 4 | min(-8, -48, 4) = -48 | 6 |

最终答案：`6`（子数组 `[2, 3]`）

再试 `nums = [-2, 0, -1]`：

| 元素 | f_max | f_min | ans |
|------|-------|-------|-----|
| -2 | -2 | -2 | -2 |
| 0 | 0 | 0 | 0 |
| -1 | max(0, 0, -1) = 0 | min(0, 0, -1) = -1 | 0 |

最终答案：`0`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 枚举所有子数组 |
| 动态规划 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 要同时维护最小值

如果只维护最大值，遇到负数时会出错（负负得正）。

### 2. 初始值

`ans` 初始化为 `-inf`，因为数组中可能全是负数，最大乘积也是负数。

### 3. 同时更新

```python
f_max, f_min = max(...), min(...)
```

这样写能确保 `f_min` 使用的是上一轮的值，而不是已经被更新过的 `f_max`。

### 4. 0 的处理

遇到 `0` 时，`f_max` 和 `f_min` 都会变成 `0`，相当于从 `0` 后面重新开始计算。

---

## 扩展思考

### 如果要求输出子数组呢？

除了维护最大/最小值，还需要记录对应的子数组起始位置。

### 为什么这题不能用单调栈？

因为乘积的单调性比求和复杂得多，负数会改变单调性方向。

## 相关题目

- [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)
- [325. 和等于 k 的最长子数组长度](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/)
