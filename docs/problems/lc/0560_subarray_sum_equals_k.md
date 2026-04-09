---
title: 和为 K 的子数组
platform: LeetCode
difficulty: Medium
id: 560
url: https://leetcode.cn/problems/subarray-sum-equals-k/
tags:
  - 数组
  - 哈希表
  - 前缀和
topics:
  - ../../topics/prefix-sum.md
  - ../../topics/hash-table.md
patterns:
  - ../../patterns/subarray-sum.md
date_added: 2026-04-09
date_reviewed: []
---

# 560. 和为 K 的子数组

## 题目描述

给你一个整数数组 `nums` 和一个整数 `k`，请你统计并返回该数组中和为 `k` 的连续子数组的个数。

**示例 1：**
```
输入: nums = [1,1,1], k = 2
输出: 2
解释: 和为 2 的子数组有 [1,1] 和 [1,1]（下标 0-1 和 1-2）
```

**示例 2：**
```
输入: nums = [1,2,3], k = 3
输出: 2
解释: 和为 3 的子数组有 [1,2] 和 [3]
```

---

## 解题思路

### 第一步：理解问题本质

这道题要求统计「和为 k 的连续子数组」的个数。

**关键洞察：** 子数组和可以转化为前缀和之差。

定义 `prefix[i]` 为数组前 i 个元素的和（即 `nums[0] + nums[1] + ... + nums[i-1]`）。

则子数组 `nums[i:j]` 的和 = `prefix[j] - prefix[i]`

如果子数组和等于 k，则 `prefix[j] - prefix[i] = k`，即 `prefix[i] = prefix[j] - k`

### 第二步：暴力解法

**思路：** 枚举所有子数组，计算和是否等于 k。

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    ans += 1
        
        return ans
```

**为什么不够好？** 时间复杂度 O(n^2)，会超时。

### 第三步：优化解法 - 前缀和 + 哈希表

**关键洞察：** 利用前缀和之差，配合哈希表快速查找。

**算法步骤：**
1. 用哈希表 `cnt` 记录各个前缀和出现的次数
2. 初始化 `cnt[0] = 1`，表示前缀和为 0 的子数组有 1 个（空数组）
3. 遍历数组，累加得到当前前缀和 `curr_sum`
4. 以当前位置结尾的和为 k 的子数组个数 = `cnt[curr_sum - k]`
5. 将当前前缀和加入哈希表

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = curr_sum = 0
        
        for x in nums:
            curr_sum += x
            ans += cnt[curr_sum - k]
            cnt[curr_sum] += 1
        
        return ans
```

### 为什么不能使用滑动窗口？

**关键原因：** 数组中包含负数。

滑动窗口的前提是：当右指针右移时，如果窗口和大于 k，可以通过左移左指针来减小和。

但当数组中有负数时，右指针右移可能使和变小，左指针右移可能使和变大，无法确定指针移动方向。

---

## 完整代码实现

```python
from typing import List
from collections import defaultdict

class Solution:
    """
    和为 K 的子数组 - 前缀和 + 哈希表

    核心思路：
    利用前缀和的思想。子数组 nums[i:j] 的和 = prefix[j] - prefix[i]。
    如果和等于 k，则 prefix[i] = prefix[j] - k。
    用哈希表记录前缀和出现的次数，快速查找满足条件的子数组个数。

    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)  # 记录前缀和出现的次数
        cnt[0] = 1              # 前缀和为 0 的子数组有 1 个
        ans = 0                 # 和为 k 的子数组个数
        curr_sum = 0            # 当前前缀和

        for x in nums:
            curr_sum += x
            # 以当前位置结尾的和为 k 的子数组个数
            ans += cnt[curr_sum - k]
            cnt[curr_sum] += 1

        return ans
```

---

## 示例推演

以 `nums = [1, 1, 1], k = 2` 为例：

**遍历过程：**

| 步骤 | 当前元素 | 当前前缀和 | cnt[curr_sum-2] | 累计答案 | 哈希表状态 |
|------|----------|-----------|-----------------|----------|-----------|
| 初始 | - | 0 | - | 0 | {0: 1} |
| 1 | 1 | 1 | cnt[-1]=0 | 0 | {0: 1, 1: 1} |
| 2 | 1 | 2 | cnt[0]=1 | 1 | {0: 1, 1: 1, 2: 1} |
| 3 | 1 | 3 | cnt[1]=1 | 2 | {0: 1, 1: 1, 2: 1, 3: 1} |

**结果：** 2

**解释：**
- 步骤 2：前缀和为 2，cnt[0]=1 表示有 1 个前缀和为 0 的位置（下标 -1），子数组 [0:2] 即 [1,1] 和为 2
- 步骤 3：前缀和为 3，cnt[1]=1 表示有 1 个前缀和为 1 的位置（下标 0），子数组 [1:3] 即 [1,1] 和为 2

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力 | O(n^2) | O(1) | 枚举所有子数组 |
| 前缀和+哈希 | O(n) | O(n) | 线性时间 |

**说明：**
- n 是数组长度
- 哈希表最多存储 n+1 个不同的前缀和

---

## 易错点总结

### 1. 哈希表初始值

```python
# 必须初始化 cnt[0] = 1
cnt = defaultdict(int)
cnt[0] = 1

# 原因：前缀和为 curr_sum 的子数组本身可能就是答案
# 例如 nums = [3], k = 3，curr_sum = 3，需要 cnt[0] = 1
```

### 2. 更新顺序

```python
# 正确的顺序：先查询，再更新
ans += cnt[curr_sum - k]
cnt[curr_sum] += 1

# 如果先更新再查询，会把自己也算进去
```

### 3. 滑动窗口的误用

```python
# 错误：尝试用滑动窗口
# 原因：数组中有负数，无法确定指针移动方向
```

---

## 扩展思考

### 1. 如果需要返回具体的子数组？

可以用哈希表记录前缀和对应的所有下标，找到匹配时构造子数组。

### 2. 如果数组是二维的？

可以用二维前缀和，时间复杂度 O(m^2 × n^2) 或优化到 O(m × n × min(m,n))。

### 3. 相关题目

- [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/) - 树上的前缀和
- [974. 和可被 K 整除的子数组](https://leetcode.cn/problems/subarray-sums-divisible-by-k/) - 前缀和取模
- [525. 连续数组](https://leetcode.cn/problems/contiguous-array/) - 前缀和变形

---

## 相关题目

- [437. 路径总和 III](https://leetcode.cn/problems/path-sum-iii/)
- [974. 和可被 K 整除的子数组](https://leetcode.cn/problems/subarray-sums-divisible-by-k/)
- [525. 连续数组](https://leetcode.cn/problems/contiguous-array/)
