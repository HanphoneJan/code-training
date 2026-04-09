---
title: 寻找重复数
platform: LeetCode
difficulty: Medium
id: 287
url: https://leetcode.cn/problems/find-the-duplicate-number/
tags:
  - 数组
  - 双指针
  - 二分查找
  - Floyd判圈
date_added: 2026-04-09
---

# 287. 寻找重复数

## 题目描述

给定一个包含 `n + 1` 个整数的数组 `nums`，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有**一个重复的整数**，返回这个重复的数。

你设计的解决方案必须**不修改**数组 `nums` 且只用**常量级** `O(1)` 的额外空间。

**示例 1：**

```
输入: nums = [1,3,4,2,2]
输出: 2
```

**示例 2：**

```
输入: nums = [3,1,3,4,2]
输出: 3
```

**示例 3：**

```
输入: nums = [3,3,3,3,3]
输出: 3
```

**提示：**
- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- `nums` 中只有一个整数出现两次或多次，其余整数均只出现一次

**进阶：**
- 如何证明 `nums` 中至少存在一个重复的数字?
- 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？
- 你可以设计一个空间复杂度为 `O(1)` 且时间复杂度小于 `O(n^2)` 的解决方案吗？

---

## 解题思路

### 第一步：理解问题本质

关键约束：
1. 不能修改数组（不能排序）
2. 只能使用 O(1) 额外空间（不能用哈希表）

这些约束排除了很多常规解法，需要使用更巧妙的算法。

### 第二步：暴力解法

双重循环，逐个比较元素。

```python
def findDuplicate_brute(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]
    return -1
```

**为什么不够好？**
- 时间复杂度 O(n^2)，会超时
- 没有利用数组元素范围的特性

### 第三步：优化解法 - 二分查找

利用抽屉原理：如果重复数是 `target`，那么小于等于 `target` 的数的个数一定大于 `target`。

```python
def findDuplicate_binary_search(nums):
    left, right = 1, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        count = sum(1 for x in nums if x <= mid)
        
        if count > mid:
            # 重复数在 [left, mid] 中
            right = mid
        else:
            # 重复数在 [mid+1, right] 中
            left = mid + 1
    
    return left
```

**复杂度分析：**
- 时间复杂度 O(n log n) - 二分查找 O(log n)，每次统计 O(n)
- 空间复杂度 O(1)

### 第四步：最优解法 - Floyd 判圈算法

**核心洞察：**
将数组看作一个链表：下标 `i` 指向 `nums[i]`。
- 每个下标有一条出边指向 `nums[i]`
- 由于存在重复数，有两个下标指向同一个值，形成环的入口
- 重复数就是环的入口

**Floyd 判圈算法（龟兔赛跑）：**
1. **阶段一**：快慢指针找相遇点
   - 慢指针每次走 1 步
   - 快指针每次走 2 步
   - 有环则必然相遇

2. **阶段二**：找环的入口
   - 一个指针从起点出发，另一个从相遇点出发
   - 两者每次各走 1 步，再次相遇点即为环入口

**数学证明：**
设环前长度为 `a`，环长度为 `b`。
- 快慢指针相遇时，快指针比慢指针多走了 `n` 圈：`2d = d + nb`
- 因此 `d = nb`，即慢指针走了 `nb` 步
- 从起点再走 `a` 步到环入口，从相遇点再走 `a` 步也到环入口

---

## 完整代码实现

```python
from typing import List


class Solution:
    """
    287. 寻找重复数 - Floyd 判圈算法（龟兔赛跑算法）

    问题分析：
    数组有 n+1 个整数，范围在 [1, n] 之间，必有一个重复数。
    关键约束：不能修改数组，只能使用 O(1) 额外空间。

    核心洞察：
    将数组看作一个链表：下标 i 指向 nums[i]。
    由于存在重复数，这个"链表"必然存在环！
    - 每个下标 i 有一条出边指向 nums[i]
    - 重复数意味着有两个下标指向同一个值，形成环的入口

    Floyd 判圈算法（同 142. 环形链表 II）：
    1. 阶段一：快慢指针找相遇点
       - 慢指针每次走 1 步：slow = nums[slow]
       - 快指针每次走 2 步：fast = nums[nums[fast]]
       - 有环则必然相遇

    2. 阶段二：找环的入口（即重复数）
       - 一个指针从起点出发，另一个从相遇点出发
       - 两者每次各走 1 步，再次相遇点即为环入口

    时间复杂度: O(n) - 快慢指针最多遍历 2n 个元素
    空间复杂度: O(1) - 只使用两个指针
    """

    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd 判圈算法寻找重复数
        将数组看作链表：下标 i -> nums[i]
        """
        # 阶段一：快慢指针找相遇点
        # 选择 0 作为起点，因为数组元素范围是 [1, n]，0 一定不在环上
        slow = fast = 0
        while True:
            slow = nums[slow]           # 慢指针走 1 步
            fast = nums[nums[fast]]     # 快指针走 2 步
            if fast == slow:            # 相遇，找到环内一点
                break

        # 阶段二：找环的入口（重复数）
        # 数学结论：从起点和相遇点各走一步，再次相遇即为环入口
        head = 0
        while slow != head:
            slow = nums[slow]   # 从相遇点出发，每次 1 步
            head = nums[head]   # 从起点出发，每次 1 步

        return slow  # 环的入口就是重复数
```

---

## 示例推演

以 `nums = [1, 3, 4, 2, 2]` 为例：

**将数组看作链表：**
```
下标:  0 -> 1 -> 3 -> 2 -> 4
值:    1    3    2    4    2

链表结构: 0 -> 1 -> 3 -> 2 -> 4
                         ↑_____|

环的入口是下标 2（值为 2），这就是重复数！
```

**阶段一：快慢指针找相遇点**
```
初始: slow = 0, fast = 0

第 1 步:
  slow = nums[0] = 1
  fast = nums[nums[0]] = nums[1] = 3

第 2 步:
  slow = nums[1] = 3
  fast = nums[nums[3]] = nums[2] = 4

第 3 步:
  slow = nums[3] = 2
  fast = nums[nums[4]] = nums[2] = 4

第 4 步:
  slow = nums[2] = 4
  fast = nums[nums[4]] = nums[2] = 4

相遇！slow = fast = 4
```

**阶段二：找环的入口**
```
head = 0, slow = 4

第 1 步:
  head = nums[0] = 1
  slow = nums[4] = 2

第 2 步:
  head = nums[1] = 3
  slow = nums[2] = 4

第 3 步:
  head = nums[3] = 2
  slow = nums[4] = 2

相遇！head = slow = 2

返回 2，这就是重复数。
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n^2) | O(1) | 双重循环，超时 |
| 排序 | O(n log n) | O(1) 或 O(n) | 修改数组，不符合要求 |
| 哈希表 | O(n) | O(n) | 空间复杂度不符合要求 |
| 二分查找 | O(n log n) | O(1) | 满足约束，但不是最优 |
| Floyd 判圈 | O(n) | O(1) | 最优解法 |

---

## 易错点总结

### 1. 起点选择

**正确做法：** 选择 0 作为起点。
```python
slow = fast = 0
```

**原因：** 数组元素范围是 `[1, n]`，0 一定不在环上，适合作为起点。

### 2. 快指针的移动

**正确做法：**
```python
fast = nums[nums[fast]]  # 走 2 步
```

**错误做法：**
```python
fast = nums[fast + 1]    # 错误！不是简单的加 1
```

### 3. 阶段二的指针设置

**正确做法：**
```python
head = 0  # 从起点出发
while slow != head:  # slow 从相遇点出发
    slow = nums[slow]
    head = nums[head]
```

### 4. 为什么一定能找到重复数？

根据抽屉原理：n+1 个物品放入 n 个抽屉，至少有一个抽屉有 2 个物品。

---

## 扩展思考

### 1. 相关题目

- [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) - Floyd 判圈模板题
- [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/) - 判断是否有环
- [202. 快乐数](https://leetcode.cn/problems/happy-number/) - 类似判圈思想

### 2. Floyd 判圈算法的应用

Floyd 判圈算法适用于：
- 判断链表是否有环
- 找环的入口
- 找序列的周期

### 3. 其他解法对比

**二分查找法：**
- 优点：容易理解，不需要将数组看作链表
- 缺点：时间复杂度 O(n log n)，不如 Floyd 的 O(n)

**Floyd 判圈法：**
- 优点：时间 O(n)，空间 O(1)，最优
- 缺点：思路巧妙，不容易想到

### 4. 数学定理

**鸽巢原理（抽屉原理）：** 如果有 n 个鸽巢，n+1 只鸽子，至少有一个鸽巢有 2 只或更多鸽子。

本题中：
- 鸽巢：1 到 n 的 n 个数字
- 鸽子：数组中的 n+1 个元素
- 结论：至少有一个数字出现两次或更多
