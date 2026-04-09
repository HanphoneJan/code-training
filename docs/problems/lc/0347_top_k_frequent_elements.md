---
title: 前 K 个高频元素
platform: LeetCode
difficulty: Medium
id: 347
url: https://leetcode.cn/problems/top-k-frequent-elements/
tags:
  - 数组
  - 哈希表
  - 堆
  - 桶排序
topics:
  - ../../topics/heap.md
  - ../../topics/hash-table.md
patterns:
  - ../../patterns/top-k.md
date_added: 2026-04-09
date_reviewed: []
---

# 347. 前 K 个高频元素

## 题目描述

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

**示例 1：**
```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例 2：**
```
输入: nums = [1], k = 1
输出: [1]
```

**提示：**
- 1 <= nums.length <= 10^5
- k 的取值范围是 [1, 数组中不相同的元素的个数]
- 题目数据保证答案唯一，即数组中前 k 个高频元素的集合是唯一的

**进阶：** 所设计算法的时间复杂度必须优于 O(n log n)，其中 n 是数组大小。

---

## 解题思路

### 第一步：理解问题本质

这道题的核心是**统计频率 + 找出前 k 大**。

可以拆解为两个子问题：
1. 统计每个元素出现的次数
2. 从所有元素中找出出现次数最多的 k 个

### 第二步：暴力解法

**思路：** 用哈希表统计频率，然后对所有频率排序，取前 k 个。

```python
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频率
        freq_map = Counter(nums)
        # 按频率降序排序，取前 k 个
        sorted_items = sorted(freq_map.items(), key=lambda x: -x[1])
        return [num for num, _ in sorted_items[:k]]
```

**为什么不够好？** 排序的时间复杂度是 O(n log n)，其中 n 是不同元素的个数。当数据量很大时，效率不够高。

### 第三步：优化解法 - 最小堆

**关键洞察：** 我们只需要前 k 个，不需要对所有元素排序。

**思路：** 维护一个大小为 k 的最小堆：
- 堆中保存当前频率最高的 k 个元素
- 堆顶是这 k 个元素中频率最小的
- 遇到频率更高的元素时，替换堆顶

```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        
        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
        
        return [num for _, num in heap]
```

**复杂度：** 时间 O(n log k)，空间 O(n + k)

### 第四步：最优解法 - 桶排序

**关键洞察：** 频率的范围是 1 到 n（数组长度），可以用桶排序达到 O(n)。

**思路：**
1. 统计每个元素的频率
2. 创建桶数组，下标表示频率，值是该频率的所有元素
3. 从高频率往低频率收集元素，直到收集够 k 个

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        
        # 桶排序：下标是频率，值是该频率的元素列表
        buckets = [[] for _ in range(max_cnt + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        
        # 从高频率往低频率收集
        ans = []
        for freq in range(max_cnt, 0, -1):
            ans.extend(buckets[freq])
            if len(ans) >= k:
                return ans[:k]
        
        return ans[:k]
```

---

## 完整代码实现

```python
from typing import List
from collections import Counter
import heapq

class Solution:
    """
    前 K 个高频元素 - 堆排序解法

    核心思路：
    1. 使用 Counter 统计每个元素的出现频率
    2. 维护一个大小为 k 的最小堆
    3. 堆顶元素是 k 个高频元素中频率最小的
    4. 当遇到频率更高的元素时，替换堆顶元素

    时间复杂度: O(n log k)
    空间复杂度: O(n + k)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素的出现频率
        freq_map = Counter(nums)

        # 维护一个大小为 k 的最小堆
        heap = []
        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                # 堆已满，如果当前频率大于堆顶，替换堆顶
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))

        return [num for _, num in heap]
```

---

## 示例推演

以 `nums = [1,1,1,2,2,3], k = 2` 为例：

**第一步：统计频率**
```
元素: 频率
1: 3
2: 2
3: 1
```

**第二步：维护大小为 2 的最小堆**

| 步骤 | 当前元素 | 频率 | 堆状态 | 操作 |
|------|----------|------|--------|------|
| 1 | 1 | 3 | [(3, 1)] | 堆未满，直接入堆 |
| 2 | 2 | 2 | [(2, 2), (3, 1)] | 堆未满，直接入堆 |
| 3 | 3 | 1 | [(2, 2), (3, 1)] | 堆已满，1 < 堆顶2，跳过 |

**最终结果：** 从堆中提取元素 [1, 2]

---

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| 暴力排序 | O(n log n) | O(n) | 对所有频率排序 |
| 最小堆 | O(n log k) | O(n + k) | 只维护 k 个元素 |
| 桶排序 | O(n) | O(n) | 利用频率范围有限的特点 |

**说明：**
- n 是数组长度
- 最小堆解法在 k << n 时优势明显
- 桶排序达到理论最优，但需要额外空间

---

## 易错点总结

### 1. 最大堆 vs 最小堆的选择

**错误思路：** 用最大堆直接取前 k 个。

**问题：** 最大堆需要将所有元素入堆，空间复杂度 O(n)。

**正确做法：** 用最小堆维护 k 个元素，空间复杂度 O(k)。

### 2. heapreplace 与 heappushpop 的区别

```python
# heapreplace: 先替换堆顶，再调整堆
heapq.heapreplace(heap, (freq, num))  # 推荐

# heappushpop: 先入堆新元素，再弹出堆顶
heapq.heappushpop(heap, (freq, num))  # 不推荐，多一次操作
```

### 3. Counter 的使用技巧

```python
# 获取频率最高的 k 个元素（面试时可能被禁止）
Counter(nums).most_common(k)

# 遍历频率字典
for num, freq in freq_map.items():
    pass
```

---

## 扩展思考

### 1. 为什么桶排序可以达到 O(n)？

因为频率的范围是确定的（1 到数组长度），属于**范围有限的整数排序**，适合用桶排序。

### 2. 如果要求按频率降序输出？

堆解法的结果是无序的，如果需要有序，可以对结果再排序：
```python
result = [num for _, num in heap]
result.sort(key=lambda x: -freq_map[x])
```

### 3. 相关题目

- [692. 前K个高频单词](https://leetcode.cn/problems/top-k-frequent-words/) - 需要处理相同频率的字典序
- [973. 最接近原点的 K 个点](https://leetcode.cn/problems/k-closest-points-to-origin/) - 类似的 Top K 问题
- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) - 经典 Top K 问题

---

## 相关题目

- [692. 前K个高频单词](https://leetcode.cn/problems/top-k-frequent-words/)
- [973. 最接近原点的 K 个点](https://leetcode.cn/problems/k-closest-points-to-origin/)
- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
