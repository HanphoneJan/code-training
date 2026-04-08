---
title: Python数据结构速查
category: 参考手册
last_updated: 2026-03-23
---
# Python数据结构速查

> 本文档汇总Python中常用的数据结构及其方法，便于快速查阅。

---

## 复杂度速查总览

| 操作 | list | dict / set | deque | heapq |
|---|---|---|---|---|
| 随机访问 `a[i]` | O(1) | — | O(n) | O(1) 仅堆顶 |
| 末尾增删 | O(1) 均摊 | — | O(1) | O(log n) |
| **头部增删** | **O(n)** | — | **O(1)** | — |
| 中间插入/删除 | O(n) | — | O(n) | — |
| `val in 容器` | **O(n)** 线性扫描 | **O(1)** 均摊 | O(n) | — |
| 排序 `.sort()` | O(n log n) | — | — | O(n log n) |
| 原地堆化 `heapify` | — | — | — | **O(n)** |
| 二分查找 `bisect` | O(log n) | — | — | — |
| 构建 `Counter/dict` | — | O(n) | — | — |

> **核心结论**：判断"某元素是否存在"，用 `set` / `dict`（O(1)）而非 `list`（O(n)）。

---

## 字符串 str

### 底层实现

CPython 中字符串是**不可变的 Unicode 字符序列**，根据字符范围自动选择存储方式：
- Latin-1 范围（≤ U+00FF）→ 每字符 1 字节
- BMP 范围（≤ U+FFFF）→ 每字符 2 字节
- 全 Unicode → 每字符 4 字节

不可变意味着**任何修改操作都会创建新字符串**，因此循环拼接字符串要用 `''.join(list)` 而非 `+=`（后者是 O(n²)）。

```
# 为什么 join 比 += 快？
# s += x 每次都要申请新内存、复制旧内容 → 累计 O(n²)
# ''.join(parts) 先算总长度、一次申请、一次写入 → O(n)
```

| 操作 | 时间复杂度 | 说明 |
|---|---|---|
| `s[i]` 索引 | O(1) | 直接偏移计算 |
| `s[a:b]` 切片 | O(k) k=切片长度 | 创建新字符串 |
| `s1 + s2` 拼接 | O(n+m) | 创建新字符串 |
| `sub in s` | O(n·m) 最坏 | CPython用优化过的Boyer-Moore-Horspool |
| `s.find/index` | O(n·m) 最坏 | 同上 |
| `s.split/join` | O(n) | 线性扫描 |
| `s.replace` | O(n) | 线性扫描 + 新建 |

### 常用方法

```python
# 格式化与转换
format(*args, **kwargs)      # 格式化字符串，算法中可用于进制转换
split(sep=None, maxsplit=-1) # 以sep分割字符串，不指定则按空白符分割
splitlines([keepends=False]) # 按行分割，返回行列表（不包含
），keepends=True则保留

strip([chars])               # 去除首尾字符，默认去除 \r, \n, " "
lstrip([chars])              # 只去除左侧
rstrip([chars])              # 只去除右侧
join(iterable)               # 拼接字符串，如 ','.join(['leet', 'code']) => "leet,code"
replace(old, new[, count])   # 字符串替换

# 查询与判断
count(sub[, start[, end]])   # 统计子串出现次数
startswith(prefix)           # 是否以prefix开头
endswith(suffix)             # 是否以suffix结尾
find(sub[, start[, end]])    # 查找子串位置，找不到返回 -1
index(sub[, start[, end]])   # 查找子串位置，找不到抛出 ValueError
rfind(sub)                   # 从右向左查找
rindex(sub)                  # 从右向左查找，找不到抛出异常

# 类型判断
isdigit()                    # 是否全为数字字符
isalpha()                    # 是否全为字母
isalnum()                    # 是否全为字母或数字
isspace()                    # 是否全为空白字符
isupper()                    # 是否全为大写字母
islower()                    # 是否全为小写字母

# 大小写转换
upper()                      # 全部大写
lower()                      # 全部小写
capitalize()                 # 首字母大写
title()                      # 每个单词首字母大写
swapcase()                   # 大小写互换

# 对齐填充
center(width[, fillchar])    # 居中对齐
ljust(width[, fillchar])     # 左对齐（右侧填充）
rjust(width[, fillchar])     # 右对齐（左侧填充）
zfill(width)                 # 左侧填充 '0'

# 字符编码
ord(c)                       # 字符转ASCII码，如 ord('a') => 97
chr(i)                       # ASCII码转字符，如 chr(97) => 'a'
```

### 算法应用

```python
# 进制转换（LeetCode 191. Number of 1 Bits）
bin(n)                       # 转为二进制字符串，如 bin(10) => '0b1010'
bin(n).count('1')            # 统计二进制中1的个数
oct(n)                       # 转为八进制字符串
hex(n)                       # 转为十六进制字符串
format(n, 'b')               # 转为二进制字符串（无前缀）
format(n, '08b')             # 转为8位二进制字符串（不足补0）
format(n, 'o')               # 转为八进制字符串（无前缀）
format(n, 'x')               # 转为十六进制字符串（无前缀）

# 字符串与数字互转
num = int("123")             # 字符串转整数
num = int("ff", 16)          # 十六进制字符串转整数
num = int("1010", 2)         # 二进制字符串转整数
s = str(123)                 # 整数转字符串

# 字符处理技巧
chars = list("hello")        # 字符串转字符列表
s = ''.join(chars)           # 字符列表转字符串
s[::-1]                      # 反转字符串
sorted(s)                    # 返回排序后的字符列表（不改变原字符串）

# eval：将字符串作为表达式计算（谨慎使用）
eval("1 + 2")                # => 3
eval("'hello'.upper()")      # => 'HELLO'
```

---

## 列表 list

### 底层实现

CPython 中 list 是**动态数组（array of pointers）**，存储的是指向 PyObject 的指针数组，而非元素本身。

**扩容策略**（不是翻倍，而是 ~1.125 倍）：
```
新容量 = 旧容量 + (旧容量 >> 3) + (旧容量 < 9 ? 3 : 6)
# 即：0→4→8→16→25→35→46→58→72→88...
```
均摊下来 `append` 是 O(1)。每次扩容需复制所有指针，代价是 O(n)，但触发频率低。

**`val in lst` 的实现**：逐一比较每个元素（先比地址，相同则返回 True；否则调用 `__eq__`），最坏 O(n)，找不到时必须扫完全部。

```python
# 演示：list 的 in 是 O(n) 线性扫描
lst = list(range(10_000_000))
val = 9_999_999

# 慢：O(n)
val in lst          # ~100ms

# 快：O(1)，先转 set
s = set(lst)        # O(n) 一次性构建
val in s            # ~50ns
```

| 操作 | 时间复杂度 | 说明 |
|---|---|---|
| `lst[i]` | O(1) | 指针偏移，极快 |
| `lst.append(x)` | O(1) 均摊 | 偶尔触发 O(n) 扩容 |
| `lst.pop()` | O(1) | 尾部，无需移动 |
| `lst.insert(0, x)` | **O(n)** | 所有元素右移 |
| `lst.pop(0)` | **O(n)** | 所有元素左移 |
| `lst.remove(x)` | O(n) | 先查找 O(n)，再移动 O(n) |
| `x in lst` | **O(n)** | 线性扫描，无哈希 |
| `lst.sort()` | O(n log n) | Timsort，稳定排序 |
| `lst.reverse()` | O(n) | 原地翻转 |
| `lst[a:b]` | O(k) | k=切片长 |
| `lst.count(x)` | O(n) | 全量扫描 |
| `lst.index(x)` | O(n) | 找到即返回 |

> **Timsort**：Python 的排序算法，结合归并排序与插入排序，对部分有序数据特别高效（接近 O(n)），最坏 O(n log n)，**稳定**（相等元素不改变相对顺序）。

### 常用方法

```python
# 排序与反转
lst.sort(key=None, reverse=False)  # 原地排序（稳定排序）
sorted(lst, key=None, reverse=False)  # 返回新列表，不改变原列表
lst.reverse()                      # 原地反转
lst[::-1]                          # 切片反转，返回新列表
reversed(lst)                      # 返回反向迭代器，不创建新列表（节省内存）

# 增删改查
lst.append(val)       # 末尾添加元素，O(1)
lst.extend(t)         # 批量添加，等价于 lst += t
lst.insert(i, val)    # 在位置i插入元素，O(n)
lst.pop()             # 移除并返回最后一个元素，O(1)
lst.pop(i)            # 移除并返回位置i的元素，O(n)
lst.remove(val)       # 移除第一个值为val的元素，O(n)
lst.clear()           # 清空列表

# 查询
lst.count(val)        # 统计val出现次数
lst.index(val[, start[, end]])  # 查找val的第一个索引，不存在抛出 ValueError，可指定搜索范围
val in lst            # 判断是否存在，O(n)

# 其他
lst.copy()            # 浅拷贝
len(lst)              # 列表长度
sum(lst)              # 求和
min(lst)              # 最小值
max(lst)              # 最大值
```

### 列表推导式

```python
# 基本用法
squares = [x**2 for x in range(10)]

# 带条件
evens = [x for x in range(10) if x % 2 == 0]

# 嵌套（二维展平）
flat = [x for row in matrix for x in row]

# 二维列表初始化（注意浅拷贝问题）
matrix = [[0] * n for _ in range(m)]  # 正确：每行独立
# matrix = [[0] * n] * m              # 错误！所有行引用同一对象

# 带索引遍历（enumerate）
for i, val in enumerate(lst):
    print(i, val)

# 同时遍历两个列表（zip）
for a, b in zip(lst1, lst2):
    print(a, b)
```

### 切片操作

```python
# --- 读取（返回新列表，原列表不变）---
lst[start:end]        # 左闭右开 [start, end)，负索引从尾部数
lst[start:end:step]   # 带步长，step 可为负数
lst[:]                # 全部元素（等价于浅拷贝）
lst[::-1]             # 整体反转
lst[::2]              # 偶数索引元素（0,2,4,...）
lst[1::2]             # 奇数索引元素（1,3,5,...）
lst[:k]               # 前 k 个元素
lst[-k:]              # 后 k 个元素
lst[:-k]              # 去掉最后 k 个元素

# --- 写入（切片赋值，原地修改）---
lst[1:3] = [10, 20]           # 替换区间（长度可以不等！）
lst[1:3] = []                 # 删除区间（等价于 del lst[1:3]）
lst[1:1] = [10, 20]           # 在 index=1 处插入（不删除原元素）
lst[::2] = [0] * len(lst[::2]) # 将所有偶数索引元素置 0

# --- 常见 coding 技巧 ---
a, b = lst[:n], lst[n:]       # 将列表分成两段
lst[l:r+1] = lst[l:r+1][::-1] # 反转子数组 [l, r]（LeetCode 原地反转技巧）

# 示例：旋转数组右移 k 位（LeetCode 189）
def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]   # nums[:] 是原地修改（不新建列表引用）
    # 不能写 nums = nums[-k:] + nums[:-k]，那样只是改了局部变量
```

### 拷贝：浅拷贝 vs 深拷贝

```python
# --- 三种等价的浅拷贝 ---
b = lst.copy()     # 列表方法，语义最清晰
b = lst[:]         # 切片语法，最简洁，常见于 coding
b = list(lst)      # 构造函数，适用于任意可迭代对象

# 浅拷贝只复制"第一层"，嵌套列表仍共享引用
a = [[1, 2], [3, 4]]
b = a.copy()       # b 是新列表，但 b[0] 和 a[0] 指向同一个 [1, 2]
b[0].append(99)
print(a)           # [[1, 2, 99], [3, 4]]  ← a 也变了！
b[1] = [99]
print(a)           # [[1, 2, 99], [3, 4]]  ← a 不变（替换整行不影响 a）

# --- 深拷贝：完全独立 ---
import copy
b = copy.deepcopy(a)  # 递归复制所有层，b 与 a 完全独立

# --- coding 中最常见的坑 ---
path = []
def dfs():
    ans.append(path)        # 错误！path 是引用，后续修改会影响 ans 中的结果
    ans.append(path[:])     # 正确：每次记录当前状态的副本
    ans.append(list(path))  # 等价写法
```

> **何时用深拷贝？** 只有嵌套结构（列表的列表、列表的字典等）且需要完全独立时才用 `deepcopy`，代价较高（O(n) 且常数大）。大多数算法题用 `path[:]` 即可。

### 算法常用技巧

```python
# --- 初始化 ---
lst = [0] * n                          # 全 0 列表
lst = [float('inf')] * n               # 全无穷（初始化 dp/距离数组）
lst = list(range(n))                   # [0, 1, 2, ..., n-1]
matrix = [[0]*cols for _ in range(rows)]  # 二维数组（每行独立！）

# --- 解包 ---
a, b, c = [1, 2, 3]                   # 直接解包
first, *rest = lst                     # 头部 + 剩余
*init, last = lst                      # 剩余 + 尾部
a, *mid, b = lst                       # 首尾 + 中间
merged = [*lst1, *lst2]                # 合并列表（等价于 lst1 + lst2）
a, b = b, a                            # 交换两变量（Python 特有，无需 tmp）

# --- 输入处理（ACM 模式）---
n = int(input())
lst = list(map(int, input().split()))  # 读一行整数
matrix = [list(map(int, input().split())) for _ in range(n)]  # 读矩阵

# --- 矩阵操作 ---
# 转置矩阵（行列互换）
transposed = list(map(list, zip(*matrix)))
# 顺时针旋转 90°
rotated = list(map(list, zip(*matrix[::-1])))
# 逆时针旋转 90°
rotated = list(map(list, zip(*matrix)))[::-1]

# --- 排序技巧 ---
lst.sort(key=lambda x: x[1])                    # 按第二元素升序
lst.sort(key=lambda x: (-x[1], x[0]))           # 按第二元素降序，再按第一升序
lst.sort(key=lambda x: (len(x), x))             # 按长度，再按字典序
words.sort(key=lambda w: [ord(c)-ord('a') for c in w])  # 自定义字母顺序

import functools
lst.sort(key=functools.cmp_to_key(lambda a, b: a - b))  # 自定义比较函数

# --- 常用聚合 ---
total = sum(lst)
total = sum(x**2 for x in lst)         # 生成器表达式，不创建中间列表
max_val = max(lst)
max_val = max(lst, key=lambda x: x[1]) # 按第二元素找最大
max_val = max(lst, default=0)          # 空列表时返回 default（Python 3.4+）
flat_sum = sum(sum(row) for row in matrix)  # 矩阵求和

# --- 去重与统计 ---
unique = list(set(lst))                # 去重（不保序）
unique_sorted = sorted(set(lst))       # 去重并排序
freq = {}
for x in lst: freq[x] = freq.get(x, 0) + 1   # 手动计数

# --- 双指针/滑动窗口常用 ---
left, right = 0, len(lst) - 1         # 对撞指针初始化
while left < right:
    # ... 双指针逻辑 ...
    left += 1; right -= 1

# --- 前缀和（一维）---
n = len(lst)
prefix = [0] * (n + 1)
for i, x in enumerate(lst):
    prefix[i+1] = prefix[i] + x
# 区间和 [l, r]（闭区间）
range_sum = prefix[r+1] - prefix[l]

# --- 差分数组 ---
diff = [0] * (n + 1)
# 区间 [l, r] 加 val：
diff[l] += val; diff[r+1] -= val
# 还原：
from itertools import accumulate
result = list(accumulate(diff))[:n]
```

---

## 字典 dict

### 底层实现

CPython 3.6+ 的 dict 是**紧凑哈希表（compact hash table）**，由两部分组成：
- **索引数组**（稀疏）：存储哈希槽，记录"键值对在 entries 数组中的位置"
- **entries 数组**（紧凑）：按插入顺序存储 `(hash, key, value)` 三元组

这使得 dict 在 Python 3.7+ **保证插入顺序**，且内存比旧版紧凑约 20-25%。

**哈希流程**：
```
1. 计算 hash(key) → 整数
2. hash & (capacity-1) → 初始槽位 i（capacity 总是 2 的幂）
3. 若槽位空 → 插入；若 hash 和 key 均相等 → 更新；否则 → 探测下一槽
4. 探测方式：i = (5*i + 1 + perturb) % capacity  （伪随机探测，非线性探测）
```

**负载因子**：默认 2/3，超过后触发扩容（容量翻倍），重新哈希所有键。

**哈希冲突**：最坏情况（所有键哈希相同）退化为 O(n)，实际中极少发生。

```python
# 为什么 key in dict 是 O(1)？
# 1. hash(key) 计算出槽位，直接跳转 → 不需要遍历
# 2. 只有极少数冲突需要探测 1-2 次
d = {i: i for i in range(10_000_000)}
999999 in d   # ~50ns，和 n=10 时几乎一样快
```

| 操作 | 时间复杂度 | 说明 |
|---|---|---|
| `d[key]` / `d.get(key)` | O(1) 均摊 | 哈希查找 |
| `d[key] = val` | O(1) 均摊 | 哈希插入/更新 |
| `del d[key]` | O(1) 均摊 | 哈希删除 |
| `key in d` | **O(1) 均摊** | 哈希查找 |
| `d.keys()` / `.values()` / `.items()` | O(1) | 返回视图，不复制 |
| 遍历 `for k in d` | O(n) | 遍历 entries 数组 |
| `d.update(other)` | O(m) m=other大小 | 逐个插入 |
| 构建 `dict(pairs)` | O(n) | 逐个哈希插入 |

> **为什么自定义类的对象默认可哈希？** Python 对象默认用 `id()`（内存地址）作为哈希值，所以任意对象都可以作为 dict 的 key。但如果定义了 `__eq__`，必须同时定义 `__hash__`（否则变为不可哈希）。

### 常用方法

```python
# 访问与修改
d[key]                         # 访问键值，不存在抛出 KeyError
d.get(key, default=None)       # 安全访问，不存在返回default
d.setdefault(key, default)     # 如key不存在则设置默认值并返回
d.update(other)                # 批量更新（可传字典或键值对）

# 删除
d.pop(key[, default])          # 删除并返回指定键值，不存在时返回default
d.popitem()                    # 删除并返回最后一个键值对（Python 3.7+ LIFO顺序）
del d[key]                     # 删除指定键，不存在抛出 KeyError
d.clear()                      # 清空字典

# 视图对象（动态，随字典变化而更新）
d.keys()                       # 返回键的视图
d.values()                     # 返回值的视图
d.items()                      # 返回键值对的视图

# 构造技巧
dict.fromkeys(iterable, value=None)  # 用可迭代对象创建字典
{k: v for k, v in pairs}            # 字典推导式
```

### 迭代技巧

```python
# 遍历键值对
for k, v in d.items():
    print(k, v)

# 按键排序遍历
for k in sorted(d):
    print(k, d[k])

# 按值排序遍历（升序）
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)

# 按值排序遍历（降序）
for k, v in sorted(d.items(), key=lambda x: -x[1]):
    print(k, v)

# 字典合并（Python 3.9+）
merged = d1 | d2               # 返回新字典
d1 |= d2                       # 原地合并

# 判断键是否存在
key in d                       # O(1)
key not in d                   # O(1)
```

---

## 集合 set

### 底层实现

set 和 dict 共用同一套哈希表机制，区别是 set **只存 key，不存 value**。

- 底层：稀疏哈希表，槽位只存 `(hash, key)`
- 负载因子：2/3，超过后扩容
- **`val in set`**：计算 hash(val) → 直接定位槽位 → O(1)

```python
# list vs set 的 in 性能对比（10M 元素）
import time
data = list(range(10_000_000))
s = set(data)
target = 9_999_999

# list: O(n)，约 100ms
t0 = time.time(); _ = target in data; print(time.time()-t0)

# set: O(1)，约 50ns
t0 = time.time(); _ = target in s;    print(time.time()-t0)
```

| 操作 | 时间复杂度 | 说明 |
|---|---|---|
| `s.add(x)` | O(1) 均摊 | 哈希插入 |
| `x in s` | **O(1) 均摊** | 哈希查找 |
| `s.remove(x)` / `s.discard(x)` | O(1) 均摊 | 哈希删除 |
| `s1 \| s2` 并集 | O(n+m) | 遍历两个集合 |
| `s1 & s2` 交集 | O(min(n,m)) | 遍历较小集合，在较大集合中查找 |
| `s1 - s2` 差集 | O(n) | 遍历 s1 |
| `s1 ^ s2` 对称差 | O(n+m) | — |
| `set(lst)` 构建 | O(n) | 逐个插入 |

> **为什么 set 的交集是 O(min(n,m)) 而非 O(n+m)？** CPython 会自动选择遍历较小的集合，对每个元素在较大集合中做 O(1) 哈希查找。

### 常用方法

```python
# 创建
s = {1, 2, 3}
s = set([1, 2, 3])             # 从可迭代对象创建（可去重）
s = set()                      # 注意：{} 是空字典而非空集合

# 增删
s.add(val)                     # 添加元素，已存在则无效
s.update(*others)              # 迭代添加多个元素/集合
s.remove(val)                  # 删除元素，不存在则抛出 KeyError
s.discard(val)                 # 删除元素，不存在则不报错（推荐）
s.pop()                        # 随机移除并返回一个元素
s.clear()                      # 清空集合

# 集合运算
s1 | s2                        # 并集（union）
s1 & s2                        # 交集（intersection）
s1 - s2                        # 差集（difference），属于s1但不属于s2
s1 ^ s2                        # 对称差集（symmetric_difference），只属于一个集合的元素
s1.union(s2)                   # 并集（等价于 |）
s1.intersection(s2)            # 交集（等价于 &）
s1.difference(s2)              # 差集（等价于 -）

# 关系判断
val in s                       # O(1) 查询
s1.issubset(s2)                # s1是否是s2的子集（s1 <= s2）
s1.issuperset(s2)              # s1是否是s2的超集（s1 >= s2）
s1.isdisjoint(s2)              # 两集合是否无交集
```

### 去重与快速查找

```python
# 列表去重（不保序，最简洁）
unique = list(set(lst))

# 列表去重（保持原顺序）
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]

# 利用集合快速查找：O(n)构建，O(1)查询
lookup = set(lst)
if target in lookup:
    print("found")

# 两数之和经典用法
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
```

---

## collections 模块

> Python内置的数据结构扩展库，提供高效的专用数据结构。

| 数据结构        | 核心作用                                           | 典型场景                              |
| --------------- | -------------------------------------------------- | ------------------------------------- |
| `Counter`     | 计数器：快速统计可迭代对象中元素出现次数           | 词频统计、热点Key计数、字母异位词     |
| `defaultdict` | 字典扩展：访问不存在的Key自动初始化默认值          | 计数统计、分组聚合、嵌套字典          |
| `OrderedDict` | 有序字典：保证字典插入顺序（Python 3.7+ 普通dict也有序，但此类提供额外API） | LRU缓存、需要移动键到首尾的场景 |
| `deque`       | 双端队列：两端增删 O(1)，优于列表首尾操作 O(n)     | 队列/栈、滑动窗口、BFS                |
| `namedtuple`  | 命名元组：给元组元素命名，兼具不可变性和可读性     | 轻量数据对象（坐标、用户信息）        |
| `ChainMap`    | 链式映射：合并多个字典，查询时按顺序遍历（无需拷贝）| 多配置合并、环境变量优先级覆盖        |

### Counter 计数器

> Counter 继承自 dict，底层就是哈希表。构建 `Counter(iterable)` 是 O(n)，`most_common(k)` 是 O(n log k)（内部用堆）。

```python
from collections import Counter

# 创建
cnt = Counter([1, 1, 2, 3, 3, 3])   # Counter({3: 3, 1: 2, 2: 1})
cnt = Counter('abracadabra')         # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
cnt = Counter({'a': 3, 'b': 1})      # 直接从字典创建

# 常用操作
cnt[key]                             # 访问计数，不存在返回0（不是KeyError）
cnt.most_common(n)                   # 返回出现次数最多的n个元素（列表，降序）
cnt.most_common()                    # 不指定n则返回所有（按频率降序）
cnt.elements()                       # 返回所有元素的迭代器（按计数重复）
cnt.total()                          # 所有计数总和（Python 3.10+）
cnt.subtract(iterable)               # 减少计数（计数可变为负数）
cnt.update(iterable)                 # 增加计数

# 遍历操作（继承自 dict）
cnt.keys()                           # 返回所有元素的视图（去重后的键）
cnt.values()                         # 返回所有计数的视图
cnt.items()                          # 返回 (元素, 计数) 键值对视图
for elem, count in cnt.items():      # 遍历每个元素及其计数
    print(f"{elem}: {count}")

# 算术运算
c1 + c2                             # 计数相加（只保留正数）
c1 - c2                             # 计数相减（只保留正数）
c1 & c2                             # 取每个键的最小计数
c1 | c2                             # 取每个键的最大计数

# 示例：统计字母频率
s = "abracadabra"
cnt = Counter(s)
print(cnt.most_common(3))            # [('a', 5), ('b', 2), ('r', 2)]

# 示例：判断字母异位词（LeetCode 438）
def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

### defaultdict 默认字典

> defaultdict 继承自 dict，复杂度与 dict 完全相同（O(1) 增删查）。唯一区别是重写了 `__missing__`：访问不存在的 key 时自动调用工厂函数创建默认值。

```python
from collections import defaultdict

# 创建（传入无参可调用对象作为工厂函数）
dd = defaultdict(list)               # 默认值为空列表 []
dd = defaultdict(int)                # 默认值为 0
dd = defaultdict(set)                # 默认值为空集合 set()
dd = defaultdict(lambda: -1)         # 默认值为 -1

# 核心特性：访问不存在的键时，自动创建默认值（不抛 KeyError）
dd['new_key'].append(1)              # 自动创建空列表并追加
dd['count'] += 1                     # 自动创建0并加1

# 注意区别
dd[key]        # 若key不存在，触发默认值，key被插入字典
dd.get(key)    # 若key不存在，返回None，key不被插入（不触发默认值）

# 示例：分组
pairs = [('a', 1), ('b', 2), ('a', 3)]
groups = defaultdict(list)
for key, val in pairs:
    groups[key].append(val)
# groups: {'a': [1, 3], 'b': [2]}

# 示例：计数（等价于Counter）
freq = defaultdict(int)
for c in "abracadabra":
    freq[c] += 1
```

### OrderedDict 有序字典

```python
from collections import OrderedDict

# 创建
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# 独有操作（普通dict没有）
od.move_to_end('a')           # 将键'a'移动到末尾
od.move_to_end('c', last=False)  # 将键'c'移动到开头
od.popitem(last=True)         # 弹出最后一个键值对（LIFO）
od.popitem(last=False)        # 弹出第一个键值对（FIFO）

# 示例：LRU缓存（最近最少使用）
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # 访问后移至末尾（最近使用）
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # 淘汰最久未使用的（头部）
```

### deque 双端队列

#### 底层实现

deque 不是单个数组，而是**双向链表连接的固定大小块（block）数组**：
- 每个 block 存储 64 个元素（CPython 实现）
- 维护 leftblock/rightblock 指针和 leftindex/rightindex 偏移
- 两端 append/pop：直接移动指针 → **严格 O(1)**（不是均摊）
- 中间 `insert(i, x)` / 随机访问 `dq[i]`：需遍历 block 链 → **O(n)**

```
# list 与 deque 头部操作对比（10万次 appendleft）
# list.insert(0, x)：每次把所有元素右移 → O(n²) 总
# deque.appendleft(x)：只移动指针 → O(n) 总

list: ~500ms（100万次 insert(0,x)）
deque: ~10ms  （100万次 appendleft(x)）
```

| 操作 | 时间复杂度 | vs list |
|---|---|---|
| `dq.append(x)` | **O(1)** | list O(1) 均摊 |
| `dq.appendleft(x)` | **O(1)** | list **O(n)** |
| `dq.pop()` | **O(1)** | list O(1) |
| `dq.popleft()` | **O(1)** | list **O(n)** |
| `dq[i]` 随机访问 | O(n) | list O(1) |
| `x in dq` | O(n) | list O(n) |
| `dq.rotate(k)` | O(k) | — |

> **选 list 还是 deque？**
> 只在尾部操作 → list（随机访问更快）
> 需要头部操作（BFS队列、滑动窗口）→ deque

```python
from collections import deque

# 创建
dq = deque()
dq = deque([1, 2, 3])
dq = deque(maxlen=3)          # 设置最大长度，满了追加时自动弹出对侧元素

# 操作
dq.append(x)                  # 右侧添加，O(1)
dq.appendleft(x)              # 左侧添加，O(1)
dq.pop()                      # 右侧弹出，O(1)
dq.popleft()                  # 左侧弹出，O(1)
dq.extend(iterable)           # 右侧批量添加
dq.extendleft(iterable)       # 左侧批量添加（注意顺序会反转）
dq.rotate(n)                  # 正数：右旋（尾部移到头部），负数：左旋
dq.clear()                    # 清空
dq.insert(i, x)               # 在位置i插入元素，O(n)（不常用，需要时用list）
dq.count(val)                 # 统计val出现次数
dq.remove(val)                # 删除第一个值为val的元素
dq.reverse()                  # 原地反转
len(dq)                       # 长度
dq[0]                         # 查看头部（不弹出）
dq[-1]                        # 查看尾部（不弹出）

# 可用作栈（右进右出）和队列（右进左出）

# 示例：BFS层序遍历
from collections import deque
q = deque([root])
while q:
    node = q.popleft()
    if node.left:  q.append(node.left)
    if node.right: q.append(node.right)

# 示例：滑动窗口最大值（单调递减队列）
def maxSlidingWindow(nums, k):
    dq = deque()   # 存索引，保持单调递减
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:    # 队头超出窗口范围
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

### namedtuple 命名元组

```python
from collections import namedtuple

# 创建命名元组类型
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age score')  # 也可以用空格分隔的字符串

# 使用
p = Point(3, 4)
print(p.x, p.y)              # 3 4（可用属性名访问）
print(p[0], p[1])            # 3 4（也可以用索引访问）
print(p)                     # Point(x=3, y=4)

# 不可变（元组特性）
# p.x = 5  # 报错 AttributeError

# 实用方法
p._asdict()                  # 转为 OrderedDict，如 {'x': 3, 'y': 4}
p._replace(x=10)             # 返回新元组，将x替换为10
Point._fields                # 返回字段名元组 ('x', 'y')

# 示例：表示坐标
directions = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
for d in directions:
    new_x, new_y = cur.x + d.x, cur.y + d.y
```

### ChainMap 链式映射

```python
from collections import ChainMap

# 创建（多个字典按顺序查找，无需合并拷贝）
defaults = {'color': 'red', 'size': 'M'}
overrides = {'color': 'blue', 'weight': 1.5}
combined = ChainMap(overrides, defaults)

# 查找：按顺序查找，找到第一个匹配即返回
print(combined['color'])     # 'blue'（overrides中找到）
print(combined['size'])      # 'M'（overrides中没有，从defaults找到）

# 修改只影响第一个字典
combined['new_key'] = 'val'  # 写入overrides
del combined['new_key']      # 只能删除第一个字典中的键

# 新增一层（常用于作用域模拟）
child = combined.new_child({'color': 'green'})

# 示例：命令行参数 > 环境变量 > 默认配置 的优先级
import os
cli_args = {'debug': True}
env_vars = {'host': 'localhost'}
defaults  = {'host': '0.0.0.0', 'port': 8080, 'debug': False}
config = ChainMap(cli_args, env_vars, defaults)
print(config['debug'])       # True（CLI优先）
print(config['host'])        # 'localhost'（env优先）
print(config['port'])        # 8080（从defaults取）
```

---

## bisect 二分查找模块

> 只能用于**已排序的数组**，所有操作时间复杂度 O(log n)。

### 底层实现

纯二分搜索，无额外数据结构：
- `bisect_left/right`：O(log n) 查找，O(1) 额外空间
- `insort_left/right`：O(log n) 查找 + **O(n) 插入**（list 中间插入需移动元素）

```
# insort 的完整复杂度
bisect（查找位置）: O(log n)
list.insert（插入）: O(n)   ← 瓶颈！
总计：O(n)

若需要频繁有序插入，考虑用 SortedList（sortedcontainers 库）→ O(log n)
```

| 操作 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| `bisect_left/right` | O(log n) | O(1) |
| `insort_left/right` | O(n)（插入移位） | O(1) |

```python
import bisect

a = [1, 2, 4, 4, 5, 8]

# 查找插入位置（不实际插入）
bisect.bisect_left(a, 4)     # => 2，若存在相等元素，插入到左侧（第一个4的位置）
bisect.bisect_right(a, 4)    # => 4，若存在相等元素，插入到右侧（最后一个4的后面）
bisect.bisect(a, 4)          # => 4，等价于 bisect_right

# 实际插入（保持有序）
bisect.insort_left(a, 3)     # 将3插入，保持升序，相等元素插入到左侧
bisect.insort_right(a, 3)    # 将3插入，保持升序，相等元素插入到右侧
bisect.insort(a, 3)          # 等价于 insort_right

# 参数 lo, hi：限制搜索范围
bisect.bisect_left(a, x, lo=0, hi=len(a))  # 只在 a[lo:hi] 范围内搜索
```

### 核心用法：左右边界查找

```python
a = [1, 2, 4, 4, 4, 5, 8]

# 查找第一个 >= x 的位置（左边界）
def lower_bound(a, x):
    return bisect.bisect_left(a, x)   # 等价于 C++ lower_bound

# 查找第一个 > x 的位置（右边界）
def upper_bound(a, x):
    return bisect.bisect_right(a, x)  # 等价于 C++ upper_bound

# 查找最后一个 <= x 的位置
def find_last_le(a, x):
    idx = bisect.bisect_right(a, x) - 1
    return idx if idx >= 0 else -1

# 判断x是否在数组中
def contains(a, x):
    idx = bisect.bisect_left(a, x)
    return idx < len(a) and a[idx] == x

# 示例：统计有序数组中x出现的次数
def count_occurrences(a, x):
    return bisect.bisect_right(a, x) - bisect.bisect_left(a, x)

a = [1, 2, 4, 4, 4, 5, 8]
print(count_occurrences(a, 4))   # 3
```

### 算法应用（LeetCode 2070 最大美丽值）

```python
# 排序后用bisect代替手写二分，代码更简洁
import bisect

def maximumBeauty(items, queries):
    items.sort()
    prices = [p for p, _ in items]
    max_beauty = []
    cur_max = 0
    for _, b in items:
        cur_max = max(cur_max, b)
        max_beauty.append(cur_max)

    result = []
    for q in queries:
        idx = bisect.bisect_right(prices, q) - 1
        result.append(max_beauty[idx] if idx >= 0 else 0)
    return result
```

---

## heapq 堆模块

> 堆是完全二叉树，用数组存储。Python的heapq实现的是**小顶堆**（最小值在堆顶）。

### 底层实现

堆用**数组（list）存储完全二叉树**，节点 i 的父子关系：
```
父节点：(i - 1) // 2
左子节点：2 * i + 1
右子节点：2 * i + 2
```

**核心操作**：
- **上浮（sift up）**：插入元素到末尾，反复与父节点比较，若比父小则交换 → `heappush` O(log n)
- **下沉（sift down）**：弹出堆顶，将末尾元素移到堆顶，反复与较小子节点交换 → `heappop` O(log n)

**`heapify` 为什么是 O(n) 而非 O(n log n)？**
```
从最后一个非叶节点（n//2 - 1）开始向前逐个做 sift down：
- 底层节点高度为 0，工作量少；高层节点少，工作量多
- 数学证明：∑ (n/2^k) * k = O(n)，不是 O(n log n)
```

| 操作 | 时间复杂度 | 说明 |
|---|---|---|
| `heappush(h, x)` | O(log n) | sift up |
| `heappop(h)` | O(log n) | sift down |
| `h[0]` 查看堆顶 | **O(1)** | 不修改堆 |
| `heapify(lst)` | **O(n)** | 非 O(n log n)！ |
| `heappushpop(h, x)` | O(log n) | 比分开调用快（少一次 sift） |
| `heapreplace(h, x)` | O(log n) | 同上 |
| `nsmallest(k, lst)` | O(n log k) | 维护大小为 k 的堆 |
| `nlargest(k, lst)` | O(n log k) | 维护大小为 k 的堆 |

> **nsmallest vs sorted**：k 很小时用 nsmallest（O(n log k)）；k 接近 n 时用 sorted（O(n log n)，但常数更小）。CPython 内部也是这样判断的。

| 类型     | 核心规则                   | 堆顶   |
| -------- | -------------------------- | ------ |
| 小顶堆   | 父节点值 ≤ 所有子节点值   | 最小值 |
| 大顶堆   | 父节点值 ≥ 所有子节点值   | 最大值 |

### 基础操作

```python
import heapq

# 创建堆（两种方式）
heap = []
heapq.heappush(heap, x)              # 插入元素并维持堆结构，O(log n)
min_val = heapq.heappop(heap)        # 弹出最小值，O(log n)
min_val = heap[0]                    # 查看堆顶（不弹出），O(1)

# 原地堆化（O(n)，比逐个push高效）
arr = [5, 4, 3, 2, 1]
heapq.heapify(arr)                   # 将列表原地转为小顶堆

# 进阶操作
heapq.heappushpop(heap, x)           # 先插入x，再弹出最小值（原子操作，高效）
heapq.heapreplace(heap, x)           # 先弹出最小值，再插入x（要求堆非空）
# 区别：heappushpop 保证弹出的是"插入x后的最小值"，heapreplace 保证堆顶先被弹出

# Top K问题
heapq.nsmallest(k, iterable)         # 返回最小的k个元素（已排序列表）
heapq.nlargest(k, iterable)          # 返回最大的k个元素（已排序列表）
heapq.nsmallest(k, iterable, key=lambda x: x[1])  # 支持自定义key

# 合并多个有序堆/迭代器（返回迭代器，惰性求值）
heapq.merge(*iterables, key=None, reverse=False)   # 合并多个已排序序列
list(heapq.merge([1,3,5], [2,4,6]))  # [1, 2, 3, 4, 5, 6]
```

### 大顶堆（插入负值）

```python
# Python没有原生大顶堆，通过插入负值模拟
max_heap = []
heapq.heappush(max_heap, -x)         # 插入时取负
max_val = -heapq.heappop(max_heap)   # 弹出后取负

# 示例：维护前k大的数
k = 3
heap = []
for x in [3, 1, 4, 1, 5, 9, 2, 6]:
    heapq.heappush(heap, -x)

top_k = [-heapq.heappop(heap) for _ in range(k)]
print(top_k)   # [9, 6, 5]
```

### 元组堆（多键排序）

```python
# heapq支持元组，按元组元素依次比较
import heapq

heap = []
heapq.heappush(heap, (priority, task_id, task))  # 先按priority排序

# 示例：Dijkstra最短路
h = [(0, start)]   # (距离, 节点)
while h:
    dist, node = heapq.heappop(h)
    for neighbor, weight in graph[node]:
        if dist + weight < dis[neighbor]:
            dis[neighbor] = dist + weight
            heapq.heappush(h, (dis[neighbor], neighbor))
```

### 堆排序

```python
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print(heap_sort([7, 2, 5, 1, 8, 3]))  # [1, 2, 3, 5, 7, 8]
```

---

## itertools 模块

### accumulate 前缀和/前缀积

```python
from itertools import accumulate
import operator

nums = [1, 2, 3, 4, 5]

# 默认：前缀和
list(accumulate(nums))               # [1, 3, 6, 10, 15]

# 指定运算：前缀积
list(accumulate(nums, operator.mul)) # [1, 2, 6, 24, 120]

# 指定初始值（Python 3.8+）
list(accumulate(nums, initial=0))    # [0, 1, 3, 6, 10, 15]（长度多1）

# 前缀最大值
list(accumulate(nums, max))          # [1, 2, 3, 4, 5]
list(accumulate([3,1,4,1,5,9], max)) # [3, 3, 4, 4, 5, 9]

# 应用：差分数组还原（差分求前缀和得原数组）
diff = [2, 1, -1, 3, -2]
original = list(accumulate(diff))    # [2, 3, 2, 5, 3]

# 应用：统计差分数组中被覆盖的点
diff = [0] * (max_end + 2)
for start, end in intervals:
    diff[start] += 1
    diff[end + 1] -= 1
covered_count = sum(s > 0 for s in accumulate(diff))
```

### chain 链式迭代

```python
from itertools import chain

# 连接多个可迭代对象（不创建新列表，惰性求值）
list1 = [1, 2, 3]
tuple1 = ('a', 'b')
str1 = "XY"
result = list(chain(list1, tuple1, str1))
# [1, 2, 3, 'a', 'b', 'X', 'Y']

# 展平嵌套列表（chain.from_iterable）
nested = [[1, 2], [3, 4, 5], [6]]
flat = list(chain.from_iterable(nested))
# [1, 2, 3, 4, 5, 6]

# 算法应用：提取多个栈的所有元素
stacks = [[1, 2], [3], [4, 5, 6]]
all_indices = sorted(chain.from_iterable(stacks))
```

### 其他常用 itertools

```python
from itertools import product, permutations, combinations, combinations_with_replacement

# 笛卡尔积（多层嵌套循环的替代）
list(product([1,2], [3,4]))          # [(1,3),(1,4),(2,3),(2,4)]
list(product('AB', repeat=2))        # [('A','A'),('A','B'),('B','A'),('B','B')]

# 全排列（n个元素取r个的全排列）
list(permutations([1,2,3], 2))       # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 组合（不重复，不考虑顺序）
list(combinations([1,2,3,4], 2))     # [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

# 可重复组合
list(combinations_with_replacement([1,2,3], 2))  # [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
```

---

## functools 模块 —— lru_cache 记忆化

> `lru_cache`（Least Recently Used Cache）是 Python 提供的**记忆化**（Memoization）装饰器，用于缓存函数的返回值。

### 核心作用

| 作用 | 说明 |
|------|------|
| **避免重复计算** | 相同参数的调用直接从缓存获取结果，不再执行函数体 |
| **优化递归** | 递归问题（如斐波那契、动态规划）中大量子问题被重复计算，记忆化将指数级复杂度降为多项式级 |
| **提升性能** | 频繁调用的纯函数可大幅减少执行时间 |
| **控制内存** | 通过 `maxsize` 限制缓存大小，防止内存无限增长 |

### 基本用法

```python
from functools import lru_cache

@lru_cache(maxsize=128)      # 最多缓存128个不同参数的结果
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 性能对比
# 无缓存：O(2^n)，fib(35) 需要数秒
# 有缓存：O(n)，fib(1000) 瞬间完成

# 查看缓存统计
print(fibonacci.cache_info())   # CacheInfo(hits=998, misses=1000, maxsize=128, currsize=128)
fibonacci.cache_clear()         # 清空缓存
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `maxsize` | 最大缓存条目数，设为 `None` 表示无限制。默认128。 |
| `typed` | 设为 `True` 时，`3` 和 `3.0` 被视为不同参数。默认 `False`。 |

### 算法应用

典型应用场景：递归 DFS、动态规划、字符串拆分等问题。

```python
# 示例：记忆化 DFS
@lru_cache(maxsize=None)
def dfs(state):
    if 终止条件:
        return 结果
    # ... 递归调用 dfs(子状态)
```

> 相关题目：[LeetCode 139. 单词拆分](https://leetcode.cn/problems/word-break/)

### 注意事项

```python
# ❌ 错误：参数必须可哈希
@lru_cache
def foo(lst: list): ...       # list 不可哈希，会报错

# ✅ 正确：使用可哈希类型
@lru_cache
def foo(tup: tuple): ...      # tuple 可哈希
```

- **仅适用于纯函数**：相同输入永远产生相同输出，无副作用
- **参数必须可哈希**：`list`、`dict` 等不可哈希类型需转为 `tuple`、`frozenset`
- **内存权衡**：`maxsize=None` 可能占用大量内存，谨慎使用

---

## 常用数学函数

### math 模块

```python
import math

# 无穷大（推荐写法）
inf = math.inf                  # 正无穷
neg_inf = -math.inf             # 负无穷
inf = float('inf')              # 不需要导入math
neg_inf = float('-inf')

# 常用函数
math.floor(x)                   # 向下取整
math.ceil(x)                    # 向上取整
math.sqrt(x)                    # 平方根（返回float）
math.isqrt(x)                   # 整数平方根（向下取整，返回int）
math.gcd(a, b)                  # 最大公约数（Python 3.5+）
math.lcm(a, b)                  # 最小公倍数（Python 3.9+）
math.log(x)                     # 自然对数
math.log2(x)                    # 以2为底的对数
math.log10(x)                   # 以10为底的对数
math.pow(x, y)                  # x的y次方（返回float）
math.factorial(n)               # n的阶乘
math.comb(n, k)                 # 组合数 C(n,k)（Python 3.8+）
math.perm(n, k)                 # 排列数 P(n,k)（Python 3.8+）

# 常用内置函数（无需导入）
abs(x)                          # 绝对值
pow(x, y)                       # x的y次方（整数运算不丢精度）
pow(x, y, mod)                  # 快速幂取模，等价于 x**y % mod
divmod(a, b)                    # 返回 (a//b, a%b) 元组
round(x, n)                     # 四舍五入，n为小数位数
```

### 无穷大的算法应用

```python
# 初始化最大值/最小值的技巧
min_val = float('inf')    # 比较时任何实数都比它小
max_val = float('-inf')   # 比较时任何实数都比它大

# 验证BST（用±inf传递边界）
def isValidBST(root, left=-math.inf, right=math.inf):
    if root is None:
        return True
    x = root.val
    return left < x < right and \
           isValidBST(root.left, left, x) and \
           isValidBST(root.right, x, right)

# Dijkstra初始化
dis = [float('inf')] * n
dis[start] = 0
```

---

## 列表 vs 数组 vs 链表

| 特性     | Python列表           | array.array | 链表               |
| -------- | -------------------- | ----------- | ------------------ |
| 存储方式 | 动态数组（连续内存） | 连续内存    | 非连续内存         |
| 随机访问 | O(1)                 | O(1)        | O(n)               |
| 头部插入 | O(n)                 | O(n)        | O(1)               |
| 尾部插入 | O(1)均摊             | O(1)均摊    | O(1)（已知尾节点） |
| 内存开销 | 较小                 | 最小        | 较大（需存储指针） |
| 元素类型 | 任意                 | 固定        | 任意               |

```python
import array

# array模块用于大规模数值计算，元素类型固定，内存比list省
arr = array.array('i', [1, 2, 3])  # 'i'表示有符号整数
arr = array.array('d', [1.0, 2.5]) # 'd'表示双精度浮点数

# 常用类型码
# 'b': 有符号字节    'B': 无符号字节
# 'i': 有符号整数    'I': 无符号整数
# 'f': 单精度浮点    'd': 双精度浮点
```

---

## 内置函数速查

```python
# 排序相关
sorted(iterable, key=None, reverse=False)   # 返回新列表
lst.sort(key=None, reverse=False)            # 原地排序

# 排序key技巧
lst.sort(key=lambda x: x[1])               # 按第二个元素排序
lst.sort(key=lambda x: (x[1], x[0]))       # 多键排序
lst.sort(key=lambda x: -x)                  # 降序（不用reverse=True）
import functools
lst.sort(key=functools.cmp_to_key(compare)) # 自定义比较函数

# 常用内置函数
enumerate(iterable, start=0)   # 返回(索引, 元素)对
zip(*iterables)                # 并行迭代多个序列
map(func, iterable)            # 对每个元素应用函数
filter(func, iterable)         # 过滤满足条件的元素
any(iterable)                  # 任一为真则返回True
all(iterable)                  # 全部为真则返回True
sum(iterable, start=0)         # 求和（start为初始值）
min(iterable, key=None)        # 最小值
max(iterable, key=None)        # 最大值

# 示例
nums = [3, 1, 4, 1, 5]
print(list(enumerate(nums, 1)))  # [(1,3),(2,1),(3,4),(4,1),(5,5)]
print(list(zip([1,2,3], 'abc'))) # [(1,'a'),(2,'b'),(3,'c')]
print(list(map(str, nums)))      # ['3','1','4','1','5']
print(list(filter(lambda x: x>2, nums)))  # [3, 4, 5]
print(any(x > 4 for x in nums))  # True
print(all(x > 0 for x in nums))  # True
```
