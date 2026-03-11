---
title: 排序
category: 算法
difficulty_range: [简单, 中等]
last_updated: 2026-02-25
---

# 排序

## 知识点概述

排序是将一组数据按照特定顺序排列的过程。

## 常见排序算法

### 1. 冒泡排序

- 时间复杂度：O(n²)
- 空间复杂度：O(1)
- 稳定性：稳定

### 2. 选择排序

- 时间复杂度：O(n²)
- 空间复杂度：O(1)
- 稳定性：不稳定

### 3. 插入排序

- 时间复杂度：O(n²)
- 空间复杂度：O(1)
- 稳定性：稳定

### 4. 快速排序

- 时间复杂度：平均 O(n log n)，最坏 O(n²)
- 空间复杂度：O(log n)
- 稳定性：不稳定

### 5. 归并排序

- 时间复杂度：O(n log n)
- 空间复杂度：O(n)
- 稳定性：稳定

### 6. 堆排序

- 时间复杂度：O(n log n)
- 空间复杂度：O(1)
- 稳定性：不稳定

## 常见题型

### 1. 排序应用

- 数组排序
- 自定义比较器

### 2. 排序优化

- 快速选择
- 部分排序

**相关题目：**
- TBD

## 快速排序模板

```python
def quick_sort(arr, left, right):
    if left >= right:
        return
    
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
```

## 相关知识点

- [数组](array.md)
- [双指针](../patterns/two_pointers.md)

## 题目列表

**中等：**
- TBD
