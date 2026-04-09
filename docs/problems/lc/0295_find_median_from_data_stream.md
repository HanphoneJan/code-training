---
title: 数据流的中位数
platform: LeetCode
difficulty: Hard
id: 295
url: https://leetcode.cn/problems/find-median-from-data-stream/
tags:
  - 堆
  - 设计
  - 数据结构
date_added: 2026-04-09
---

# 295. 数据流的中位数

## 题目描述

**中位数**是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如：
- `[2,3,4]` 的中位数是 `3`
- `[2,3]` 的中位数是 `(2 + 3) / 2 = 2.5`

设计一个支持以下两种操作的数据结构：

- `void addNum(int num)` - 从数据流中添加一个整数到数据结构中。
- `double findMedian()` - 返回目前所有元素的中位数。

**示例 1：**

```
输入：
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出：[null, null, null, 1.5, null, 2.0]

解释：
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // 返回 2.0
```

**提示：**
- `-10^5 <= num <= 10^5`
- 在调用 `findMedian` 之前，数据结构中至少有一个元素
- 最多 `5 * 10^4` 次调用 `addNum` 和 `findMedian`

**进阶：**
- 如果数据流中所有整数都在 0 到 100 范围内，如何优化？
- 如果数据流中 99% 的整数都在 0 到 100 范围内，如何优化？

---

## 解题思路

### 第一步：理解问题本质

需要在数据流中动态维护中位数，支持：
1. 插入操作 `addNum`
2. 查询中位数 `findMedian`

关键要求：
- 插入操作要高效
- 查询中位数要 O(1)

### 第二步：暴力解法

使用数组存储所有元素，查询时排序后取中位数。

```python
class MedianFinderBrute:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0
```

**为什么不够好？**
- `addNum` 是 O(1)，但 `findMedian` 是 O(n log n)
- 每次查询都排序，效率太低

### 第三步：优化解法 - 有序列表

维护一个有序列表，插入时使用二分查找定位。

```python
import bisect

class MedianFinderSorted:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)  # O(n) 插入

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0
```

**复杂度分析：**
- `addNum`: O(n) - 插入有序列表需要移动元素
- `findMedian`: O(1)

### 第四步：最优解法 - 双堆

使用两个堆将数据流分成两部分：
- **大顶堆**：保存较小的一半，堆顶是较小部分的最大值
- **小顶堆**：保存较大的一半，堆顶是较大部分的最小值

**平衡条件：**
- 元素总数为偶数时，两个堆大小相等
- 元素总数为奇数时，小顶堆比大顶堆多一个元素

**插入策略：**
1. 当前总元素为偶数时，新元素先放入大顶堆，再将大顶堆堆顶放入小顶堆
2. 当前总元素为奇数时，新元素先放入小顶堆，再将小顶堆堆顶放入大顶堆

---

## 完整代码实现

```python
from heapq import heappush, heappushpop


class MedianFinder:
    """
    295. 数据流的中位数 - 双堆解法

    核心思路：
    维护两个堆，将数据流分成"较小的一半"和"较大的一半"。

    堆的设计：
    - 大顶堆 B（用负数存入小顶堆）：保存较小的一半，堆顶是较小部分的最大值
    - 小顶堆 A：保存较大的一半，堆顶是较大部分的最小值

    平衡条件：
    - 元素总数为偶数时，两个堆大小相等
    - 元素总数为奇数时，A 比 B 多一个元素（这样中位数就是 A 的堆顶）

    插入策略：
    1. 当前总元素为偶数时，新元素先放入 B，再将 B 的堆顶放入 A
       （保证 A 多一个元素，且 A 的堆顶是中位数）
    2. 当前总元素为奇数时，新元素先放入 A，再将 A 的堆顶放入 B
       （保证两个堆大小相等，中位数是两堆顶的平均）

    时间复杂度:
    - addNum: O(log n) - 堆的插入和弹出操作
    - findMedian: O(1) - 直接访问堆顶

    空间复杂度: O(n) - 存储所有元素
    """

    def __init__(self):
        """
        初始化两个堆
        A: 小顶堆，保存较大的一半
        B: 大顶堆（用负数模拟），保存较小的一半
        """
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半（用负数存入小顶堆）

    def addNum(self, num: int) -> None:
        """
        向数据流中添加一个数
        保持平衡：A 的大小等于 B，或比 B 多 1
        """
        if len(self.A) != len(self.B):
            # 当前 A 比 B 多一个，新元素加入后要平衡
            # 先将 num 加入 A，再将 A 的堆顶移到 B
            heappush(self.B, -heappushpop(self.A, num))
        else:
            # 当前 A 和 B 相等，新元素加入后 A 多一个
            # 先将 num 加入 B，再将 B 的堆顶移到 A
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        """
        获取当前中位数
        - 元素个数为奇数：A 的堆顶
        - 元素个数为偶数：两堆顶的平均值
        """
        if len(self.A) != len(self.B):
            # A 比 B 多一个，中位数就是 A 的堆顶
            return float(self.A[0])
        else:
            # 两堆大小相等，中位数是堆顶的平均
            # B 中存的是负数，所以用减法
            return (self.A[0] - self.B[0]) / 2.0
```

---

## 示例推演

以操作序列 `[1, 2, findMedian, 3, findMedian]` 为例：

**初始状态：** `A = [], B = []`

**addNum(1)：**
```
A 和 B 大小相等（都是 0）
- 将 1 加入 B（存为 -1）: B = [-1]
- 将 B 堆顶移到 A: A = [1], B = []

结果: A = [1], B = []
```

**addNum(2)：**
```
A 比 B 多 1 个
- 将 2 加入 A: A 变为 [1, 2]（堆结构）
- 将 A 堆顶移到 B: A = [2], B = [-1]

结果: A = [2], B = [-1]
```

**findMedian()：**
```
A 和 B 大小相等（都是 1）
中位数 = (A[0] - B[0]) / 2 = (2 - 1) / 2 = 1.5
```

**addNum(3)：**
```
A 和 B 大小相等
- 将 3 加入 B（存为 -3）: B = [-3, -1]
- 将 B 堆顶移到 A: A = [2, 3], B = [-1]

结果: A = [2, 3], B = [-1]
```

**findMedian()：**
```
A 比 B 多 1 个（2 个 vs 1 个）
中位数 = A[0] = 2
```

---

## 复杂度分析

| 解法 | addNum | findMedian | 空间复杂度 | 说明 |
|------|--------|-----------|-----------|------|
| 暴力 | O(1) | O(n log n) | O(n) | 每次查询排序 |
| 有序列表 | O(n) | O(1) | O(n) | 插入需要移动元素 |
| 双堆 | O(log n) | O(1) | O(n) | 最优解法 |

---

## 易错点总结

### 1. Python 只有小顶堆

**正确做法：** 大顶堆用负数模拟。
```python
heappush(self.B, -num)    # 存入负数
-num = heappop(self.B)     # 取出后取反
```

### 2. 平衡条件的维护

**正确做法：**
```python
if len(self.A) != len(self.B):
    # A 多一个，新元素处理后要平衡
    heappush(self.B, -heappushpop(self.A, num))
else:
    # 相等，新元素处理后 A 多一个
    heappush(self.A, -heappushpop(self.B, -num))
```

### 3. heappushpop 的使用

`heappushpop(heap, item)` 先 push 再 pop，比分开调用更高效。

### 4. 中位数计算

```python
if len(self.A) != len(self.B):
    return float(self.A[0])           # 奇数个
else:
    return (self.A[0] - self.B[0]) / 2.0  # 偶数个，注意 B 存的是负数
```

---

## 扩展思考

### 1. 相关题目

- [480. 滑动窗口中位数](https://leetcode.cn/problems/sliding-window-median/) - 双堆 + 延迟删除
- [502. IPO](https://leetcode.cn/problems/ipo/) - 双堆应用

### 2. 进阶问题

**如果数据流中所有整数都在 0 到 100 范围内，如何优化？**

使用计数数组（桶排序思想）：
```python
class MedianFinder:
    def __init__(self):
        self.count = [0] * 101
        self.total = 0

    def addNum(self, num: int) -> None:
        self.count[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        # 通过前缀和找到中位数位置
        mid = (self.total + 1) // 2
        cumsum = 0
        for i in range(101):
            cumsum += self.count[i]
            if cumsum >= mid:
                if self.total % 2 == 1:
                    return float(i)
                # 找第二个中位数
                if cumsum > mid:
                    return float(i)
                # 第二个中位数在后面的桶
                for j in range(i + 1, 101):
                    if self.count[j] > 0:
                        return (i + j) / 2.0
```

时间复杂度：
- `addNum`: O(1)
- `findMedian`: O(101) = O(1)

### 3. 延迟删除技巧

对于滑动窗口中位数问题，需要删除离开窗口的元素。可以使用"延迟删除"：
- 使用哈希表记录待删除元素
- 当堆顶元素在待删除集合中时，才真正删除
