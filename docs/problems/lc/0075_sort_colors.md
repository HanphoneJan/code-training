---
title: 颜色分类
platform: LeetCode
difficulty: Medium
id: 75
url: https://leetcode.cn/problems/sort-colors/
tags:
  - 数组
  - 双指针
  - 排序
date_added: 2026-03-25
---

# 75. 颜色分类

## 题目描述

给定一个包含红色、白色和蓝色、共 `n` 个元素的数组 `nums`，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

## 示例

**示例 1：**
```
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
```

**示例 2：**
```
输入：nums = [2,0,1]
输出：[0,1,2]
```

---

## 解题思路

### 第一步：理解问题本质

这是一个经典的**荷兰国旗问题**。数组中只有 0, 1, 2 三个值，需要原地排序。

### 第二步：暴力解法

**思路**：统计每个数字的个数，然后按顺序填充。

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        idx = 0
        for i in range(3):
            for j in range(count[i]):
                nums[idx] = i
                idx += 1
```

**缺点**：需要两次遍历。

### 第三步：最优解法 —— 三指针法

**核心洞察**：
- `p0`：指向 0 应该放置的位置（从数组开头）
- `p2`：指向 2 应该放置的位置（从数组末尾）
- `i`：当前遍历位置

**算法步骤**：
- `nums[i] == 0`：与 `p0` 交换，`p0++`，`i++`
- `nums[i] == 1`：`i++`
- `nums[i] == 2`：与 `p2` 交换，`p2--`（`i` 不递增）

---

## 完整代码实现

```python
from typing import List

class Solution:
    """
    颜色分类 - 荷兰国旗问题

    核心思想：
    数组中只有 0, 1, 2 三个值，需要原地排序。
    这是经典的"荷兰国旗问题"。

    三指针法（最优）：
    - p0：指向0应该放置的位置（从数组开头）
    - p2：指向2应该放置的位置（从数组末尾）
    - i：当前遍历位置

    遍历策略：
    - nums[i] == 0：与 p0 位置交换，p0++，i++
    - nums[i] == 1：i++
    - nums[i] == 2：与 p2 位置交换，p2--（i 不递增，因为交换过来的元素需要再判断）

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # nums[i] == 2
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 计数排序 | O(n) | O(1) | 需要两次遍历 |
| **三指针（最优）** | **O(n)** | **O(1)** | 一次遍历 |

---

## 相关题目

- [283. 移动零](https://leetcode.cn/problems/move-zeroes/)
