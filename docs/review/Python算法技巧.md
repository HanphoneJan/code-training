---
title: Python算法技巧
category: 参考手册
last_updated: 2026-03-05
---
# Python算法技巧

> 本文档汇总Python算法竞赛/面试中常用的技巧和套路。

## 基础思维

### 递归、递推与枚举

| 方法           | 特点                     | 适用场景               |
| -------------- | ------------------------ | ---------------------- |
| **递归** | 函数调用自身，有归的过程 | 树的遍历、分治、回溯   |
| **递推** | 从已知推未知，循环实现   | 动态规划、斐波那契数列 |
| **枚举** | 遍历所有可能             | 小规模问题、验证答案   |

## 二分查找

### 标准模板

```python
def binary_search(arr: List[int], target: int) -> int:
    """在有序数组中查找target，返回索引，不存在返回-1"""
    left, right = 0, len(arr)  # 左闭右开区间
    while left < right:  # 不使用 <=：左闭右开写法更统一，循环结束时 left 即为答案位置
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid  # 收缩右边界到 mid
    return -1 if left >= len(arr) or arr[left] != target else left
```

### 二分查找变体

```python
# 查找第一个 >= target 的位置（下界）
def lower_bound(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# 查找第一个 > target 的位置（上界）
def upper_bound(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
```

## 前缀和

### 一维前缀和

```python
# 构建
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# 查询区间和 [l, r]
def range_sum(l: int, r: int) -> int:
    return prefix[r + 1] - prefix[l]
```

### 二维前缀和

```python
# 构建
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + matrix[i][j]

# 查询子矩阵和 [r1, c1] 到 [r2, c2]
def submatrix_sum(r1: int, c1: int, r2: int, c2: int) -> int:
    return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
```

## 差分

![](https://hanphone.top/gh/HanphoneJan/public_pictures/learn/Leetcode%E5%B7%AE%E5%88%86%E6%95%B0%E7%BB%84%E7%A4%BA%E4%BE%8B.webp)

```python
# 一维差分
diff = [0] * (n + 1)

# 区间 [l, r] 加 val
diff[l] += val
diff[r + 1] -= val

# 还原
arr = [0] * n
cur = 0
for i in range(n):
    cur += diff[i]
    arr[i] = cur
```

## 双指针

### 对撞指针

```python
def two_sum(arr: List[int], target: int) -> Tuple[int, int]:
    """在有序数组中找两数之和等于target"""
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1
    return -1, -1
```

### 快慢指针

```python
def find_duplicate(nums: List[int]) -> int:
    """Floyd判圈算法找环"""
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

## 滑动窗口

### 固定窗口大小

```python
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    from collections import deque
    q = deque()  # 存下标，保持单调递减
    res = []
    for i, x in enumerate(nums):
        # 移除窗口外的元素
        if q and q[0] <= i - k:
            q.popleft()
        # 保持单调性
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        # 记录结果
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

### 可变窗口大小

```python
def min_subarray_len(target: int, nums: List[int]) -> int:
    """找和 >= target 的最短子数组"""
    left = 0
    cur_sum = 0
    ans = float('inf')
    for right, x in enumerate(nums):
        cur_sum += x
        while cur_sum >= target:
            ans = min(ans, right - left + 1)
            cur_sum -= nums[left]
            left += 1
    return ans if ans != float('inf') else 0
```

## 位运算

```python
# 常用技巧
x & 1          # 判断奇偶
x & (x - 1)    # 消除最低位的1
x & (-x)       # 获取最低位的1
x | (1 << n)   # 将第n位置1
x & ~(1 << n)  # 将第n位置0
x ^ (1 << n)   # 翻转第n位

# 统计二进制中1的个数
bin(x).count('1')

# 判断是否是2的幂
x > 0 and (x & (x - 1)) == 0
```

## Python 内置函数巧用

### zip 函数

```python
# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))  # [(1, 4), (2, 5), (3, 6)]

# 同时遍历多个列表
for a, b in zip(list1, list2):
    print(a, b)
```

### enumerate 函数

```python
# 获取索引和值
for i, val in enumerate(arr):
    print(f"索引 {i}: 值 {val}")

# 指定起始索引
for i, val in enumerate(arr, 1):  # 从1开始
    print(i, val)
```

### itertools 模块

```python
from itertools import *

# 排列
permutations([1, 2, 3])  # 所有排列

# 组合
combinations([1, 2, 3], 2)  # 所有2个元素的组合

# 累加
accumulate([1, 2, 3, 4])  # [1, 3, 6, 10]

# 分组
groupby(sorted([1, 1, 2, 2, 3]))  # 按连续相同值分组
```

## 输入输出模板

### 快速读入（大量数据时）

```python
import sys
input = sys.stdin.readline

# 读取一行
n = int(input())
arr = list(map(int, input().split()))

# 读取多行
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
```

## 常用装饰器

### 记忆化搜索

```python
from functools import lru_cache, cache

@cache  # Python 3.9+
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@lru_cache(maxsize=None)  # Python 3.8 及以下
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

## 参考

- [LeetCode 算法面试题汇总](https://leetcode.cn/studyplan/top-100-liked/)
- [OI Wiki](https://oi-wiki.org/)
