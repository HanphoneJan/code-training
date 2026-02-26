---
title: 三数之和
platform: LeetCode
difficulty: 中等
id: 15
url: https://leetcode.cn/problems/3sum/
tags:
  - 数组
  - 双指针
  - 排序
topics:
  - ../../topics/array.md
  - ../../topics/sorting.md
patterns:
  - ../../patterns/two_pointers.md
date_added: 2026-02-25
date_reviewed: []
---

# 0015. 三数之和

## 题目描述

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。

请你返回所有和为 `0` 且不重复的三元组。

## 解题思路

### 方法一：排序 + 双指针

1. 先对数组排序
2. 固定第一个数，使用双指针寻找另外两个数
3. 通过跳过重复元素来去重

- 时间复杂度：O(n²)
- 空间复杂度：O(log n)（排序的栈空间）

## 代码实现

### Python

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # 跳过重复元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # 跳过重复元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

## 相关题目

- [1. 两数之和](1)
- [16. 最接近的三数之和](16)

## 笔记

- 排序 + 双指针是处理多数之和问题的经典方法
- 去重是关键难点，需要在多个地方跳过重复元素
