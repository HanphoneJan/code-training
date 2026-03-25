---
title: 两数之和
platform: LeetCode
difficulty: Easy
id: 1
url: https://leetcode.cn/problems/two-sum/
tags:
  - 数组
  - 哈希表
date_added: 2026-03-25
---

# 1. 两数之和

## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出**和为目标值** `target` 的那**两个**整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

## 示例

**示例 1：**
```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9，返回 [0, 1]
```

**示例 2：**
```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**
```
输入：nums = [3,3], target = 6
输出：[0,1]
```

---

## 解题思路

### 第一步：理解问题本质

我们需要在数组中找到两个数，使它们的和等于目标值。核心问题是：**如何快速判断一个数的"补数"是否存在？**

所谓"补数"，就是 `target - num`，即与当前数相加等于目标值的另一个数。

### 第二步：暴力解法

**思路**：枚举数组中的每一对数字，检查它们的和是否等于目标值。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

**为什么不够好**：
- 时间复杂度是 O(n²)，当数组很大时效率很低
- 没有利用任何数据结构来加速查找

### 第三步：优化解法 —— 排序+双指针

**思路**：先排序，然后用双指针从两端向中间移动。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 记录原始索引
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # 按数值排序
        indexed_nums.sort(key=lambda x: x[0])

        left, right = 0, len(indexed_nums) - 1
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
```

**优点**：时间复杂度降为 O(n log n)
**缺点**：需要排序，改变了原始索引，需要额外空间保存索引

### 第四步：最优解法 —— 哈希表

**核心洞察**：
- 当我们遍历到数字 `num` 时，只需要知道 `target - num` 是否在数组中
- 哈希表的查找时间复杂度是 O(1)
- 边遍历边存储，可以实现一次遍历完成

**算法步骤**：
1. 创建一个空哈希表，用于存储 `{数值: 索引}`
2. 遍历数组，对于每个元素 `num`：
   - 计算补数 `complement = target - num`
   - 如果补数在哈希表中，返回 `[哈希表[补数], 当前索引]`
   - 否则，将 `{num: 当前索引}` 存入哈希表

**为什么正确**：
- 当我们遍历到位置 `i` 时，哈希表中存储的是 `0` 到 `i-1` 的所有元素
- 如果 `target - nums[i]` 在哈希表中，说明之前存在某个位置 `j`，使得 `nums[i] + nums[j] = target`
- 由于题目保证有唯一解，且我们按顺序遍历，第一次找到的就是答案

---

## 完整代码实现

```python
from typing import List


class Solution:
    """
    两数之和 - 哈希表解法

    核心思路：
    - 遍历数组时，使用哈希表记录每个数值对应的索引
    - 对于当前元素num，检查(target - num)是否在哈希表中
    - 如果在，说明找到了答案；如果不在，将当前元素存入哈希表

    为什么用哈希表：
    - 哈希表的查找时间复杂度是O(1)
    - 将整体时间复杂度从O(n²)降低到O(n)

    时间复杂度：O(n) - 只需遍历数组一次
    空间复杂度：O(n) - 哈希表最多存储n个元素
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表：存储数值到索引的映射
        hashtable = dict()

        for i, num in enumerate(nums):
            # 计算需要找到的补数
            complement = target - num

            # 如果补数已在哈希表中，返回两个索引
            if complement in hashtable:
                return [hashtable[complement], i]

            # 将当前数值和索引存入哈希表
            hashtable[num] = i

        return []  # 题目保证有解，这里为了语法完整


# 测试代码
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in tests:
        result = sol.twoSum(nums, target)
        print(f"nums={nums}, target={target} -> {result}, expected={expected}")
```

---

## 示例推演

以 `nums = [2, 7, 11, 15], target = 9` 为例：

| 步骤 | i | num | complement | 哈希表状态 | 操作 |
|------|---|-----|-----------|-----------|------|
| 1 | 0 | 2 | 7 | {} | 7不在表中，存入{2:0} |
| 2 | 1 | 7 | 2 | {2:0} | **2在表中！返回[0,1]** |

成功找到答案 `[0, 1]`，因为 `nums[0] + nums[1] = 2 + 7 = 9`。

再以 `nums = [3, 2, 4], target = 6` 为例：

| 步骤 | i | num | complement | 哈希表状态 | 操作 |
|------|---|-----|-----------|-----------|------|
| 1 | 0 | 3 | 3 | {} | 3不在表中，存入{3:0} |
| 2 | 1 | 2 | 4 | {3:0} | 4不在表中，存入{3:0, 2:1} |
| 3 | 2 | 4 | 2 | {3:0, 2:1} | **2在表中！返回[1,2]** |

成功找到答案 `[1, 2]`，因为 `nums[1] + nums[2] = 2 + 4 = 6`。

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n²) | O(1) | 双重循环枚举所有组合 |
| 排序+双指针 | O(n log n) | O(n) | 需要排序和保存索引 |
| **哈希表（最优）** | **O(n)** | **O(n)** | 一次遍历完成 |

---

## 易错点总结

### 1. 先查表再存数

**错误写法**：先存入当前数，再查表
```python
# 错误！
hashtable[num] = i  # 先存
if target - num in hashtable:  # 再查
    ...
```

**正确写法**：先查表，再存数
```python
# 正确！
if target - num in hashtable:  # 先查
    ...
hashtable[num] = i  # 再存
```

**原因**：如果先存，可能会把同一个元素当成答案（例如 `target = 6, num = 3`，先存后查会找到刚存入的自己）。

### 2. 返回的是索引，不是数值

注意题目要求返回的是**数组下标**，不是数值本身。

### 3. 答案顺序

题目说可以按任意顺序返回答案，所以 `[0,1]` 和 `[1,0]` 都是正确的。

---

## 扩展思考

### 1. 如果数组是有序的？

如果数组已经有序，可以使用双指针法：
- 左指针指向开头，右指针指向结尾
- 和小于 target，左指针右移
- 和大于 target，右指针左移
- 时间复杂度 O(n)，空间复杂度 O(1)

### 2. 如果要求返回所有可能的组合？

如果存在多组解，需要修改代码收集所有结果，而不是找到一组就返回。

### 3. 如果数组中有重复元素？

哈希表解法天然支持重复元素，因为存储的是 `{值: 索引}`，即使值相同，索引也不同。

### 4. 三数之和

类似的问题 [15. 三数之和](https://leetcode.cn/problems/3sum/)，需要在两数之和的基础上再加一层循环，或使用双指针技巧。

---

## 相关题目

- [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)
- [15. 三数之和](https://leetcode.cn/problems/3sum/)
- [18. 四数之和](https://leetcode.cn/problems/4sum/)
- [1. 两数之和](https://leetcode.cn/problems/two-sum/)
