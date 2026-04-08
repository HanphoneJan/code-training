---
title: 排序
category: 算法
difficulty_range: [简单, 中等]
last_updated: 2026-03-23
---
# 排序

## 排序算法对比

[十大经典排序算法总结 | JavaGuide](https://javaguide.cn/cs-basics/algorithms/10-classical-sorting-algorithms.html)

|      排序算法      |      最好时间复杂度      |      平均时间复杂度      |      最差时间复杂度      |       空间复杂度       |      排序方式      |      稳定性      | 核心特点                                     |
| :----------------: | :----------------------: | :----------------------: | :----------------------: | :---------------------: | :----------------: | :--------------: | :------------------------------------------- |
|      冒泡排序      |         $O(n)$         |        $O(n^2)$        |        $O(n^2)$        |        $O(1)$        |      内部排序      |       稳定       | 仅教学用，实际不推荐                         |
|      选择排序      |        $O(n^2)$        |        $O(n^2)$        |        $O(n^2)$        |        $O(1)$        |      内部排序      |      不稳定      | 数据移动次数少，但不稳定                     |
|      插入排序      |         $O(n)$         |        $O(n^2)$        |        $O(n^2)$        |        $O(1)$        |      内部排序      |       稳定       | 小规模或基本有序时效率高                     |
|      希尔排序      |      $O(n\log n)$      |      $O(n\log n)$      |        $O(n^2)$        |        $O(1)$        |      内部排序      |      不稳定      | 插入排序的改进版                             |
| **归并排序** | **$O(n\log n)$** | **$O(n\log n)$** | **$O(n\log n)$** |   **$O(n)$**   | **外部排序** |  **稳定**  | **分治思想，性能稳定，适合链表**       |
| **快速排序** | **$O(n\log n)$** | **$O(n\log n)$** |   **$O(n^2)$**   | **$O(\log n)$** | **内部排序** | **不稳定** | **实际最常用，原地排序，平均性能优异** |
|  **堆排序**  | **$O(n\log n)$** | **$O(n\log n)$** | **$O(n\log n)$** |   **$O(1)$**   |      内部排序      |      不稳定      | **原地排序，适合 Top K 问题**          |
| **计数排序** |   **$O(n+k)$**   |   **$O(n+k)$**   |   **$O(n+k)$**   |   **$O(k)$**   | **外部排序** |  **稳定**  | **非比较排序，适用于小范围整数**       |
|       桶排序       |        $O(n+k)$        |        $O(n+k)$        |        $O(n^2)$        |       $O(n+k)$       |      外部排序      |       稳定       | 数据分布均匀时效率高                         |
|      基数排序      |     $O(n\times k)$     |     $O(n\times k)$     |     $O(n\times k)$     |       $O(n+k)$       |      外部排序      |       稳定       | 按位排序，适用于固定位数数据                 |

![十大排序算法对比表格图.webp](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%8D%81%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E5%AF%B9%E6%AF%94%E8%A1%A8%E6%A0%BC%E5%9B%BE.webp)

> **稳定**：相等元素排序后相对顺序不变。Python 的 `list.sort()` / `sorted()` 使用 Timsort（归并+插入的混合），**稳定**。

---

## 冒泡排序

* 外层循环：控制**要排几轮**
* 内层循环：控制**这一轮两两比较，每轮少比较i次**
* 交换：把大的数往后 “冒

$$
(n-1)+(n-2)+\cdots+1 = \frac{n(n-1)}{2}
$$

![冒泡排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)
仅用于教学，实际不推荐。

```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        flag = False         #  初始化标志位
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True  # 记录交换元素
        if not flag: break   # 内循环未交换任何元素，则跳出
```

---

## 归并排序

分治策略：将数组一分为二，分别排序后合并。

![归并排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F%E5%8A%A8%E5%9B%BE%E6%BC%94%E7%A4%BA.gif)

### 核心思想：先分后合

归并排序的核心是**合并两个已经有序的数组**。

1. **分**：将数组从中间分成两半，递归对每半排序
2. **治**：合并两个有序数组（双指针法）

**与快速排序的区别**：归并排序的"分"非常简单（直接中间劈开），但"合"需要额外工作；快速排序则相反，"分"比较复杂（要按大小重新排列），但不需要"合"。

### 示例推演

假设排序 `[38, 27, 43, 3]`：

**第一步：分解**

```
[38, 27, 43, 3]
    /        \
[38, 27]  [43, 3]
  /   \     /   \
[38] [27] [43] [3]
```

**第二步：合并**

```
[38] [27] → 比较 38 和 27 → [27, 38]
[43] [3]  → 比较 43 和 3  → [3, 43]

[27, 38] 和 [3, 43] 合并：
- 27 vs 3  → 取 3,  结果: [3],      右数组剩 [43]
- 27 vs 43 → 取 27, 结果: [3, 27],   左数组剩 [38]
- 38 vs 43 → 取 38, 结果: [3, 27, 38], 左数组空
- 右数组剩余 [43] 全部加入

最终结果: [3, 27, 38, 43]
```

### 代码实现

```python
def merge_sort(arr):
    """归并排序：稳定、O(nlog n)，但需要 O(n) 额外空间"""
    if len(arr) <= 1:
        return arr

    # 1. 分：从中间分成两半
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. 合：合并两个有序数组
    return merge(left, right)


def merge(arr1, arr2):
    """合并两个有序数组（双指针法）"""
    result = []
    i = j = 0

    # 双指针同时遍历，谁小取谁
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # <= 保证稳定性
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # 处理剩余元素
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```

### 复杂度分析

| 指标   | 复杂度          | 说明                                     |
| ------ | --------------- | ---------------------------------------- |
| 时间   | $O(n \log n)$ | 每层合并工作量$O(n)$，共 $\log n$ 层 |
| 空间   | $O(n)$        | 合并时需要临时数组                       |
| 稳定性 | 稳定            | 相等元素保持相对顺序（<= 保证）          |

---

## 快速排序

分治策略：选取基准，将数组划分为"小于基准"和"大于基准"两部分。

![快速排序动图演示.gif](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/快速排序动图演示.gif)

### 核心思想：先排后分

快速排序的核心是**分区**：把数组按基准值分成左右两部分。

1. **选基准**：从数组选一个元素作为 pivot
2. **分区**：重新排列，使小于 pivot 的在左，大于的在右
3. **递归**：对左右子数组递归排序。直至子数组长度为 1 时终止递归，即可完成对整个数组的排序。

**与归并排序的区别**：快速排序在递归**之前**就已经完成了排序（分区的过程就是排序），而归并排序是在递归**返回时**才进行排序（合并的过程）。

### 示例推演

假设排序 `[38, 27, 43, 3, 9, 82, 10]`，选最右元素 10 为 pivot：

**第一步：分区过程**

```
初始: [38, 27, 43, 3, 9, 82, 10]
       i                    pivot=10

j=0: 38>10，不交换，i保持-1
j=1: 27>10，不交换
j=2: 43>10，不交换
j=3: 3<=10，i++，交换 arr[0]和arr[3] → [3, 27, 43, 38, 9, 82, 10]
j=4: 9<=10，i++，交换 arr[1]和arr[4] → [3, 9, 43, 38, 27, 82, 10]
j=5: 82>10，不交换

最后：把 pivot 放到 i+1 位置
交换 arr[2]和arr[6] → [3, 9, 10, 38, 27, 82, 43]
                              ↑
                           pivot最终位置
```

**第二步：递归**

```
左半部分 [3, 9] 已有序
右半部分 [38, 27, 82, 43] 继续排序...
```

### 代码实现

```python
import random

def quick_sort(arr, left, right):
    """快速排序：平均 O(nlog n)，原地排序"""
    if left >= right:
        return

    # 分区，获取 pivot 的最终位置
    p = partition_random(arr, left, right)

    # 递归排序左右子数组
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


def partition_random(arr, left, right):
    """随机选择基准，避免最坏情况"""
    # 随机选基准，交换到最右
    random_idx = random.randint(left, right)
    arr[random_idx], arr[right] = arr[right], arr[random_idx]

    pivot = arr[right]
    i = left - 1  # i 指向已处理区间的最后一个位置

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 放到正确位置
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
```

### 复杂度分析

| 情况      | 时间复杂度      | 空间复杂度    | 说明                             |
| --------- | --------------- | ------------- | -------------------------------- |
| 最好/平均 | $O(n \log n)$ | $O(\log n)$ | 每次分区均匀，递归深度$\log n$ |
| 最坏      | $O(n^2)$      | $O(n)$      | 每次分区极不均匀（如数组已有序） |
| 稳定性    | -               | -             | 不稳定（会交换相等元素的位置）   |

> **为什么选随机基准？** 避免遇到已排序数组时退化为 $O(n^2)$。随机化后期望时间复杂度为 $O(n \log n)$。

---

## 堆排序

利用堆这种数据结构进行排序。堆是完全二叉树，分为大顶堆和小顶堆。

### 核心思想

1. **建堆**：将无序数组构建成堆（`heapify`，O(n)）
2. **排序**：反复将堆顶元素（最值）与末尾交换，然后对剩余元素重新调整堆

### 复杂度分析

- 建堆：$O(n)$
- 每次调整堆：$O(\log n)$
- 排序总时间：$O(n\log n)$
- 空间：$O(1)$（原地排序）

```python
import heapq


def heap_sort(arr):
    """堆排序：使用 Python 内置 heapq 模块"""
    # 方法1：直接 heapify
    heapq.heapify(arr)  # 原地建堆，O(n)
    # 依次弹出堆顶，得到有序数组
    return [heapq.heappop(arr) for _ in range(len(arr))]


def heap_sort_manual(arr):
    """手动实现堆排序（不使用 heapq）"""
    n = len(arr)

    # 建大顶堆（从最后一个非叶节点开始调整）
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

    # 排序：将堆顶（最大值）与末尾交换，然后调整剩余堆
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 最大值放到末尾
        heapify_down(arr, i, 0)  # 调整前 i 个元素

    return arr


def heapify_down(arr, n, i):
    """下沉调整：将以 i 为根的子树调整为大顶堆"""
    largest = i
    left = 2 * i + 1   # 左子节点
    right = 2 * i + 2  # 右子节点

    # 找出根、左子、右子中的最大值
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根，交换并继续调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, n, largest)
```

---

## 计数排序

非比较排序算法，适用于**数值范围较小**的整数排序。

### 核心思想

1. **统计频率**：遍历数组，统计每个数值出现的次数
2. **计算前缀和**：确定每个数值在结果数组中的最终位置
3. **稳定填充**：根据计数数组，将元素放到正确位置

### 适用条件

- 数据是**整数**（或可以映射为整数）
- 数据**范围不大**（$k$ 较小，最好 $k = O(n)$）
- 需要**稳定排序**

### 复杂度分析

- 时间：$O(n + k)$，$n$ 是元素个数，$k$ 是数值范围
- 空间：$O(k)$（计数数组）
- 稳定：是

```python
def counting_sort(arr):
    """
    计数排序：适用于小范围整数
    时间 O(n + k)，空间 O(k)
    """
    if not arr:
        return arr

    # 确定数值范围
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1  # 数值范围大小

    # 1. 统计频率
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1

    # 2. 计算前缀和（确定每个数值的结束位置）
    # count[i] 现在表示数值 (i + min_val) 在结果中的最后一个位置 + 1
    for i in range(1, k):
        count[i] += count[i - 1]

    # 3. 稳定填充（从后往前遍历，保证稳定性）
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        pos = count[num - min_val] - 1  # 该数值应该放的位置
        result[pos] = num
        count[num - min_val] -= 1  # 更新位置

    return result


# 简化版（非稳定，直接按计数展开）
def counting_sort_simple(arr):
    """简化版计数排序：非稳定，但代码更简洁"""
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    # 统计频率
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1

    # 按计数展开
    idx = 0
    for i in range(k):
        for _ in range(count[i]):
            arr[idx] = i + min_val
            idx += 1

    return arr
```

### 计数排序的应用场景

```python
# 场景1：年龄排序（范围小，0-150）
ages = [25, 18, 32, 25, 40, 18, 65]
sorted_ages = counting_sort(ages)

# 场景2：成绩排序（0-100分）
scores = [85, 92, 78, 85, 92, 60, 100]
sorted_scores = counting_sort(scores)

# 场景3：配合其他排序（基数排序的底层）
# 基数排序对每一位使用计数排序，实现 O(n*k) 的线性排序
```

---

## 桶排序

非比较排序算法，将数据分到有限数量的桶中，每个桶再分别排序。

### 核心思想

1. **分桶**：根据数据的取值范围，划分为若干个桶（区间）
2. **入桶**：将每个元素放入对应的桶中
3. **桶内排序**：对每个非空桶内部进行排序（通常用插入排序或递归桶排序）
4. **合并**：按顺序收集所有桶的元素

**与计数排序的区别**：计数排序每个桶只存一个值的出现次数，桶排序的每个桶存放的是一个区间范围内的多个值。

![桶排序示意图](https://hanphone.top/gh/HanphoneJan/public-pictures/algorithm/桶排序示意图.png)

### 适用条件

- 数据**分布比较均匀**（否则桶内数据量差异大）
- 数据范围可以**合理划分**成若干个区间
- 需要**稳定排序**时

### 示例推演

假设排序 `[0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]`：

**第一步：确定桶的数量和范围**

- 数据范围：0.32 ~ 0.52
- 创建 5 个桶，每个桶范围 0.05
  - 桶0: [0.30, 0.35)
  - 桶1: [0.35, 0.40)
  - 桶2: [0.40, 0.45)
  - 桶3: [0.45, 0.50)
  - 桶4: [0.50, 0.55]

**第二步：元素入桶**

```
0.42 → 桶2: [0.42]
0.32 → 桶0: [0.32]
0.33 → 桶0: [0.32, 0.33]
0.52 → 桶4: [0.52]
0.37 → 桶1: [0.37]
0.47 → 桶3: [0.47]
0.51 → 桶4: [0.52, 0.51]
```

**第三步：桶内排序**

```
桶0: [0.32, 0.33] （已有序）
桶1: [0.37] （只有一个元素）
桶2: [0.42] （只有一个元素）
桶3: [0.47] （只有一个元素）
桶4: [0.51, 0.52] → 排序后 [0.51, 0.52]
```

**第四步：合并结果**

```
[0.32, 0.33] + [0.37] + [0.42] + [0.47] + [0.51, 0.52]
= [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
```

### 代码实现

```python
def bucket_sort(arr, bucket_count=10):
    """
    桶排序：适用于数据分布均匀的情况
    平均 O(n)，最坏 O(n^2)
    """
    if not arr or len(arr) <= 1:
        return arr

    # 1. 确定数据范围
    min_val, max_val = min(arr), max(arr)

    # 2. 创建空桶
    buckets = [[] for _ in range(bucket_count)]

    # 3. 元素入桶
    # 计算每个元素应该放入哪个桶
    for num in arr:
        # 映射到 [0, bucket_count-1] 的区间
        idx = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[idx].append(num)

    # 4. 每个桶内排序（使用插入排序或内置排序）
    for bucket in buckets:
        bucket.sort()  # 小规模数据，用内置排序即可

    # 5. 合并结果
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result
```

### 复杂度分析

| 情况   | 时间复杂度     | 空间复杂度    | 说明                                |
| :----- | :------------- | :------------ | :---------------------------------- |
| 最好   | $O(n)$       | $O(n + k)$  | 数据均匀分布，每个桶内元素很少      |
| 平均   | $O(n)$       | $O(n + k)$  | 桶的数量 $k$ 与 $n$ 同数量级时    |
| 最坏   | $O(n^2)$     | $O(n + k)$  | 数据集中在少数桶内，退化为桶内排序  |
| 稳定性 | 稳定           | -             | 取决于桶内排序算法（使用稳定排序）  |

> **桶的数量如何选择？** 通常取 $k \approx n$，即桶的数量与元素数量相当。太多桶浪费空间，太少桶退化为普通排序。

### 桶排序的应用场景

```python
# 场景1：浮点数排序（范围在[0,1)之间）
floats = [0.42, 0.32, 0.33, 0.52, 0.37]
sorted_floats = bucket_sort(floats)

# 场景2：成绩分段排序（按10分一段）
scores = [85, 92, 78, 85, 92, 60, 100, 73, 88]
# 分桶：60-69, 70-79, 80-89, 90-100

def bucket_sort_scores(scores):
    """成绩按10分一段分桶排序"""
    buckets = [[] for _ in range(10)]  # 0-9, 10-19, ..., 90-100
    for s in scores:
        idx = min(s // 10, 9)  # 100分放到第9个桶
        buckets[idx].append(s)

    result = []
    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)
    return result

# 场景3：外部排序（海量数据无法一次加载）
# 将数据分桶后，每个桶可以独立加载到内存排序
```

---

## 算法选择指南

| 场景         | 推荐算法                       | 原因                                    |
| :----------- | :----------------------------- | :-------------------------------------- |
| 通用排序     | `list.sort()` / `sorted()` | Python 内置 Timsort，性能优异且稳定     |
| 需要稳定排序 | 归并排序                       | $O(n\log n)$ 且稳定                   |
| 空间敏感     | 快速排序、堆排序               | 原地排序，空间$O(\log n)$ 或 $O(1)$ |
| 链表排序     | 归并排序                       | 不需要随机访问，空间可优化到$O(1)$    |
| Top K 问题   | 堆排序 / 快速选择              | 堆可维护前 K 个，快速选择平均$O(n)$   |
| 数据范围小   | 计数排序                       | $O(n + k)$，可接近线性                |
| 部分有序数据 | 插入排序 / Timsort             | 接近$O(n)$                            |

---

## Python 内置排序

Python 的 `list.sort()` 和 `sorted()` 使用 **Timsort** 算法：

- **混合算法**：归并排序 + 插入排序
- **稳定性**：稳定排序（相等元素保持相对顺序）
- **自适应**：对部分有序数据接近 $O(n)$
- **最坏情况**：$O(n\log n)$

```python
# 基础用法
arr.sort()                          # 原地排序
new_arr = sorted(arr)               # 返回新列表

# 降序
arr.sort(reverse=True)

# 按 key 排序
arr.sort(key=lambda x: x[1])        # 按第二个元素排序
arr.sort(key=len)                   # 按长度排序
arr.sort(key=lambda x: (x[1], -x[0]))  # 多关键字：先按第2个升序，再按第1个降序

# 自定义比较函数（Python 3 需要 cmp_to_key）
from functools import cmp_to_key

def compare(a, b):
    """返回负数表示 a 在前，正数表示 b 在前"""
    if a[0] != b[0]:
        return a[0] - b[0]  # 按第一个元素升序
    return b[1] - a[1]      # 第一个相同则按第二个降序

arr.sort(key=cmp_to_key(compare))
```
