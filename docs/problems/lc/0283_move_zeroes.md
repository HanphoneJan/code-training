---
title: 移动零
platform: LeetCode
difficulty: Easy
id: 283
url: https://leetcode.cn/problems/move-zeroes/
tags:
  - 数组
  - 双指针
date_added: 2026-04-09
---

# 283. 移动零

## 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意**，必须在不复制数组的情况下原地对数组进行操作。

**示例 1：**

```
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**示例 2：**

```
输入: nums = [0]
输出: [0]
```

**提示：**
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

**进阶：** 你能尽量减少完成的操作次数吗？

---

## 解题思路

### 第一步：理解问题本质

需要在原地修改数组，将非零元素移到前面，零移到后面，同时保持非零元素的相对顺序。

这是一个典型的数组分区问题，可以使用双指针解决。

### 第二步：暴力解法

创建一个新数组，先复制所有非零元素，再填充零，最后复制回原数组。

```python
def moveZeroes_brute(nums):
    n = len(nums)
    result = []
    
    # 先复制非零元素
    for num in nums:
        if num != 0:
            result.append(num)
    
    # 再填充零
    while len(result) < n:
        result.append(0)
    
    # 复制回原数组
    for i in range(n):
        nums[i] = result[i]
```

**为什么不够好？**
- 使用了 O(n) 额外空间，不符合题目要求
- 需要多次遍历数组

### 第三步：优化解法 - 两次遍历

第一遍将所有非零元素移到前面，第二遍将剩余位置填充为零。

```python
def moveZeroes_two_pass(nums):
    n = len(nums)
    left = 0
    
    # 第一遍：将非零元素移到前面
    for i in range(n):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    
    # 第二遍：填充零
    for i in range(left, n):
        nums[i] = 0
```

**复杂度分析：**
- 时间复杂度 O(n) - 两次遍历
- 空间复杂度 O(1) - 原地修改

### 第四步：最优解法 - 快慢指针

使用两个指针，一次遍历完成：
- **慢指针**：指向下一个非零元素应该放置的位置
- **快指针**：遍历数组，寻找非零元素

当快指针找到非零元素时，与慢指针交换，然后慢指针前进。

---

## 完整代码实现

```python
from typing import List


class Solution:
    """
    283. 移动零 - 双指针解法

    核心思路：
    使用双指针将数组分为两部分：左边是非零元素，右边是零。

    解法一：两次遍历（当前实现）
    - 第一遍：统计零的个数
    - 第二遍：将所有非零元素移到前面
    - 第三遍：将剩余位置填充为零

    解法二：一次遍历（快慢指针）
    - 慢指针指向当前可以放置非零元素的位置
    - 快指针遍历数组，遇到非零元素就与慢指针交换

    时间复杂度: O(n) - 遍历数组一次或两次
    空间复杂度: O(1) - 原地修改，只使用常数额外空间
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        两次遍历法：先将非零元素前移，再填充零
        不返回任何值，直接修改输入数组
        """
        n = len(nums)
        # 统计零的个数
        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1

        # 将所有非零元素移到数组前面
        left = 0  # 指向下一个可以放置非零元素的位置
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1

        # 将剩余位置填充为零
        for i in range(n - count, n):
            nums[i] = 0

    def moveZeroes_two_pointers(self, nums: List[int]) -> None:
        """
        快慢指针法：一次遍历完成
        - 慢指针：指向下一个非零元素应该放置的位置
        - 快指针：遍历数组寻找非零元素
        """
        slow = 0  # 慢指针：指向下一个非零元素的位置
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 交换快慢指针指向的元素
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

---

## 示例推演

以 `nums = [0, 1, 0, 3, 12]` 为例：

### 两次遍历法：

**第一遍（统计零）：**
```
nums = [0, 1, 0, 3, 12]
零的个数 count = 2
```

**第二遍（移动非零元素）：**
```
初始: left = 0
i=0: nums[0]=0, 跳过
i=1: nums[1]=1, nums[0]=1, left=1
i=2: nums[2]=0, 跳过
i=3: nums[3]=3, nums[1]=3, left=2
i=4: nums[4]=12, nums[2]=12, left=3

此时 nums = [1, 3, 12, 3, 12]
```

**第三遍（填充零）：**
```
从索引 n-count=3 到 n-1=4 填充零
nums[3] = 0
nums[4] = 0

最终结果: [1, 3, 12, 0, 0]
```

### 快慢指针法：

```
初始: slow = 0, nums = [0, 1, 0, 3, 12]

fast=0: nums[0]=0, 是零，不交换
        nums = [0, 1, 0, 3, 12], slow=0

fast=1: nums[1]=1, 非零，交换 nums[0] 和 nums[1]
        nums = [1, 0, 0, 3, 12], slow=1

fast=2: nums[2]=0, 是零，不交换
        nums = [1, 0, 0, 3, 12], slow=1

fast=3: nums[3]=3, 非零，交换 nums[1] 和 nums[3]
        nums = [1, 3, 0, 0, 12], slow=2

fast=4: nums[4]=12, 非零，交换 nums[2] 和 nums[4]
        nums = [1, 3, 12, 0, 0], slow=3

最终结果: [1, 3, 12, 0, 0]
```

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 操作次数 | 说明 |
|------|-----------|-----------|---------|------|
| 暴力 | O(n) | O(n) | 3n | 需要额外数组 |
| 两次遍历 | O(n) | O(1) | 2n | 两次遍历数组 |
| 快慢指针 | O(n) | O(1) | n | 一次遍历，最优 |

---

## 易错点总结

### 1. 交换 vs 赋值

**两次遍历法使用赋值：**
```python
nums[left] = nums[i]  # 赋值
```

**快慢指针法使用交换：**
```python
nums[slow], nums[fast] = nums[fast], nums[slow]  # 交换
```

### 2. 慢指针的更新时机

**正确做法：** 只有在发生交换/赋值后才移动慢指针。

```python
if nums[fast] != 0:
    nums[slow], nums[fast] = nums[fast], nums[slow]
    slow += 1  # 只有交换后才移动
```

### 3. 相对顺序的保持

快慢指针法之所以能保持相对顺序，是因为：
- 慢指针总是指向零（或已经处理过的位置）
- 快指针找到的非零元素被交换到慢指针位置
- 由于快指针从左到右遍历，非零元素的相对顺序不变

### 4. 边界条件

- 数组全为零：`[0, 0, 0]` -> `[0, 0, 0]`
- 数组全为非零：`[1, 2, 3]` -> `[1, 2, 3]`
- 单个元素：`[0]` 或 `[1]`

---

## 扩展思考

### 1. 相关题目

- [27. 移除元素](https://leetcode.cn/problems/remove-element/) - 类似的双指针
- [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) - 快慢指针
- [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)

### 2. 变体问题

**题目：将数组中的负数移到前面，正数移到后面**

解法相同，只需修改判断条件：
```python
def moveNegatives(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] < 0:  # 负数移到前面
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

### 3. 荷兰国旗问题

将数组分成三部分（红、白、蓝），需要三个指针：
```python
def sortColors(nums):
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
```
