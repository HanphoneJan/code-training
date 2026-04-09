---
title: 除了自身以外数组的乘积
platform: LeetCode
difficulty: Medium
id: 238
url: https://leetcode.cn/problems/product-of-array-except-self/
tags:
  - 数组
  - 前缀和
topics:
  - ../../topics/array.md
  - ../../topics/prefix-sum.md
patterns:
  - ../../patterns/prefix-suffix-decomposition.md
date_added: 2026-04-09
date_reviewed: []
---

# 238. 除了自身以外数组的乘积

## 题目描述

给你一个整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积。

**题目数据保证**：数组 `nums` 之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内。

**要求**：
- 请不要使用除法
- 在 O(n) 时间复杂度内完成此题

## 示例

**示例 1：**
```
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
```

**示例 2：**
```
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
```

---

## 解题思路

### 第一步：理解问题本质

对于位置 `i`，`answer[i]` 等于 `nums` 中除 `nums[i]` 外所有元素的乘积。

即：`answer[i] = nums[0] * ... * nums[i-1] * nums[i+1] * ... * nums[n-1]`

### 第二步：暴力解法 - 双重循环

对于每个位置，遍历其他所有位置计算乘积。

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                answer[i] *= nums[j]
    return answer
```

**为什么不够好**：时间复杂度 O(n²)。

### 第三步：优化解法 - 使用除法

先计算所有元素的乘积，然后 `answer[i] = total / nums[i]`。

**为什么不行**：题目明确要求不能使用除法，且当 `nums[i] = 0` 时无法处理。

### 第四步：最优解法 - 前后缀分解

**关键观察**：
```
answer[i] = (nums[0] * ... * nums[i-1]) * (nums[i+1] * ... * nums[n-1])
          = 前缀积[i] * 后缀积[i]
```

先计算前缀积和后缀积，然后相乘得到结果。

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    除了自身以外数组的乘积 - 前后缀分解

    核心思路：
    answer[i] = 前缀积[i] * 后缀积[i]
    其中前缀积[i] = nums[0] * ... * nums[i-1]
          后缀积[i] = nums[i+1] * ... * nums[n-1]

    优化：先用 answer 数组存储后缀积，再用变量维护前缀积

    时间复杂度：O(n)
    空间复杂度：O(1) - 不包括输出数组
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 计算后缀积，存储在 answer 中
        # answer[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
        for i in range(n - 2, -1, -1):
            answer[i] = answer[i + 1] * nums[i + 1]

        # 计算前缀积，乘到 answer 中
        pre = 1
        for i in range(n):
            answer[i] *= pre
            pre *= nums[i]

        return answer
```

---

## 示例推演

以 `nums = [1,2,3,4]` 为例：

**步骤 1：计算后缀积**

| i | answer[i] | 计算 | 结果 |
|---|-----------|------|------|
| 3 | answer[3] | 1（边界） | 1 |
| 2 | answer[2] | answer[3] * nums[3] = 1 * 4 | 4 |
| 1 | answer[1] | answer[2] * nums[2] = 4 * 3 | 12 |
| 0 | answer[0] | answer[1] * nums[1] = 12 * 2 | 24 |

此时 `answer = [24, 12, 4, 1]`（只有后缀积）

**步骤 2：计算前缀积并相乘**

| i | pre | answer[i] * pre | 新的 answer[i] | 更新 pre |
|---|-----|-----------------|----------------|----------|
| 0 | 1 | 24 * 1 | 24 | 1 * 1 = 1 |
| 1 | 1 | 12 * 1 | 12 | 1 * 2 = 2 |
| 2 | 2 | 4 * 2 | 8 | 2 * 3 = 6 |
| 3 | 6 | 1 * 6 | 6 | 6 * 4 = 24 |

最终结果：`[24, 12, 8, 6]`

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 双重循环 |
| 除法 | O(n) | O(1) | 题目不允许 |
| 前后缀数组 | O(n) | O(n) | 需要两个额外数组 |
| 优化前后缀 | O(n) | O(1) | 最优解法 |

---

## 易错点总结

### 1. 边界处理

```python
# 后缀积计算，从 n-2 开始
for i in range(n - 2, -1, -1):
    answer[i] = answer[i + 1] * nums[i + 1]

# answer[n-1] 保持为 1（右边没有元素）
```

### 2. 更新顺序

```python
# 先使用 pre 计算 answer[i]，再更新 pre
answer[i] *= pre
pre *= nums[i]  # 下一个位置的前缀积包含当前元素
```

### 3. 包含 0 的情况

如果数组中有 0：
- 一个 0：该位置结果为总乘积，其他位置为 0
- 两个及以上 0：所有位置都为 0

本题算法天然支持这种情况。

---

## 扩展思考

### 1. 如果可以用除法？

需要注意 0 的特殊处理。

### 2. 相关题目

- [238. 除了自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)
- [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) - 类似的前后缀思想
- [135. 分发糖果](https://leetcode.cn/problems/candy/) - 双向遍历

---

## 相关题目

- [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)
- [135. 分发糖果](https://leetcode.cn/problems/candy/)
- [265. 粉刷房子 II](https://leetcode.cn/problems/paint-house-ii/)
