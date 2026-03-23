---
title: 排序
category: 算法
difficulty_range: [简单, 中等]
last_updated: 2026-02-25
---
# 排序

## 排序算法

[十大经典排序算法总结 | JavaGuide](https://javaguide.cn/cs-basics/algorithms/10-classical-sorting-algorithms.html)

| 排序算法           | 最好时间复杂度           | 平均时间复杂度           | 最差时间复杂度           | 空间复杂度              | 排序方式           | 稳定性           | 核心特点                                           |
| ------------------ | ------------------------ | ------------------------ | ------------------------ | ----------------------- | ------------------ | ---------------- | -------------------------------------------------- |
| 冒泡排序           | $O(n)$                 | $O(n^2)$               | $O(n^2)$               | $O(1)$                | 内部排序           | 稳定             | 简单易实现，适合小规模或基本有序的数据             |
| 选择排序           | $O(n^2)$               | $O(n^2)$               | $O(n^2)$               | $O(1)$                | 内部排序           | 不稳定           | 每轮选择最小元素交换，数据移动次数少               |
| 插入排序           | $O(n)$                 | $O(n^2)$               | $O(n^2)$               | $O(1)$                | 内部排序           | 稳定             | 局部有序时效率高，适合小规模数据                   |
| 希尔排序           | $O(n\log n)$           | $O(n\log n)$           | $O(n^2)$               | $O(1)$                | 内部排序           | 不稳定           | 插入排序的改进版，分组排序降低复杂度               |
| **归并排序** | **$O(n\log n)$** | **$O(n\log n)$** | **$O(n\log n)$** | **$O(n)$**      | **外部排序** | **稳定**   | **分治思想，适合外部分类，排序效率稳定**     |
| **快速排序** | **$O(n\log n)$** | **$O(n\log n)$** | **$O(n^2)$**     | **$O(\log n)$** | **内部排序** | **不稳定** | **实际应用最广泛，原地排序，分治划分效率高** |
| **堆排序**   | $O(n\log n)$           | $O(n\log n)$           | $O(n\log n)$           | $O(1)$                | 内部排序           | 不稳定           | 利用堆结构，原地排序，时间复杂度稳定               |
| 计数排序           | $O(n+k)$               | $O(n+k)$               | $O(n+k)$               | $O(k)$                | 外部排序           | 稳定             | 非比较排序，适用于数值范围较小的整数               |
| 桶排序             | $O(n+k)$               | $O(n+k)$               | $O(n^2)$               | $O(n+k)$              | 外部排序           | 稳定             | 分桶排序，桶内可结合其他排序算法                   |
| 基数排序           | $O(n\times k)$         | $O(n\times k)$         | $O(n\times k)$         | $O(n+k)$              | 外部排序           | 稳定             | 按位排序，适用于整数或字符串等固定长度数据         |

![十大排序算法对比表格图.webp](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%8D%81%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E5%AF%B9%E6%AF%94%E8%A1%A8%E6%A0%BC%E5%9B%BE.webp)

### 冒泡排序

仅用于教学
![冒泡排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)

```python
def bubble_sort(arr, left, right):
    if left >= right:  # 递归/循环终止条件：区间长度≤1无需排序
        return
    # 外层循环：控制排序轮数（每轮将当前区间最大元素"冒泡"到末尾）
    for i in range(left, right):
        swapped = False  # 优化：标记本轮是否发生交换，无交换则提前终止
        # 内层循环：逐个比较相邻元素，将最大元素逐步后移
        for j in range(left, right - (i - left)):
            if arr[j] > arr[j + 1]:  # 找到左边大于右边的元素对
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换相邻元素
                swapped = True
        if not swapped:  # 本轮无交换，说明区间已有序，直接退出
            break
```

### 归并排序

归并排序算法是一个**运用分治法的递归过程**，边界条件为当输入序列仅有一个元素时，直接返回，具体过程如下：

1. 如果输入内只有一个元素，则直接返回，否则将长度为 $n$ 的输入序列分成两个长度为 $n/2$ 的子序列；
2. 分别对这两个子序列进行归并排序，使子序列变为有序状态；
3. 设定两个指针，分别指向两个已经排序子序列的起始位置；
4. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间（用于存放排序结果），并移动指针到下一位置；
5. 重复步骤 3 ~ 4 直到某一指针达到序列尾；
6. 将另一序列剩下的所有元素直接复制到合并序列尾。

![归并排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)

```python
def merge_sort(arr):
    """
    归并排序的主函数，递归拆分数组并调用合并函数
    :param arr: 待排序的整数列表
    :return: 排序后的整数列表
    """
    # 基线条件：数组长度小于等于1时直接返回（已有序）
    if len(arr) <= 1:
        return arr
  
    # 找到数组中间位置，拆分左右两部分
    middle = len(arr) // 2
    arr_1 = arr[:middle]  # 对应Java的Arrays.copyOfRange(arr, 0, middle)
    arr_2 = arr[middle:]  # 对应Java的Arrays.copyOfRange(arr, middle, arr.length)
  
    # 递归排序左右子数组，然后合并结果
    return merge(merge_sort(arr_1), merge_sort(arr_2))


def merge(arr_1, arr_2):
    """
    合并两个已经排好序的数组
    :param arr_1: 第一个有序数组
    :param arr_2: 第二个有序数组
    :return: 合并后的有序数组
    """
    # 初始化结果数组，长度为两个输入数组长度之和
    sorted_arr = [0] * (len(arr_1) + len(arr_2))
    idx = 0   # 结果数组的指针
    idx_1 = 0 # 第一个数组的指针
    idx_2 = 0 # 第二个数组的指针
  
    # 同时遍历两个数组，按大小将元素放入结果数组
    while idx_1 < len(arr_1) and idx_2 < len(arr_2):
        if arr_1[idx_1] < arr_2[idx_2]:
            sorted_arr[idx] = arr_1[idx_1]
            idx_1 += 1
        else:
            sorted_arr[idx] = arr_2[idx_2]
            idx_2 += 1
        idx += 1
  
    # 处理第一个数组的剩余元素
    if idx_1 < len(arr_1):
        while idx_1 < len(arr_1):
            sorted_arr[idx] = arr_1[idx_1]
            idx_1 += 1
            idx += 1
    # 处理第二个数组的剩余元素
    else:
        while idx_2 < len(arr_2):
            sorted_arr[idx] = arr_2[idx_2]
            idx_2 += 1
            idx += 1
  
    return sorted_arr
```

### 快速排序

快速排序用到了分治思想，同样的还有归并排序。乍看起来快速排序和归并排序非常相似，都是将问题变小，先排序子串，最后合并。不同的是快速排序在划分子问题的时候经过多一步处理，将划分的两组数据划分为一大一小，这样在最后合并的时候就不必像归并排序那样再进行比较。但也正因为如此，划分的不定性使得快速排序的时间复杂度并不稳定。

快速排序使用分治法（Divide and conquer）策略来把一个序列分为较小和较大的 2 个子序列，然后递归地排序两个子序列。具体算法描述如下：

1. **选择基准（Pivot）** ：从数组中选一个元素作为基准。为了避免最坏情况，通常会随机选择。
2. **分区（Partition）** ：重新排列序列，将所有比基准值小的元素摆放在基准前面，所有比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个操作结束之后，该基准就处于数列的中间位置。
3. **递归（Recurse）** ：递归地把小于基准值元素的子序列和大于基准值元素的子序列进行快速排序。

**关于性能，这也是它与归并排序的关键区别：**

- **平均和最佳情况：** 它的时间复杂度是 $O(nlogn)$。这种情况发生在每次分区都能把数组分成均等的两半。
- **最坏情况：** 它的时间复杂度会退化到 $O(n^2)$。这发生在每次我们选的基准都是当前数组的最小值或最大值时，比如对一个已经排好序的数组，每次都选第一个元素做基准，这就会导致分区极其不均，算法退化成类似冒泡排序。这就是为什么**随机选择基准**非常重要。

![快速排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)
使用中间值作为基准点，还行。

```python
def quick_sort(arr, left, right):
	if left >= right: # 递归终止条件
		return
	i, j = left, right
	pivot = arr[(left + right) // 2] # 选择中间值作为基准点
	while i <= j:
		while arr[i] < pivot: # 找到左边第一个大于等于 pivot 的元素
			i += 1
		while arr[j] > pivot: # 找到右边第一个小于等于 pivot 的元素
			j -= 1
		if i <= j:
			arr[i], arr[j] = arr[j], arr[i] # 交换元素
			i += 1
			j -= 1
	quick_sort(arr, left, j) # 对左半部分递归排序
	quick_sort(arr, i, right) # 对右半部分递归排序
```

```python
import random

class Solution:
    def sortArray(self, a):
        """sortArray 方法，对外提供排序接口"""
        self.quick(a, 0, len(a) - 1)
        return a
  
    def quick(self, a, left, right):
        """quick 递归函数，核心递归排序逻辑"""
        if left >= right:  # 递归终止条件：区间无元素或只有一个元素
            return
        # 调用分区函数，获取基准值的最终位置
        p = self.partition(a, left, right)
        # 递归排序左子数组 [left, p-1]
        self.quick(a, left, p - 1)
        # 递归排序右子数组 [p+1, right]
        self.quick(a, p + 1, right)
  
    def partition(self, a, left, right):
        """partition 分区函数，返回基准值的最终位置"""
        # 1. 随机生成 [left, right] 范围内的基准索引（对齐 Java 的 ThreadLocalRandom）
        # random.randint(left, right) 等价于 Java 的 nextInt(right-left+1)+left
        random_pivot_idx = random.randint(left, right)
        # 2. 将随机基准点交换到区间最左端（left 位置）
        self.swap(a, left, random_pivot_idx)
        # 3. 确定基准值（pv）：此时 left 位置是随机选中的基准元素
        pv = a[left]
        # 4. 初始化双指针：i 从 left+1 开始，j 从 right 开始
        i = left + 1
        j = right
  
        while i <= j:
            # 左指针向右找第一个 >= pv 的元素
            while i <= j and a[i] < pv:
                i += 1
            # 右指针向左找第一个 <= pv 的元素
            while i <= j and a[j] > pv:
                j -= 1
            # 交换不符合位置的元素，同时移动指针
            if i <= j:
                self.swap(a, i, j)
                i += 1
                j -= 1
  
        # 5. 将基准值（left 位置）交换到分区点 j 位置（基准的最终正确位置）
        self.swap(a, j, left)
        # 返回基准值的最终索引，作为递归的分区点
        return j
  
    def swap(self, a, i, j):
        """swap 方法，交换数组中两个元素的位置"""
        a[i], a[j] = a[j], a[i]

```

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


### 堆排序
