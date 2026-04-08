---
title: 栈、队列、堆与并查集
category: 数据结构
difficulty_range: [简单, 中等]
last_updated: 2026-03-23
---

# 栈、队列、堆与并查集

## 栈（Stack）

### 核心概念

**栈 (Stack)** 只允许在有序的线性数据集合的一端（称为栈顶 top）进行加入数据（push）和移除数据（pop）。按照 **后进先出（LIFO, Last In First Out）** 的原理运作。在栈中，push 和 pop 的操作都发生在栈顶。

栈常用一维数组或链表来实现，用数组实现的栈叫作 **顺序栈** ，用链表实现的栈叫作 **链式栈** 。

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 访问 | O(n) | 最坏情况需要遍历 |
| 插入删除 | O(1) | 顶端插入和删除元素 |

### Python实现

```python
# 使用列表实现栈
stack = []
stack.append(x)      # 入栈 O(1)
stack.pop()          # 出栈 O(1)
stack[-1]            # 查看栈顶 O(1)
len(stack) == 0      # 判断是否为空
```

### 单调栈

**核心思想**：及时去掉无用数据，保证栈中数据有序。

用于解决：下一个更大/更小元素、股票价格跨度等问题。

```python
# 下一个更大元素模板
# 倒序遍历，维护一个从栈底到栈顶递减的栈
def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # 存下标
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = nums[stack[-1]]
        stack.append(i)
    return res
```

### 栈的应用场景

- **浏览器回退和前进**：使用两个栈实现前进后退功能
- **检查符号是否成对出现**：如括号匹配问题
- **反转字符串**：利用后进先出特性
- **维护函数调用**：程序调用栈的实现
- **深度优先遍历（DFS）**：在深度优先搜索过程中，栈被用来保存搜索路径，以便回溯到上一层

### 例题：基本计算器

[224. 基本计算器](https://leetcode.cn/problems/basic-calculator/)

```python
def calculate(self, s: str) -> int:
    ops = [1]              # 维护括号层级的符号栈，初始默认正号
    sign = 1               # 当前数字的运算符号
    ret = 0                # 最终计算结果
    n = len(s)
    i = 0
    while i < n:
        if s[i] == ' ':    # 跳过空格
            i += 1
        elif s[i] == '+':  # 遇到加号，继承栈顶层级符号
            sign = ops[-1]
            i += 1
        elif s[i] == '-':  # 遇到减号，栈顶层级符号取反
            sign = -ops[-1]
            i += 1
        elif s[i] == '(':  # 左括号，当前符号入栈
            ops.append(sign)
            i += 1
        elif s[i] == ')':  # 右括号，弹出当前层级符号
            ops.pop()
            i += 1
        else:              # 数字，解析完整数字
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            ret += num * sign
    return ret
```

---

## 队列（Queue）

### 核心概念

**队列（Queue）** 是 **先进先出 (FIFO，First In, First Out)** 的线性表。在具体应用中通常用链表或者数组来实现，用数组实现的队列叫作 **顺序队列** ，用链表实现的队列叫作 **链式队列** 。队列只允许在后端（rear）进行插入操作也就是入队 enqueue，在前端（front）进行删除操作也就是出队 dequeue。

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 访问 | O(n) | 最坏情况需要遍历 |
| 插入删除 | O(1) | 后端插入前端删除元素 |

### 队列分类

#### 单队列（顺序队列）

为了避免当只有一个元素的时候，队头和队尾重合使处理变得麻烦，所以引入两个指针，**front 指针指向对头元素，rear 指针指向队列最后一个元素的下一个位置**，这样当 front 等于 rear 时，此队列不是还剩一个元素，而是空队列。

**顺序队列存在"假溢出"的问题**也就是明明有位置却不能添加的情况，还可能出现 rear 指针越界。实际很少用。

#### 循环队列

循环队列可以解决顺序队列的假溢出和越界问题。

顺序队列中，我们说 `front==rear` 的时候队列为空，循环队列中则不一样，也可能为满。解决办法有两种：

1. **设置标志变量**：设置一个标志变量 `flag`，当 `front==rear` 并且 `flag=0` 的时候队列为空，当 `front==rear` 并且 `flag=1` 的时候队列为满。
   - 入队时，只要队列不满，先赋值再移动 `rear`，若移动后 `front==rear`，说明队列满，置 `flag=1`
   - 出队时，只要队列不空，先取值再移动 `front`，若移动后 `front==rear`，说明队列空，置 `flag=0`

2. **牺牲一个空间**：队列为空的时候就是 `front==rear`，队列满的时候，我们保证数组还有一个空闲的位置，rear 就指向这个空闲位置，判断队列是否为满的条件是：`(rear+1) % QueueSize==front`。虽然牺牲了一个空间，但简洁方便。

#### 双端队列（Deque）

**双端队列 (Deque)** 是一种在队列的两端都可以进行插入和删除操作的队列，比单队列更加灵活常用，并且完全覆盖了栈。

#### 优先队列（Priority Queue）

**优先队列 (Priority Queue)** 从底层结构上来讲并非线性的数据结构，它一般是由堆来实现的。

- 在每个元素入队时，优先队列会将新元素其插入堆中并调整堆
- 在队头出队时，优先队列会返回堆顶元素并调整堆

虽然优先队列的底层并非严格的线性结构，但是在我们使用的过程中，我们是感知不到**堆**的，从使用者的眼中优先队列可以被认为是一种线性的数据结构：一种会自动排序的线性队列。

### Python实现

```python
from collections import deque

# 使用deque实现队列（推荐使用）
queue = deque()
queue.append(x)        # 入队 O(1)
queue.popleft()        # 出队 O(1)
queue[0]               # 查看队首 O(1)

# 不推荐使用list的pop(0)，时间复杂度O(n)
```

### 循环队列实现

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_size = k
        self.size = 0        # 当前元素个数
        self.front = 0       # 队首指针
        self.rear = 0        # 队尾指针

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        last_index = (self.rear - 1) % self.max_size
        return self.queue[last_index]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
```

### 双端队列

```python
from collections import deque

q = deque(maxlen=3)   # 可设置最大长度，满了自动弹出左侧
q.append(1)           # 右侧追加
q.appendleft(2)       # 左侧追加
q.pop()               # 右侧弹出
q.popleft()           # 左侧弹出（队列的标准出队操作）
q.extend([3,4])       # 右侧批量追加
q.rotate(1)           # 向右旋转

# 双端队列可以同时用作栈和队列！
```

### 队列的应用场景

当我们需要按照一定顺序来处理数据的时候可以考虑使用队列这个数据结构。

- **阻塞队列**：阻塞队列可以看成在队列基础上加了阻塞操作的队列。当队列为空的时候，出队操作阻塞，当队列满的时候，入队操作阻塞。使用阻塞队列我们可以很容易实现"生产者 - 消费者"模型。
- **线程池中的请求/任务队列**：当线程池中没有空闲线程时，新的任务请求线程资源会被如何处理呢？答案是这些任务会被放入任务队列中，等待线程池中的线程空闲后再从队列中取出任务执行。
- **栈**：双端队列天生便可以实现栈的全部功能（`push`、`pop` 和 `peek`），并且在 Deque 接口中已经实现了相关方法。Stack 类已经和 Vector 一样被遗弃，现在在 Java 中**普遍使用双端队列（Deque）来实现栈**。
- **广度优先搜索（BFS）**：在图的广度优先搜索过程中，队列被用于存储待访问的节点，保证按照层次顺序遍历图的节点。
- **Linux 内核进程队列**（按优先级排队）
- **现实生活中的派对，播放器上的播放列表**
- **消息队列**

---

## 堆（Heap）

### 核心概念

堆是**完全二叉树**，用数组（顺序表）存储：
- **大顶堆**：父节点值 ≥ 所有子节点值，根节点是最大值
- **小顶堆**：父节点值 ≤ 所有子节点值，根节点是最小值

堆中的每一个节点值都大于等于（或小于等于）子树中所有节点的值。或者说，任意一个节点的值都大于等于（或小于等于）所有子节点的值。

堆通常基于完全二叉树实现的，所以在插入和删除数据时，只需要在二叉树中上下移动节点，时间复杂度为 `O(log(n))`，堆初始化的时间复杂度为 `O(n)`。（**二叉**）堆是一个数组，它可以被看成是一个 **近似的完全二叉树**。

核心操作是「上浮（Sift Up）」和「下沉（Sift Down）」。

### 数组存储的二叉堆

![数组存储的二叉堆示例图.webp](https://hanphone.top/gh/HanphoneJan/public-pictures/datastructure/%E6%95%B0%E7%BB%84%E5%AD%98%E5%82%A8%E7%9A%84%E4%BA%8C%E5%8F%89%E5%A0%86%E7%A4%BA%E4%BE%8B%E5%9B%BE.webp)

堆用数组存储完全二叉树，节点 i 的父子关系：
- 父节点索引：`(i - 1) // 2`
- 左子节点索引：`2 * i + 1`
- 右子节点索引：`2 * i + 2`

### 堆的手动实现

```python
class MinHeap:
    """小顶堆手动实现"""

    def __init__(self):
        self.heap = []  # 使用数组存储堆

    def _parent(self, i: int) -> int:
        """获取父节点索引"""
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        """获取左子节点索引"""
        return 2 * i + 1

    def _right(self, i: int) -> int:
        """获取右子节点索引"""
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        """交换两个位置的元素"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i: int):
        """上浮：将索引i处的元素向上调整"""
        parent = self._parent(i)
        # 如果当前节点小于父节点，交换并继续上浮
        if i > 0 and self.heap[i] < self.heap[parent]:
            self._swap(i, parent)
            self._sift_up(parent)

    def _sift_down(self, i: int):
        """下沉：将索引i处的元素向下调整"""
        min_idx = i
        left = self._left(i)
        right = self._right(i)

        # 找出当前节点和左右子节点中的最小值
        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right

        # 如果最小值不是当前节点，交换并继续下沉
        if i != min_idx:
            self._swap(i, min_idx)
            self._sift_down(min_idx)

    def push(self, x: int):
        """插入元素"""
        self.heap.append(x)           # 先放到末尾
        self._sift_up(len(self.heap) - 1)  # 再上浮到正确位置

    def pop(self) -> int:
        """弹出堆顶元素"""
        if not self.heap:
            raise IndexError("pop from empty heap")

        min_val = self.heap[0]
        last_val = self.heap.pop()

        # 如果堆不为空，将最后一个元素放到堆顶，然后下沉
        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return min_val

    def peek(self) -> int:
        """查看堆顶元素"""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0
```

### 堆操作详解

#### 插入元素（上浮 Sift Up）

1. 将要插入的元素放到数组最后
2. 比较该元素与其父节点，如果小于父节点则交换
3. 重复步骤2，直到该元素大于等于父节点或到达根节点

**时间复杂度**：$O(\log n)$，最坏情况需要从叶子节点上浮到根节点。

#### 删除堆顶（下沉 Sift Down）

1. 将堆顶元素（最小值）保存，用于返回
2. 将数组最后一个元素移到堆顶位置
3. 比较该元素与其左右子节点，如果大于较小的子节点则交换
4. 重复步骤3，直到该元素小于等于两个子节点或到达叶子节点

**时间复杂度**：$O(\log n)$，最坏情况需要从根节点下沉到叶子节点。

#### 建堆（Heapify）

对一个无序数组，从最后一个非叶子节点开始，自底向下执行下沉操作。

```python
def _heapify(self):
    """将无序数组堆化，O(n)"""
    # 从最后一个非叶子节点开始下沉
    # 最后一个非叶子节点的索引是 (n-2)//2 = n//2 - 1
    for i in range(len(self.heap) // 2 - 1, -1, -1):
        self._sift_down(i)
```

**为什么时间复杂度是 $O(n)$ 而不是 $O(n \log n)$？**

虽然看起来要对 $n/2$ 个节点各做一次下沉（$O(\log n)$），但实际上大部分节点的高度很小。通过数学推导可得，建堆的总时间复杂度为 $O(n)$。

### heapq模块

```python
import heapq

# 基础操作
heap = []
heapq.heappush(heap, x)           # 插入元素
heapq.heappop(heap)               # 弹出最小值
heapq.heapify(arr)                # 原地堆化 O(n)

# 进阶操作
heapq.heappushpop(heap, x)        # 先插入再弹出
heapq.heapreplace(heap, x)        # 先弹出再插入

# Top K问题
heapq.nsmallest(k, nums)          # 返回最小的k个元素
heapq.nlargest(k, nums)           # 返回最大的k个元素
```

### 大顶堆实现

```python
import heapq

# 通过插入负值实现大顶堆
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, -x)

    def pop(self):
        return -heapq.heappop(self.heap)

    def top(self):
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)
```

### 堆排序

堆排序的过程分为两步：

- **第一步是建堆**，将一个无序的数组建立为一个堆。建堆的过程就是一个对所有非叶节点的自顶向下堆化过程。如果节点个数为 n，那么我们需要对 n/2 到 1 的节点进行自顶向下（沉底）堆化。注意，顺序是从后往前堆化。
- **第二步是排序**，将堆顶元素取出放到数组末尾（也就是与数组末尾元素交换），然后对剩下的元素进行堆化，反复迭代，直到所有元素被取出为止。

```python
import heapq

def heap_sort(arr):
    """堆排序：使用 Python 内置 heapq 模块"""
    heapq.heapify(arr)  # 原地建堆，O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

### 例题：从数量最多的堆取走礼物

[2558. 从数量最多的堆取走礼物](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/)

```python
def pickGifts(self, gifts: List[int], k: int) -> int:
    for i in range(len(gifts)):
        gifts[i] *= -1
    heapq.heapify(gifts)
    while k and -gifts[0] > 1:
        heapq.heapreplace(gifts, -isqrt(-gifts[0]))
        k -= 1
    return -sum(gifts)
```

---

## 并查集（Union-Find）

### 核心概念

并查集用于解决：
- 判断两个元素是否属于同一集合
- 某个元素在哪个集合
- 合并两个集合

操作均摊时间复杂度接近 **O(α(n))**，α为阿克曼函数的反函数，可视为常数。

### 模板实现

```python
class UnionFind:
    def __init__(self, n: int):
        # 代表元数组：fa[x]表示x所在集合的代表元
        self._fa = list(range(n))
        # 集合大小
        self._size = [1] * n
        # 连通块个数
        self.cc = n

    def find(self, x: int) -> int:
        """查找x所在集合的代表元（带路径压缩）"""
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # 路径压缩
        return self._fa[x]

    def is_same(self, x: int, y: int) -> bool:
        """判断x和y是否在同一个集合"""
        return self.find(x) == self.find(y)

    def merge(self, from_: int, to: int) -> bool:
        """合并两个集合"""
        x, y = self.find(from_), self.find(to)
        if x == y:  # 已经在同一集合
            return False
        self._fa[x] = y
        self._size[y] += self._size[x]
        self.cc -= 1
        return True

    def get_size(self, x: int) -> int:
        """获取x所在集合的大小"""
        return self._size[self.find(x)]
```

### 最小生成树（Kruskal算法）

```python
def mstKruskal(n: int, edges: List[List[int]]) -> int:
    """
    计算图的最小生成树的边权之和
    如果图不连通，返回math.inf
    edges: [(u, v, weight), ...]
    """
    edges.sort(key=lambda e: e[2])  # 按边权排序

    uf = UnionFind(n)
    sum_wt = 0
    for x, y, wt in edges:
        if uf.merge(x, y):  # 如果合并成功，说明这条边在MST中
            sum_wt += wt

    if uf.cc > 1:  # 图不连通
        return float('inf')
    return sum_wt
```

---

## 相关题目

### 栈
- [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)
- [224. 基本计算器](https://leetcode.cn/problems/basic-calculator/)
- [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/)（单调栈）

### 队列
- [622. 设计循环队列](https://leetcode.cn/problems/design-circular-queue/)
- [933. 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/)

### 堆
- [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
- [2558. 从数量最多的堆取走礼物](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/)

### 并查集
- [547. 省份数量](https://leetcode.cn/problems/number-of-provinces/)
- [684. 冗余连接](https://leetcode.cn/problems/redundant-connection/)

---

## 参考

- [并查集详解 - CSDN](https://blog.csdn.net/the_zed/article/details/105126583)
- [Python heapq文档](https://docs.python.org/zh-cn/3/library/heapq.html)
