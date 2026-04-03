---
title: 多数元素
platform: LeetCode
difficulty: 简单
id: 169
url: https://leetcode.cn/problems/majority-element/
tags:
  - 数组
  - 哈希表
  - 分治
  - 计数
  - 排序
  - Boyer-Moore 投票算法
topics:
  - ../../topics/array.md
  - ../../topics/bit_manipulation.md
  - ../../topics/hash_table.md
patterns:
  - ../../patterns/boyer_moore_voting.md
date_added: 2026-04-03
date_reviewed: []
---

# 0169. 多数元素

## 题目描述

给定一个大小为 `n` 的数组 `nums`，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

## 示例

**示例 1：**
```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**
```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

---

## 解题思路

### 第一步：理解问题

要找出出现次数超过一半的元素。这意味着：如果把这个元素的所有出现和其他元素两两配对抵消，它最后一定会剩下。

### 第二步：暴力解法

用哈希表统计每个数字出现次数：

```python
from collections import Counter

def majorityElement(nums):
    cnt = Counter(nums)
    for k, v in cnt.items():
        if v > len(nums) // 2:
            return k
```

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 第三步：排序解法

排序后，中间位置 `n // 2` 的元素一定是多数元素：

```python
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]
```

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(1)` 或 `O(log n)`

### 第四步：最优解法 - Boyer-Moore 投票算法

核心理念：把不同的两两抵消，最后剩下的就是多数元素。

算法步骤：
1. 维护候选者 `candidate` 和计数器 `count`
2. 遍历数组：
   - `count == 0` 时，当前元素成为新的 `candidate`
   - 当前元素 == `candidate` 时，`count += 1`
   - 否则 `count -= 1`
3. 最后 `candidate` 就是答案

为什么正确？因为多数元素出现次数 > n/2，即使和其他所有元素抵消，它仍会幸存。

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    169. 多数元素 - Boyer-Moore 投票算法

    核心思想：
    把不同的元素两两抵消，最后剩下的就是出现次数超过一半的多数元素。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```

---

## 示例推演

以 `nums = [2, 2, 1, 1, 1, 2, 2]` 为例：

| 元素 | count 前 | candidate | count 后 |
|------|---------|-----------|---------|
| 2 | 0 | 2 | 1 |
| 2 | 1 | 2 | 2 |
| 1 | 2 | 2 | 1 |
| 1 | 1 | 2 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 |
| 2 | 0 | 2 | 1 |

最终 `candidate = 2`。

从抵消的角度理解：
- 2, 2, 1, 1 互相抵消
- 剩余 1, 2, 2
- 1 和一个 2 抵消
- 剩余 2

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 哈希表 | O(n) | O(n) | 直观但空间占用大 |
| 排序 | O(n log n) | O(1) | 不满足时间最优 |
| 投票算法 | O(n) | O(1) | **最优解** |

---

## 易错点总结

### 1. count == 0 时才换 candidate

即使当前 num 不等于 candidate，只要 count > 0，只能说明这个 candidate 的优势被削弱了，还不能确定它不是多数元素。

### 2. 初始 candidate

可以设为 `nums[0]`，也可以随便设一个值，效果一样，因为 `count = 0` 会立即被第一个元素覆盖。

### 3. 题目保证有解

如果题目不保证有解，投票算法结束后还需要再遍历一遍验证 candidate 的出现次数是否 > n/2。

---

## 扩展思考

### 如果要求找出所有出现次数 > n/3 的元素？

这是 [229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii/)，需要维护两个候选者。

### 投票算法的本质

这是一种**消去法**。只要某个元素的出现次数严格超过一半，它就是不可被完全抵消的。

## 相关题目

- [229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii/)
- [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)
