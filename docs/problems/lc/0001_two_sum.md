---
title: 两数之和
platform: LeetCode
difficulty: 简单
id: 1
url: https://leetcode.cn/problems/two-sum/
tags:
  - 数组
  - 哈希表
topics:
  - ../../topics/array.md
  - ../../topics/hash_table.md
patterns:
  - ../../patterns/hash_map.md
date_added: 2026-02-25
date_reviewed: []
---

# 0001. 两数之和

## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target` 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

## 解题思路

### 方法一：哈希表

- 使用哈希表存储已遍历的元素及其索引
- 对于每个元素 `nums[i]`，检查 `target - nums[i]` 是否在哈希表中
- 时间复杂度：O(n)
- 空间复杂度：O(n)

## 代码实现

### Python

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []
```

### C++

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> hashmap;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (hashmap.find(complement) != hashmap.end()) {
            return {hashmap[complement], i};
        }
        hashmap[nums[i]] = i;
    }
    return {};
}
```

## 相关题目

- [15. 三数之和](15)
- [18. 四数之和](18)

## 笔记

- 典型的空间换时间思路
- 哈希表是解决查找问题的常用数据结构
