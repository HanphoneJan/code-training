---
title: Python数据结构速查
category: 参考手册
last_updated: 2026-03-05
---

# Python数据结构速查

> 本文档汇总Python中常用的数据结构及其方法，便于快速查阅。

## 字符串 str

### 常用方法

```python
# 格式化与转换
format(*args, **kwargs)      # 格式化字符串，算法中可用于进制转换
split(sep=None, maxsplit=-1) # 以sep分割字符串
strip([chars])               # 去除首尾字符，默认去除 \r, \n, " "
join(iterable)               # 拼接字符串，如 ','.join(['leet', 'code']) => "leet,code"
replace(old, new[, count])   # 字符串替换

# 查询与判断
count(sub[, start[, end]])   # 统计子串出现次数
startswith(prefix)           # 是否以prefix开头
endswith(suffix)             # 是否以suffix结尾
find(sub)                    # 查找子串位置，找不到返回-1
index(sub)                   # 查找子串位置，找不到抛出异常

# 其他
ord(c)                       # 字符转ASCII码
chr(i)                       # ASCII码转字符
```

### 算法应用

```python
# 进制转换示例（LeetCode 191. Number of 1 Bits）
bin(n).count('1')            # 统计二进制中1的个数
format(n, 'b')               # 转为二进制字符串
format(n, 'o')               # 转为八进制字符串
format(n, 'x')               # 转为十六进制字符串
```

---

## 列表 list

> Python列表的底层数据结构是一个**动态数组**，支持动态扩展。

### 常用方法

```python
# 排序与反转
lst.sort(*, key=None, reverse=False)  # 原地排序
lst.reverse()                         # 原地反转

# 增删改查
lst.append(val)       # 末尾添加元素
lst.extend(t)         # 批量添加，等价于 lst += t
lst.insert(i, val)    # 在位置i插入元素
lst.pop([i])          # 移除并返回指定位置元素（默认最后一个）
lst.remove(val)       # 移除第一个值为val的元素
lst.clear()           # 清空列表
lst.count(val)        # 统计val出现次数
lst.index(val)        # 查找val的索引

# 其他
lst.copy()            # 浅拷贝
len(lst)              # 列表长度
```

### 列表推导式

```python
# 基本用法
squares = [x**2 for x in range(10)]

# 带条件
evens = [x for x in range(10) if x % 2 == 0]

# 二维列表初始化（注意浅拷贝问题）
matrix = [[0] * n for _ in range(m)]  # 正确
# matrix = [[0] * n] * m              # 错误！所有行引用同一列表
```

---

## 字典 dict

### 常用方法

```python
# 访问与修改
d[key]                    # 访问键值，不存在抛出KeyError
d.get(key, default)       # 安全访问，不存在返回default
d.setdefault(key, val)    # 如key不存在则设置默认值
d.update(other)           # 批量更新

# 删除
d.pop(key[, default])     # 删除并返回指定键值
d.popitem()               # 删除并返回最后一个键值对（LIFO顺序）
d.clear()                 # 清空字典

# 视图对象
d.keys()                  # 返回键的视图
d.values()                # 返回值的视图
d.items()                 # 返回键值对的视图

# 构造技巧
dict.fromkeys(iterable, value)  # 用可迭代对象创建字典，值都为value
```

### 迭代技巧

```python
# 遍历键值对
for k, v in d.items():
    print(k, v)

# 按键排序遍历
for k in sorted(d):
    print(k, d[k])

# 按值排序遍历
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)
```

---

## 集合 set

### 常用方法

```python
# 添加删除
s.add(val)                # 添加元素
s.remove(val)             # 删除元素，不存在则报错
s.discard(val)            # 删除元素，不存在不报错
s.pop()                   # 随机移除并返回一个元素
s.clear()                 # 清空集合

# 集合运算
s1 | s2    # 并集
s1 & s2    # 交集
s1 - s2    # 差集
s1 ^ s2    # 对称差集（异或）

# 判断
val in s                  # 判断元素是否在集合中
s1.issubset(s2)           # s1是否是s2的子集
s1.issuperset(s2)         # s1是否是s2的超集
```

### 去重与计数

```python
# 列表去重（保持顺序）
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]

# 利用集合快速查找
lookup = set(lst)         # O(n)构建，O(1)查询
```

---

## collections 模块

### Counter 计数器

```python
from collections import Counter

# 创建
cnt = Counter([1, 1, 2, 3, 3, 3])  # Counter({3: 3, 1: 2, 2: 1})
cnt = Counter('abracadabra')       # Counter({'a': 5, 'b': 2, ...})

# 常用操作
cnt.most_common(n)        # 返回出现次数最多的n个元素
cnt.elements()            # 返回所有元素的可迭代对象
cnt.total()               # 返回所有计数总和（Python 3.10+）

# 运算
c1 + c2                   # 计数相加
c1 - c2                   # 计数相减（只保留正数）
c1 & c2                   # 取最小计数
c1 | c2                   # 取最大计数
```

### defaultdict 默认字典

```python
from collections import defaultdict

# 自动为不存在的键提供默认值
dd = defaultdict(list)    # 默认值为空列表
dd = defaultdict(int)     # 默认值为0
dd = defaultdict(set)     # 默认值为空集合

# 示例：分组
groups = defaultdict(list)
for key, val in pairs:
    groups[key].append(val)  # 无需检查key是否存在
```

### deque 双端队列

```python
from collections import deque

# 创建
dq = deque(maxlen=3)      # 可设置最大长度，满了自动弹出左侧元素

# 操作
dq.append(x)              # 右侧添加
dq.appendleft(x)          # 左侧添加
dq.pop()                  # 右侧弹出
dq.popleft()              # 左侧弹出（队列的标准出队操作）
dq.extend(iterable)       # 右侧批量添加
dq.extendleft(iterable)   # 左侧批量添加
dq.rotate(n)              # 旋转，正数向右，负数向左
dq.clear()                # 清空

# 可用作栈和队列！
```

---

## heapq 堆模块

> 堆是完全二叉树，用数组存储。Python的heapq实现的是**小顶堆**。

### 基础操作

```python
import heapq

# 创建堆
heap = []
heapq.heappush(heap, x)           # 插入元素
min_val = heapq.heappop(heap)     # 弹出最小值

# 原地堆化（O(n)）
arr = [5, 4, 3, 2, 1]
heapq.heapify(arr)                # 转为小顶堆

# 进阶操作
heapq.heappushpop(heap, x)        # 先插入再弹出（比分开调用高效）
heapq.heapreplace(heap, x)        # 先弹出再插入（与heappushpop顺序相反）

# Top K问题
heapq.nsmallest(k, iterable)      # 返回最小的k个元素
heapq.nlargest(k, iterable)       # 返回最大的k个元素
heapq.nsmallest(k, iterable, key=lambda x: x[1])  # 支持自定义key
```

### 大顶堆技巧

```python
# 通过插入负值实现大顶堆
max_heap = []
heapq.heappush(max_heap, -x)      # 插入负值
max_val = -heapq.heappop(max_heap) # 弹出后取负

# 示例：从数量最多的堆取走礼物（LeetCode 2558）
def pickGifts(self, gifts: List[int], k: int) -> int:
    for i in range(len(gifts)):
        gifts[i] *= -1
    heapify(gifts)
    while k and -gifts[0] > 1:
        heapreplace(gifts, -isqrt(-gifts[0]))
        k -= 1
    return -sum(gifts)
```

### 堆排序

```python
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# 示例
print(heap_sort([7, 2, 5, 1, 8, 3]))  # [1, 2, 3, 5, 7, 8]
```

---

## 列表 vs 数组 vs 链表

| 特性 | Python列表 | array.array | 链表 |
|------|-----------|-------------|------|
| 存储方式 | 动态数组（连续内存） | 连续内存 | 非连续内存 |
| 随机访问 | O(1) | O(1) | O(n) |
| 头部插入 | O(n) | O(n) | O(1) |
| 尾部插入 | O(1)均摊 | O(1)均摊 | O(1)（已知尾节点）|
| 内存开销 | 较小 | 小 | 较大（需存储指针）|
| 元素类型 | 任意 | 固定 | 任意 |

```python
import array

# array模块用于大规模数值计算，类型固定
arr = array.array('i', [1, 2, 3])  # 'i'表示有符号整数
```

---

## 参考

- [Python官方文档 - 内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)
- [collections模块文档](https://docs.python.org/zh-cn/3/library/collections.html)
- [heapq模块文档](https://docs.python.org/zh-cn/3/library/heapq.html)
