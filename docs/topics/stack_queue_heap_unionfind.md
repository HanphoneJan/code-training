---
title: 栈、队列、堆与并查集
category: 数据结构
difficulty_range: [简单, 中等]
last_updated: 2026-03-05
---

# 栈、队列、堆与并查集

## 栈（Stack）

### 核心概念

栈是一种**后进先出（LIFO）**的数据结构，核心操作：
- **入栈（Push）**：向栈顶添加元素
- **出栈（Pop）**：从栈顶移除元素
- **查看栈顶（Peek）**：获取栈顶元素不移除

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

队列是一种**先进先出（FIFO）**的数据结构，核心操作：
- **入队（Enqueue）**：向队尾添加元素
- **出队（Dequeue）**：从队头移除元素

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

### 循环队列

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

### 双端队列（Deque）

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

---

## 堆（Heap）

### 核心概念

堆是**完全二叉树**，用数组（顺序表）存储：
- **大顶堆**：父节点值 ≥ 所有子节点值，根节点是最大值
- **小顶堆**：父节点值 ≤ 所有子节点值，根节点是最小值

核心操作是「上浮（Sift Up）」和「下沉（Sift Down）」。

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
