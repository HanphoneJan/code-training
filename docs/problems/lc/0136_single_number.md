---
title: 只出现一次的数字
platform: LeetCode
difficulty: 简单
id: 136
url: https://leetcode.cn/problems/single-number/
tags:
  - 数组
  - 位运算
topics:
  - ../../topics/array.md
  - ../../topics/bit_manipulation.md
patterns:
  - ../../patterns/bit_manipulation.md
date_added: 2026-04-03
date_reviewed: []
---

# 0136. 只出现一次的数字

## 题目描述

给你一个 **非空** 整数数组 `nums`，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

## 示例

**示例 1：**
```
输入：nums = [2,2,1]
输出：1
```

**示例 2：**
```
输入：nums = [4,1,2,1,2]
输出：4
```

---

## 解题思路

### 第一步：理解问题

数组中只有一个数字出现一次，其他都出现两次。传统方法是哈希表统计次数，但空间复杂度是 `O(n)`，不满足要求。

### 第二步：暴力解法

用哈希表统计每个数字出现次数：

```python
from collections import Counter

def singleNumber(nums):
    cnt = Counter(nums)
    for k, v in cnt.items():
        if v == 1:
            return k
```

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 第三步：排序解法

先排序，然后两两比较：

```python
def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]
```

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(1)`（或 `O(log n)`，取决于排序）

### 第四步：最优解法 - 异或运算

利用异或（XOR）的三个性质：
1. `a ^ 0 = a`
2. `a ^ a = 0`
3. 满足交换律和结合律

所以把所有数字异或起来，出现两次的数字会互相抵消，剩下的就是只出现一次的数字。

```python
def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num
    return x
```

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    136. 只出现一次的数字 - 位运算（异或）

    核心思想：
    利用异或运算的性质：a ^ a = 0，a ^ 0 = a。
    所有出现两次的数字异或后抵消为 0，最后剩下的就是只出现一次的数字。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x
```

---

## 示例推演

以 `nums = [4, 1, 2, 1, 2]` 为例：

```
x = 0
x ^= 4  -> x = 4  (0 ^ 4 = 4)
x ^= 1  -> x = 5  (4 ^ 1 = 5)
x ^= 2  -> x = 7  (5 ^ 2 = 7)
x ^= 1  -> x = 6  (7 ^ 1 = 6)
x ^= 2  -> x = 4  (6 ^ 2 = 4)
```

最终答案：`4`

从交换律和结合律的角度：
```
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1 ^ 1) ^ (2 ^ 2)
= 4 ^ 0 ^ 0
= 4
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 哈希表 | O(n) | O(n) | 直观但不符合空间要求 |
| 排序 | O(n log n) | O(1) | 不满足时间要求 |
| 异或 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. 初始值

异或的初始值必须是 `0`，因为 `0 ^ a = a`。

### 2. 适用于什么场景？

只有当「一个数字出现一次，其他都出现两次」时才有效。如果其他数字出现三次，需要用更复杂的方法。

---

## 扩展思考

### 如果只有一个数字出现一次，其他都出现三次？

就是 [137. 只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/)，需要用位运算统计每一位上 1 的个数，模 3 后还原。

### 如果有两个数字只出现一次？

就是 [260. 只出现一次的数字 III](https://leetcode.cn/problems/single-number-iii/)，需要把所有数字分组后分别异或。

## 相关题目

- [137. 只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/)
- [260. 只出现一次的数字 III](https://leetcode.cn/problems/single-number-iii/)
