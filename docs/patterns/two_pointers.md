---
title: 双指针模式
category: 算法模式
difficulty: 简单-中等
applicable_to:
  - 数组
  - 链表
  - 字符串
last_updated: 2026-02-25
---

# 双指针模式

## 模式概述

双指针是一种常见的算法技巧，使用两个指针在数据结构中移动，以解决特定问题。

## 适用场景

1. **有序数组**中查找满足特定条件的元素对
2. **数组去重**或**原地修改**
3. **回文判断**
4. **快慢指针**检测环

## 模式分类

### 1. 对撞指针

两个指针分别从两端向中间移动。

**特点：**
- 一个指针从头开始，另一个从尾开始
- 向中间靠拢
- 通常用于有序数组

**模板：**

```python
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # 处理逻辑
        if condition_met:
            # 找到答案
            return result
        elif need_increase:
            left += 1
        else:
            right -= 1
    
    return default_result
```

**应用题目：**
- TBD
- 两数之和 II（有序数组）
- 盛最多水的容器

### 2. 快慢指针

两个指针以不同速度移动。

**特点：**
- 同向移动
- 速度不同
- 常用于链表环检测、数组去重

**模板：**

```python
def two_pointer_fast_slow(arr):
    slow = 0
    
    for fast in range(len(arr)):
        if condition_met:
            arr[slow] = arr[fast]
            slow += 1
    
    return slow  # 或 arr[:slow]
```

**应用题目：**
- 删除有序数组中的重复项
- 移动零
- 链表环检测

### 3. 滑动窗口

特殊的双指针，维护一个窗口。

详见 [滑动窗口模式](sliding_window.md)

## 实战案例

### 案例 1：三数之和

```python
def threeSum(nums):
    nums.sort()  # 先排序
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # 去重
        
        # 使用双指针查找另外两个数
        left, right = i + 1, len(nums) - 1
        
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

### 案例 2：数组去重

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1
```

## 解题步骤

1. **判断是否适用双指针**
   - 是否需要遍历数组？
   - 是否需要比较两个位置的元素？
   - 是否有序或需要排序？

2. **选择双指针类型**
   - 对撞指针：有序数组，查找元素对
   - 快慢指针：去重，原地修改
   - 滑动窗口：子数组/子串问题

3. **确定移动条件**
   - 什么时候移动左指针？
   - 什么时候移动右指针？
   - 终止条件是什么？

4. **处理边界情况**
   - 空数组
   - 单元素数组
   - 重复元素

## 时间复杂度

- 通常为 O(n) 或 O(n²)（嵌套循环）
- 相比暴力解法（O(n²) 或 O(n³)）有显著优化

## 相关知识点

- [数组](../topics/array.md)
- [滑动窗口](sliding_window.md)
- [排序](../topics/sorting.md)

## 练习题目

**简单：**
- 删除有序数组中的重复项
- 移动零
- 反转字符串

**中等：**
- TBD
- 盛最多水的容器
- 长度最小的子数组

**困难：**
- 接雨水
- 最小覆盖子串

## 总结

双指针是一种简单但强大的技巧：
- ✅ 降低时间复杂度
- ✅ 节省空间（原地操作）
- ✅ 代码简洁清晰

关键是识别使用场景和选择合适的指针移动策略。
