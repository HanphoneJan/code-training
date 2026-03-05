[分享｜如何科学刷题？ - 讨论 - 力扣（LeetCode）](https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/)
[LeetCode 热题 100 - 学习计划 - 力扣（LeetCode）全球极客挚爱的技术成长平台](https://leetcode.cn/studyplan/top-100-liked/)
[(35 封私信 / 80 条消息) 数据结构与算法入门宝典：超全知识汇总（包括深度学习手撕） - 知乎](https://zhuanlan.zhihu.com/p/1903577161132115759)
[OI Wiki - OI Wiki](https://oi-wiki.org/)
[通过动画可视化数据结构和算法- VisuAlgo](https://visualgo.net/zh)

[LeetCode 热题 100 - 学习计划 - 力扣（LeetCode）全球极客挚爱的技术成长平台](https://leetcode.cn/studyplan/top-100-liked/)

https://pythontutor.com/python-compiler.html#mode=edit

![灵神刷题路线图.webp](https://hanphone.top/gh/HanphoneJan/public_pictures/learn/%E7%81%B5%E7%A5%9E%E5%88%B7%E9%A2%98%E8%B7%AF%E7%BA%BF%E5%9B%BE.webp)


## Python常用数据结构与方法
注意，python中使用数组需要import array，元素类型固定。Python列表的底层数据结构是一个**动态数组**。 动态数组的特点是可以根据需要动态扩展或缩小其大小。 在Python中，列表的底层实现使用了C语言的结构体和指针，以便高效地处理列表的操作。 动态数组通过分配一块连续的内存空间来存储元素。 当列表中的元素数量超过当前分配的内存空间时，动态数组会自动分配更大的内存空间，并将原始元素复制到新的内存空间中。

```python
# str
format(*args, **kwargs)  # 用法丰富多样, 算法中可用于字符串形式的进制转换(练习: LeetCode [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/))
split(sep=None, maxsplit=-1)  # 以sep来分割字符串
strip([chars])  # 去除首末两端的字符, 默认是 \r,\n," "
join(iterable)  # 将iterable内的元素拼接成字符串,如','.join(['leet', 'code']) #="leet,code"
replace(old, new[, count])  # 字符串替换, old to new
count(sub[, start[, end]])  # 统计子字符串sub的个数
startswith(prefix[, start[, end]])  # 以prefix开始的字符串
endswith(suffix[, start[, end]])  # 以suffix结束的字符串

#list
lst.sort(*, key=None, reverse=False)
lst.append(val)  # 也可以 lst = lst + [val]
lst.clear()  # 清空列表
lst.count(val)  # val个数
lst.extend(t)  # or s += t  # += 其实调用的是 __iadd__ 方法
lst.pop(val=lst[-1])  # (默认)从末端移除一个值
lst.remove(val)  # 移除 val
lst.reverse()  # 反转
lst.insert(i, val)  # 在 i 处插入 val

from collections import deque
queue = deque([iterable[, maxlen]])
queue.append(val)  # 往右边添加一个元素
queue.appendleft(val)  # 往左边添加一个元素
queue.clear()  # 清空队列
queue.count(val)  # 返回指定元素的出现次数
queue.extend(iterable)  # 从队列右边扩展一个序列的元素
queue.extendleft(iterable)  #  从队列左边扩展一个列表的元素
queue.insert(val[, start[, stop]])  # 在指定位置插入元素
queue.pop()  # 获取最右边一个元素，并在队列中删除
queue.popleft()  # 获取最左边一个元素，并在队列中删除
queue.reverse()  # 队列反转
queue.remove(val)  # 删除指定元素
queue.rotate(n=1)  # 把右边元素放到左边

import bisect # 只能用于已经排序的数组
bisect.bisect_left(a, x, lo=0, hi=len(a))  # 返回将x插入a后的位置index(如果a中存在与x等值的元素，则插入到左侧), 默认从 0到-1
bisect.bisect_right(a, x, lo=0, hi=len(a))  # 返回将x插入a后的位置index(如果a中存在与x等值的元素，则插入到右侧)
bisect.bisect(a, x, lo=0, hi=len(a))  # 与 bisect_right 相同
bisect.insort_left(a, x, lo=0, hi=len(a))  # 将x插入a(如果a中存在与x等值的元素，则插入到左侧)
bisect.insort_right(a, x, lo=0, hi=len(a))  # 将x插入a(如果a中存在与x等值的元素，则插入到右侧)
bisect.insort(a, x, lo=0, hi=len(a))  # 与insort_left 相同, 将变量x插入到a中,并保持a升序

# dict
from collections import defaultdict
pop(key[, default])  # 通过键去删除键值对(若没有该键则返回default(没有设置default则报错))
setdefault(key[, default])  # 设置默认值
update([other])  # 批量添加
get(key[, default])  # 通过键获取值(若没有该键可设置默认值, 预防报错)
clear()  # 清空字典
keys()  # 将字典的键组成新的可迭代对象
values()  # 将字典中的值组成新的可迭代对象
items()  # 将字典的键值对凑成一个个元组, 组成新的可迭代对象

# counnter
from collections import Counter
cnt = Counter([iterable-or-mapping])
cnt.elements()  # 所有元素
cnt.most_common([n])  # 指定一个参数n，列出前n个元素，不指定参数，则列出所有
cnt.subtract([iterable-or-mapping])  # 原来的元素减去新传入的元素
cnt.update([iterable-or-mapping])  # 增加元素

from collections import OrderedDict #使得插入的顺序有序

# set
add(elem)  # 向集合中添加数据
update(*others)  # 迭代着增加
clear()  # 清空集合
discard(elem)  # 删除集合中指定的值(不存在则不删除)

#heap 可实现优先级队列的数据结构. 可以解决 top n 问题
import heapq
heap = []  # 建堆
heapq.heappush(heap,item)  # 往堆中插入新值
item = heapq.heappop(heap)  # 弹出最小的值
item = heap[0]  # 查看堆中最小的值, 不弹出
heapq.heapify(x)  # 以线性时间将一个列表转为堆
item = heapq.heapreplace(heap,item)  # 弹出一个最小的值, 然后将 item 插入到堆当中. 堆的整体的结构不会发生改变.
heapq.heappoppush(heap, item)  # 弹出最小的值.并且将新的值插入其中.
heapq.merge(*iterables, key=None, reverse=False)  # 将多个堆进行合并
heapq.nlargest(n, iterable, key=None)  # 从堆中找出最大的 n 个数，key的作用和sorted( )方法里面的key类似, 用列表元素的某个属性和函数作为关键字
heapq.nsmallest(n, iterable, key=None)  # 从堆中找出最小的 n 个数, 与 nlargest 相反
```
#### collections
是 Python 内置的数据结构扩展库，它在原生的 list、dict、set、tuple 基础上，提供了一批更高效、更贴合业务场景的专用数据结构

| 数据结构          | 核心作用                                           | 典型场景                  |
| ------------- | ---------------------------------------------- | --------------------- |
| `defaultdict` | 字典扩展：访问不存在的 Key 自动初始化默认值（如 `int`/`list`/`set`） | 计数统计、分组聚合、嵌套字典        |
| `Counter`     | 计数器：快速统计可迭代对象中元素的出现次数（返回类字典结构）                 | 词频统计、热点 Key 计数、数据去重统计 |
| `OrderedDict` | 有序字典：保证字典插入顺序                                  | 需固定键值顺序的场景（如配置解析）     |
| `deque`       | 双端队列：高效实现两端增删操作（O (1)），优于列表的首尾操作（O (n)）        | 队列 / 栈、滑动窗口、高频增删场景    |
| `namedtuple`  | 命名元组：给元组元素命名，兼具元组不可变和类的可读性                     | 轻量数据对象（如坐标、用户信息）      |
| `ChainMap`    | 链式映射：合并多个字典，查询时按顺序遍历（无需拷贝）                     | 多配置合并、环境变量优先级覆盖       |
```python
import math
inf = math.inf # 需要导入
inf = float('inf') # 无需导入
# 负无穷大
neg_inf = float('-inf')
```
## 滑动窗口
滑动窗口相当于在维护一个**队列**。右指针的移动可以视作**入队**，左指针的移动可以视作**出队**。
### 定长
#### 模板
```python
//第一种写法
class Solution:
    def template(self, arr: list[int], k: int) -> list[int]:
        # 处理边界情况（空数组/窗口大小非法）
        if not arr or k <= 0 or k > len(arr):
            return []
        
        # 计算第一个窗口（前k个元素）
        for i in range(k):
            # 此处编写第一个窗口的业务逻辑
            pass
        
        # 滑动窗口（从第k个元素开始）
        for i in range(k, len(arr)):
            left = i - k  # 左窗口边界（离开窗口的元素索引）
            right = i     # 右窗口边界（进入窗口的元素索引）
            # 此处编写滑动窗口的业务逻辑
            pass
        
        return []
//第二种写法
class Solution:
    def template(self, arr: list[int], k: int) -> list[int]:
        # 处理边界情况
        if not arr or k <= 0 or k > len(arr):
            return []
        
        for i in range(len(arr)):
            # 1. 右窗口指针i指向当前进入窗口的元素
            # 此处可编写元素进入窗口的逻辑
            
            # 2. 窗口元素不足k个时，继续循环不处理业务逻辑
            if i < k - 1:
                continue
            
            # 3. 窗口元素达到k个，执行核心业务逻辑
            # 此时窗口范围：[i - k + 1, i]
            # 此处编写业务逻辑
            
            # 4. 剔除左侧离开窗口的元素（左窗口指针：i - k + 1）
            # 此处编写元素离开窗口的逻辑
        
        return []
```

#### 例题—定长子串中元音的最大数目
[1456. 定长子串中元音的最大数目 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)

| 算法  | 时间复杂度         | 空间复杂度 | 核心优化点                |
| --- | ------------- | ----- | -------------------- |
| 算法一 | O(n)          | O(1)  | 集合查询（O (1)）+ 单循环滑动窗口 |
| 算法二 | O(n×m)（≈O(n)） | O(n)  | 滑动窗口但用列表查元音 + 临时数组   |
| 算法三 | O(n×k×m)      | O(1)  | 无优化，暴力枚举所有窗口         |
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # 用集合直观表达元音
        max_count = current_count = left = 0
        
        for right, char in enumerate(s):
            # 先加入当前右指针字符（如果是元音则计数+1）
            if char in vowels:
                current_count += 1
            
            # 当窗口大小超过k时，移动左指针并调整计数
            if right - left + 1 > k:
                if s[left] in vowels:
                    current_count -= 1
                left += 1
            
            # 更新最大计数（保证窗口大小合法时才更新）
            if right - left + 1 == k:
                max_count = max(max_count, current_count)
        
        return max_count
```
### 不定长
**用两个指针维护一个动态的窗口区间，根据条件收缩或扩展窗口**
不定长滑动窗口主要分为三类：求最长子数组，求最短子数组，求子数组个数。
#### 模板
```python
def sliding_window(s):
    # 1. 初始化窗口状态（哈希表/集合/计数器）、双指针、结果
    window = {}  # 记录窗口内元素的状态（如计数）
    left = right = 0  # 左右指针，初始都在0
    res = 0  # 存储最终结果（长度/数量等）

    # 2. 右指针扩展窗口，遍历整个字符串/数组
    while right < len(s):
        c = s[right]  # 当前右指针指向的元素
        right += 1  # 右指针右移，扩大窗口
        # 3. 更新窗口内的状态（如计数、集合）
        window[c] = window.get(c, 0) + 1

        # 4. 根据条件收缩左指针（核心：不同题目条件不同）
        while 窗口需要收缩的条件:  # 如：重复字符数超过k/窗口包含所有目标字符
            d = s[left]  # 当前左指针指向的元素
            left += 1  # 左指针右移，缩小窗口
            # 5. 更新窗口内的状态
            window[d] -= 1
            if window[d] == 0:
                del window[d]

        # 6. 更新结果（注意：更新位置可能在收缩前/后，依题目而定）
        res = max(res, right - left)  # 例如：记录最大窗口长度
    return res
```


## 二分算法
两个难度：一是想不到用二分来解，二是check函数不会写
### 二分查找
对于不重复的升序数组：`left`指向了数组中第一个大于`target`的元素的索引，`left`的值等于数组中小于`target`的元素个数
#### 闭区间写法
循环结束时，left = right + 1
```python
# 闭区间写法
left, right = 0, n-1
while left<=right:
	mid = int(left+(right-left)/2)
	if(nums[mid]==target):
		return mid
	elif(nums[mid]>target):
		right = mid -1
	else:
		left = mid +1
```
#### 开区间写法
循环结束的唯一条件是 `left == right`
```python
# 左闭右开
left, right = 0, n  # 左闭右开区间[0, n)
while left < right:  # 区间非空时继续（left < right）
	mid = left + (right - left) // 2  # 避免溢出
	if nums[mid] == target:
		return mid  # 找到目标，返回索引
	elif nums[mid] > target:
		right = mid  # 目标在左区间[left, mid)
	else:
		left = mid + 1  # 目标在右区间[mid+1, right)
return -1  # 未找到目标
```
`right` 始终表示 “搜索范围的下一个不包含的位置”

### 例题—每一个查询的最大美丽值 
[2070. 每一个查询的最大美丽值 - 力扣（LeetCode）--题解](https://leetcode.cn/problems/most-beautiful-item-for-each-query/solutions/1100468/jiang-xun-wen-chi-xian-pai-xu-by-endless-o5j0/)
给你一个二维整数数组 `items` ，其中 `items[i] = [pricei, beautyi]` 分别表示每一个物品的 **价格** 和 **美丽值** 。
同时给你一个下标从 **0** 开始的整数数组 `queries` 。对于每个查询 `queries[j]` ，你想求出价格小于等于 `queries[j]` 的物品中，**最大的美丽值** 是多少。如果不存在符合条件的物品，那么查询的结果为 `0` 。
请你返回一个长度与 `queries` 相同的数组 `answer`，其中 `answer[j]`是第 `j` 个查询的答案。
1. 对items 按price升序排序
2. 建立items排序之后的前缀max数组，以美丽度建立。 prefix[i] 包含i，表示前i个的最大美丽度
3. 遍历query数组，每一个query，对items适用二分。二分<=query的上界得到索引idx。prefix\[idx]即当前索引所求解
```python
def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
	# 步骤1：按价格升序排序物品
	items.sort()
	n = len(items)
	if n == 0:
		return [0] * len(queries)
	
	# 步骤2：分离价格和预处理前缀最大美丽值
	prices = []
	max_beauty = []
	current_max = 0
	for price, beauty in items:
		prices.append(price)
		current_max = max(current_max, beauty)
		max_beauty.append(current_max)
	
	# 步骤3：对每个查询二分查找并获取结果
	result = []
	for q in queries:
		# 找到第一个大于q的价格的索引，减一就是最后一个<=q的价格的索引
		idx = bisect.bisect_right(prices, q) - 1
		if idx >= 0:
			result.append(max_beauty[idx])
		else:
			result.append(0)
	return result
```

#### enumerate
**内置函数！将可迭代对象（如列表、元组、字符串等）组合为一个索引序列，用于将数组拆分为索引+值。**
```python
nums = [10, 20, 30, 40]

# 方法1：字典推导式 + enumerate
dict1 = {index: value for index, value in enumerate(nums)}
print("字典推导式结果：", dict1)  # 输出：{0: 10, 1: 20, 2: 30, 3: 40}

# 方法2：直接用dict()转换enumerate对象
dict2 = dict(enumerate(nums))
print("dict构造函数结果：", dict2)  # 输出：{0: 10, 1: 20, 2: 30, 3: 40}
```
#### in/ not in
用于判断一个元素是否**存在于**一个**可迭代对象（或容器）中**，返回布尔值。列表、元组、字符串、集合、哈希表、字典都支持！

## 数据结构
常用枚举技巧、前缀和、栈、队列、堆。**多数数据结构最难的操作是删除！**
数组：连续内存存储，随机访问 O (1)，插入 / 删除末尾元素 O (1)，中间操作 O (n)。
### 枚举
一般是遍历+维护哈希表
#### 哈希表
哈希表（Hash Table，也叫散列表）是一种**通过哈希函数将键（Key）映射到值（Value）的高效数据结构**，核心目标是实现**O (1) 时间复杂度的增删改查**（理想情况下），也是缓存、数据库等系统的底层核心（如 Redis 的键值存储、Java 的 HashMap 均基于哈希表实现）。
哈希表主要由 3 部分构成，缺一不可：

| 组成部分                | 作用                                             |
| ------------------- | ---------------------------------------------- |
| 哈希函数（Hash Function） | 将任意长度的 Key 映射为固定范围的整数（哈希值 / 索引），是哈希表的 “核心转换器”。 |
| 哈希表数组               | 存储数据的底层数组，哈希值直接作为数组下标，定位数据存储位置。                |
| 冲突解决机制              | 解决 “不同 Key 映射到同一哈希值” 的问题（哈希冲突）。                |
哈希函数有：
整数 Key：直接取模 hash(key) = key % 数组长度（最简单，如 Key=100，数组长度 = 16 → 哈希值 = 4）；
字符串 Key：经典的 “BKDRHash”
由于哈希函数的输出范围是有限的（数组长度固定），而 Key 的范围是无限的，**不同 Key 映射到同一哈希值是必然的**

|解决机制|原理|优点|缺点|典型应用|
|---|---|---|---|---|
|链地址法（拉链法）|数组每个下标位置对应一个链表 / 红黑树，冲突的 Key 依次存入链表 / 树中。|实现简单、扩容成本低|链表过长会导致查询退化到 O (n)|Redis、Java HashMap（JDK8+ 链表≥8 转红黑树）|
|开放定址法|冲突时，按固定规则（线性探测、二次探测）寻找下一个空的数组位置。|无需额外存储结构|易出现 “聚集效应”（连续位置被占）|早期数据库、内存缓存|
|再哈希法|冲突时，用另一个哈希函数重新计算哈希值，直到找到空位置。|避免聚集|多次哈希计算，效率略低|分布式哈希表（DHT）|

**python中的字典底层就是哈希表，而使用defaultdict模块会为不存在的键自动创建一个「默认值」，不用手动判断 / 初始化，** int默认初始化为0，列表等为空。
`defaultdict` 要求传入「无参可调用对象」作为工厂函数，`lambda: -1` 是最简的无参函数，调用后返回 `-1`；
```python
from collections import defaultdict
d = defaultdict(lambda: -1)
d[key] 触发默认值，d.get(key) 不会触发（仍返回 None）
```
#### Counter
**继承字典，用于统计可迭代对象的每个元素的个数**
```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
cnt = Counter(nums)
print(cnt)  # 输出：Counter({3: 3, 2: 2, 1: 1})
s = "abracadabra"
cnt_str = Counter(s)
print(dict(cnt_str))  # 输出：{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```
[438. 找到字符串中所有字母异位词 - 力扣（LeetCode）](https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/2969498/liang-chong-fang-fa-ding-chang-hua-chuan-14pd/?envType=study-plan-v2&envId=top-100-liked)
#### 前缀和
**任意子数组都是一个前缀去掉前缀后的结果**，**因此子数组的和就是两个前缀和的差**
prefix_sums\[0] = 0
nums\[i] = prefix_sum\[i]-prefix_sums\[i-1]

```python
class NumArray:
    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]
```
##### 二维前缀和
[304. 二维区域和检索 - 矩阵不可变 - 力扣（LeetCode）](https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/2667331/tu-jie-yi-zhang-tu-miao-dong-er-wei-qian-84qp/)
前缀和数组 s 是 m+1 行 n+1 列（第 0 行、第 0 列全为 0，作为边界）；
s\[i]\[j] 的定义：表示原始矩阵中「从左上角 (0,0) 到右下角 (i-1,j-1)」的子矩阵所有元素的和。
`当前区域和 = 左边区域和 + 上边区域和 - 重叠区域和 + 当前元素`。
`目标区域和 = 最大区域和 - 左边区域和 - 上边区域和 + 重叠区域和`。
```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2,c2) 的子矩阵元素和
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2+1][c2+1] - self.s[r2+1][c1] - self.s[r1][c2+1] + self.s[r1][c1]
```
#### accumulate
```python
from itertools import accumulate
nums = [1, 2, 3, 4, 5]
# 生成前缀和迭代器（无初始值，长度和原列表一致）
prefix_sums = accumulate(nums)
# 转成列表查看结果（迭代器需转列表/循环才能获取元素）
print(list(prefix_sums))  # 输出：[1, 3, 6, 10, 15]
```
#### 距离和
[2602. 使数组元素全部相等的最少操作次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/description/)
#### 二维数组
```python
arr = [[0 for _ in range(cols)] for _ in range(rows)]
arr = np.zeros((3, 4))
```

### 差分
差分与前缀和的关系，类似导数与积分的关系。数组 a 的差分的前缀和就是数组 a（不变）。
diff\[i] = nums\[i] - nums\[i-1]
**从左到右累加 diff 中的元素，可以得到数组 nums。**
**把 a 的子数组 a\[i],a\[i+1],…,\[j] 都加上 x 等价于 把 d\[i] 增加 x，把 d\[j+1] 减少 x。**


#### 例题—与车相交的点
[2848. 与车相交的点 - 力扣（LeetCode）](https://leetcode.cn/problems/points-that-intersect-with-cars/description/)
给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。对于任意下标 i，nums\[i] = \[starti, endi] ，其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。
返回数轴上被车 任意部分 覆盖的整数点的数目。
```python
# 方法一：暴力
def numberOfPoints(self, nums: List[List[int]]) -> int:
	result = [0]*101
	for start,end in nums:
		result[start:end+1] = [1] *(end-start+1)
	return result.count(1)

#方法二：差分
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 步骤1：找到所有区间的最大结束值，确定差分数组的长度
        max_end = max(end for _, end in nums)
        # 步骤2：初始化差分数组（长度+2是为了避免end+1越。界）
        diff = [0] * (max_end + 2)  
        # 步骤3：遍历所有区间，更新差分数组
        for start, end in nums:
            diff[start] += 1    # 区间起点：计数+1（表示开始覆盖）
            diff[end + 1] -= 1  # 区间终点的下一位：计数-1（表示结束覆盖）
        # 步骤4：计算前缀和 + 统计被覆盖的点的数量
        return sum(s > 0 for s in accumulate(diff))
```
[2132. 用邮票贴满网格图 - 力扣（LeetCode）](https://leetcode.cn/problems/stamping-the-grid/solutions/1199642/wu-nao-zuo-fa-er-wei-qian-zhui-he-er-wei-zwiu/)

### 栈stack
后进先出（LIFO），可用数组或链表实现。有以下五个核心操作：
- **push()**：向栈顶添加元素。
- **pop()**：从栈顶移除元素并返回其值。
- **peek()/top()**：返回栈顶元素但不删除。
- **isEmpty()**：判断栈是否为空。
- **size()**：返回栈中元素个数。
使用python的列表就能很好实现
#### chain
```python
from itertools import chain

# --- 场景一：连接多个独立的可迭代对象 ---
print("--- 场景一：连接多个独立对象 ---")
list1 = [1, 2, 3]
tuple1 = ('a', 'b')
str1 = "XY"  # 字符串也是可迭代对象

# 使用 chain(*iterables) 直接将它们作为参数传入
# 这适用于你事先知道要连接哪些对象的情况
combined_iter = chain(list1, tuple1, str1)

# 将迭代器转换为列表以便查看完整结果
combined_list = list(combined_iter)
print(f"使用 chain(list1, tuple1, str1) 的结果: {combined_list}")
# 输出: 使用 chain(list1, tuple1, str1) 的结果: [1, 2, 3, 'a', 'b', 'X', 'Y']

# --- 场景二：连接一个容器内的所有可迭代对象 ---
print("--- 场景二：连接容器内的所有对象 ---")
list_of_lists = [[10, 20], [30, 40, 50], [60]]
# 使用 chain.from_iterable(iterable) 将一个“容器”传入
# 这适用于你有一个列表（或其他可迭代对象），其内部元素本身也是可迭代对象的情况
flattened_iter_from_lists = chain.from_iterable(list_of_lists)
# 将迭代器转换为列表
flattened_list = list(flattened_iter_from_lists)
print(f"使用 chain.from_iterable(list_of_lists) 的结果: {flattened_list}")
# 输出: 使用 chain.from_iterable(list_of_lists) 的结果: [10, 20, 30, 40, 50, 60]
```

[3170. 删除星号以后字典序最小的字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/solutions/2798240/yong-26-ge-zhan-mo-ni-pythonjavacgo-by-e-mhtn/)
```python
class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            # 找第一个非空栈，即为最小字母
            for st in stacks:
                if st:
                    st.pop()
                    break
        return ''.join(s[i] for i in sorted(chain.from_iterable(stacks)))
```

#### 例题—基本计算器
[224. 基本计算器 - 力扣（LeetCode）](https://leetcode.cn/problems/basic-calculator/description/)
```python
def calculate(self, s: str) -> int:
	ops = [1]                          # 维护括号层级的符号栈，初始默认正号
	sign = 1                           # 当前数字的运算符号
	
	ret = 0                            # 最终计算结果
	n = len(s)                         # 表达式字符串长度
	i = 0                              # 遍历字符串的指针
	while i < n:
	    if s[i] == ' ':                # 跳过空格
	        i += 1
	    elif s[i] == '+':              # 遇到加号，当前符号继承栈顶层级符号
	        sign = ops[-1]
	        i += 1
	    elif s[i] == '-':              # 遇到减号，当前符号为栈顶层级符号取反
	        sign = -ops[-1]
	        i += 1
	    elif s[i] == '(':              # 遇到左括号，将当前符号入栈（记录该层级符号）
	        ops.append(sign)
	        i += 1
	    elif s[i] == ')':              # 遇到右括号，弹出当前层级符号（括号结束）
	        ops.pop()
	        i += 1
	    else:                          # 遇到数字，解析完整数字并累加至结果
	        num = 0
	        while i < n and s[i].isdigit(): # 解析连续数字字符为整数
	            num = num * 10 + ord(s[i]) - ord('0')
	            i += 1
	        ret += num * sign          # 按当前符号累加数字到结果
	return ret                         # 返回最终计算结果
```
##### eval()
将字符串作为数学表达式计算
```python
s = "123"
num = int(s)
num =123
s = str(num)
```
#### 单调栈
**及时去掉无用数据，保证栈中数据有序。**

### 队列queue
核心操作有四个：
- **入队（Enqueue）**：向队列尾部添加元素。
- **出队（Dequeue）**：从队列头部移除元素。
- **查看队头元素（Peek）**：获取队列头部元素但不删除。
- **判断空 / 满**：检查队列是否为空或已满。
手动实现的话推荐使用链表。一般的单向队列用栈实现需要两个标准的栈，一个负责入队，一个负责出队，然后在出队栈为空时把入队栈元素倒进出队栈。在python可以用列表的pop(0)来实现出队。循环队列就是比一般队列多两个指针。
front（队首指针）：指向队列中第一个有效元素的位置（即下一次 pop 要取出的元素位置）；
rear（队尾指针）：指向队列中最后一个有效元素的下一个位置（即下一次 push 要插入元素的位置。
一般用在广度优先搜索（BFS）：用于遍历图或树，层序遍历，需用队列存储待访问的相邻节点。
### 循环队列的实现
```python
class MyCircularQueue:
    def __init__(self, k: int):
        # 初始化固定长度的数组存储队列元素，初始值为None（表示空位置）
        self.queue = [None] * k      
        # 记录队列的最大容量（即数组长度）
        self.max_size = k
        # 记录当前队列中实际元素的个数（核心：避免front/rear判断空/满的边界问题）
        self.size = 0        
        # 队首指针：始终指向队列中第一个有效元素的索引
        self.front = 0                
        # 队尾指针：始终指向队列中最后一个有效元素的下一个位置（即下一个可插入的位置）
        self.rear = 0                 

    def enQueue(self, value: int) -> bool:
        """入队操作：将元素添加到队尾，成功返回True，队列满返回False"""
        # 先判断队列是否已满，满则无法入队
        if self.isFull():
            return False
        # 将新元素赋值到队尾指针指向的空位置
        self.queue[self.rear] = value
        # 队尾指针循环后移（取模处理：到达数组末尾则回到0）
        self.rear = (self.rear + 1) % self.max_size 
        # 实际元素个数+1
        self.size += 1
        # 入队成功
        return True

    def deQueue(self) -> bool:
        """出队操作：移除队首元素，成功返回True，队列为空返回False"""
        # 先判断队列是否为空，空则无法出队
        if self.isEmpty():
            return False
        # 将队首指针指向的元素置为None（清空，避免残留值，可选操作）
        self.queue[self.front] = None
        # 队首指针循环后移（取模处理：到达数组末尾则回到0）
        self.front = (self.front + 1) % self.max_size
        # 实际元素个数-1
        self.size -= 1
        # 出队成功
        return True

    def Front(self) -> int:
        """获取队首元素：队列为空返回-1，否则返回队首元素值"""
        # 空队列返回-1（符合常规题目要求）
        if self.isEmpty():
            return -1
        # 直接返回队首指针指向的元素
        return self.queue[self.front]

    def Rear(self) -> int:
        """获取队尾元素：队列为空返回-1，否则返回队尾元素值"""
        # 空队列返回-1（符合常规题目要求）
        if self.isEmpty():
            return -1
        # 队尾指针指向"下一个插入位置"，因此前一位才是最后一个有效元素
        # 取模处理边界：当rear=0时，队尾索引为max_size-1（数组最后一位）
        last_index = (self.rear - 1) % self.max_size
        # 返回队尾元素值
        return self.queue[last_index]

    def isEmpty(self) -> bool:
        """判断队列是否为空：实际元素个数为0则为空"""
        return self.size == 0

    def isFull(self) -> bool:
        """判断队列是否已满：实际元素个数等于最大容量则为满"""
        return self.size == self.max_size
```

#### deque双向队列模块
```python
from collections import deque

q = deque(maxlen=3)  # 最大长度3，满了追加会自动弹出左侧元素
q.append(1)         # 右侧追加（普通队列入队）
q.appendleft(2)     # 左侧追加
q.pop()             # 右侧弹出
q.popleft()         # 左侧弹出（普通队列出队）
q.clear()           # 清空
q.extend([3,4])     # 右侧批量追加，将一个列表中的每个元素单独zhui。列表也有extend方法
q.rotate(1)         # 向右旋转（尾部元素移到头部）
```
双向队列模块可以用作栈和单向队列！

### 堆heap
就是**完全二叉树，用数组（顺序表）存储**。核心特点是快速访问最值元素（时间复杂度 $O(1)$）、插入 / 删除最值的效率高$(O(\log n)$），核心操作是「上浮（Sift Up）」和「下沉（Sift Down）」，所有操作（插入、删除最值）均基于这两个基础动作。
堆分为「大顶堆」和「小顶堆」，核心是**父节点与子节点的数值关系**：

| 类型            | 核心规则            | 最值位置    |
| ------------- | --------------- | ------- |
| 大顶堆（Max-Heap） | 任意父节点值 ≥ 所有子节点值 | 根节点是最大值 |
| 小顶堆（Min-Heap） | 任意父节点值 ≤ 所有子节点值 | 根节点是最小值 |
#### heapq
对于已有数组，可以原地堆化。
```python
import heapq

# 1. 基础方法：heappush / heappop / heapify
heap = []
[heapq.heappush(heap, x) for x in [3,1,2,5,4]]  # 逐个插入元素，维持小顶堆结构
print(heap)  # [1, 3, 2, 5, 4]
min_val = heapq.heappop(heap)                    # 弹出堆顶最小值
print(min_val)  # 1
print(heap)  # [2, 3, 4, 5]

# heapify：将无序列表原地转为小顶堆（时间复杂度O(n)）
arr1, arr2 = [5,4,3,2,1], [9,7,8,5,6,4,10]
heapq.heapify(arr1); heapq.heapify(arr2); 
print(arr1)  # [1, 2, 3, 5, 4]
print(arr2)  # [4, 5, 8, 7, 6, 9, 10]

# 2. 进阶方法：heappushpop / heapreplace
heap = [2,3,4,5]
# heappushpop：先插入元素，再弹出堆顶（比分开调用更高效）
val1 = heapq.heappushpop(heap, 6)
val2 = heapq.heappushpop(heap, 1)
print(val1, val2, heap)  # 2 1 [3, 5, 4, 6]

heap = [3,5,4,6]
# heapreplace：先弹出堆顶，再插入元素（与heappushpop顺序相反）
val3 = heapq.heapreplace(heap, 1)
print(val3, heap)  # 3 [1, 5, 4, 6]

# 3. Top K问题：nlargest / nsmallest
# nsmallest：返回前k个最小元素（已排序）；nlargest：返回前k个最大元素（已排序）
nums = [10,2,8,5,1,7,9,3]
print(heapq.nsmallest(3, nums))  # [1, 2, 3]
print(heapq.nlargest(3, nums))  # [10, 9, 8]

students = [("Alice",95),("Bob",80),("Charlie",90),("David",85)]
# 带自定义key：按元组第二个元素（分数）排序取前2高
print(heapq.nlargest(2, students, key=lambda x:x[1]))  # [('Alice', 95), ('Charlie', 90)]

# 4. heapify实现堆排序
def heap_sort(arr):
    heapq.heapify(arr)  # 先转为小顶堆
    return [heapq.heappop(arr) for _ in range(len(arr))]  # 逐次弹堆顶实现升序
print(heap_sort([7,2,5,1,8,3]))  # [1, 2, 3, 5, 7, 8]
```
heapq 无原生大顶堆，可通过「插入负值」实现，插入时存负值，弹出时取绝对值。
#### 例题—从数量最多的堆取走礼物 
[2558. 从数量最多的堆取走礼物 - 力扣（LeetCode）](https://leetcode.cn/problems/take-gifts-from-the-richest-pile/solutions/2501655/yuan-di-dui-hua-o1-kong-jian-fu-ti-dan-p-fzdh/)
```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapify(gifts)
        while k and -gifts[0] > 1:
            heapreplace(gifts,-isqrt(-gifts[0]))
            k -= 1
        return -sum(gifts)
```

### 并查集
**为了解决问题：判断两个元素是否属于同一集合、某个元素在哪个集合、合并两个集合**，因此提出了并查集这个抽象数据类型，一般用树结构实现，用一个根节点代表一个集合。操作均摊时间复杂度接近 O (1)，适合大规模动态合并 / 查询场景。
**查找操作：任给一个结点，只需找到根节点即可确定所在集合。**
路径压缩算法：在查找时，将x到根节点路径上的所有点的pre（上级）都设为根节点，树扁平化，提高查找效率
**合并操作：合并两棵树，简单！**
[【算法与数据结构】—— 并查集-CSDN博客](https://blog.csdn.net/the_zed/article/details/105126583)
#### 模板
```python
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己，大小为 1
        self._fa = list(range(n))  # 代表元
        self._size = [1] * n  # 集合大小
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        fa = self._fa
        # 如果 fa[x] == x，则表示 x 是代表元
        if fa[x] != x:
            fa[x] = self.find(fa[x])  # fa 改成代表元
        return fa[x]

    # 判断 x 和 y 是否在同一个集合
    def is_same(self, x: int, y: int) -> bool:
        # 如果 x 的代表元和 y 的代表元相同，那么 x 和 y 就在同一个集合
        # 这就是代表元的作用：用来快速判断两个元素是否在同一个集合
        return self.find(x) == self.find(y)

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self._size[y] += self._size[x]  # 更新集合大小（注意集合大小保存在代表元上）
        # 无需更新 _size[x]，因为我们不用 _size[x] 而是用 _size[find(x)] 获取集合大小，但 find(x) == y，我们不会再访问 _size[x]
        self.cc -= 1  # 成功合并，连通块个数减一
        return True

    # 返回 x 所在集合的大小
    def get_size(self, x: int) -> int:
        return self._size[self.find(x)]  # 集合大小保存在代表元上
```
## 链表、树、回溯
二叉树 DFS	
理解递归，为动态规划做铺垫
### 链表
**在 Python 中，对链表的所有操作本质都是对「引用（指针）」的操作，而 “物理存在的节点” 本身只能通过引用间接修改 。**  只有`ListNode()`构造函数的调用才会创建新节点，调用多少次创建多少物理节点，一般用node.next = ListNode() 添加新节点。
对于链表的遍历，在什么情况下，循环条件要写 while node？什么情况下要写 while node.next 或 while node.next.next

| 循环条件                                                       | 能访问到的节点       | 核心目标       | 核心适用场景                                     | 安全前提                                  |
| ---------------------------------------------------------- | ------------- | ---------- | ------------------------------------------ | ------------------------------------- |
| `while node`，终止位置`n为ode` 为 `None` 时                        | 所有节点（含最后一个节点） | 处理每个节点本身   | 遍历打印 / 累加节点值、统计节点数、查找目标值、链表深拷贝             | 无需额外校验（空链表直接退出）                       |
| `while node.next`，终止位置为最后一个节点时（`node.next=None`）           | 仅到倒数第二个节点     | 处理节点的后继    | 找尾节点、尾部插入节点、删除最后一个节点、基础版找中间节点              | 需先校验 `if not node`（防空链表）              |
| `while node.next.next`终止位置为倒数第二个节点时（`node.next.next=None`） | 仅到倒数第三个节点     | 处理节点的后继的后继 | 快慢指针判环 / 找中点、删除倒数第二个节点、找倒数第三个节点、批量操作两个后继节点 | 需先校验 `node and node.next`（防空 / 单节点链表） |
#### 如何区分链表数组？
**本质上是内存是否连续分配的问题，以及是否需要指针拼接。** 链表相对数组的主要优势就是**内存的动态利用**，所以尽量不要用数组辅助去做链表题，不然链表就没有意义。
#### 例题—找出临界点之间的最小和最大距离
[2058. 找出临界点之间的最小和最大距离 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
```python
def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
	minDistance = maxDistance  = -1
	first = last = -1
	pos = 0
	cur = head
	while cur.next.next:
		x,y,z = cur.val,cur.next.val,cur.next.next.val
		if y>max(x,z) or y<min(x,z):
			if last!= -1:
				minDistance = (pos-last if minDistance == -1 else min(minDistance,pos-last))
				maxDistance = max(maxDistance,pos-first)
			if first == -1:
				first = pos
			last = pos
		cur = cur.next
		pos += 1
	return [minDistance,maxDistance]
```

#### 反转链表
哨兵节点的作用：让处理逻辑更简单
[92. 反转链表 II - 力扣（LeetCode）](https://leetcode.cn/problems/reverse-linked-list-ii/solutions/1992226/you-xie-cuo-liao-yi-ge-shi-pin-jiang-tou-teqq/)
```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	# 反转整个链表
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		cur = head
		pre = None
		while cur:
			tmp = cur.next
			cur.next = pre
			pre = cur
			cur = tmp
		return pre
	# 只反转链表的中间部分	
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. 构建虚拟头节点dummy，p0初始指向dummy（最终p0会停在left的前一个节点）
        # 虚拟头节点的作用：统一处理left=1（反转从表头开始）的边界情况，无需单独判断
        p0 = dummy = ListNode(next=head)
        
        # 2. 移动p0到「left的前一个节点」（循环left-1次）
        # 例如left=2时，p0从dummy移动1次，指向原链表第1个节点（索引0）
        for _ in range(left - 1):
            p0 = p0.next

        # 3. 初始化反转用的指针：pre（反转后的前驱）、cur（当前待反转节点）
        pre = None  # 初始无前驱，反转后第一个节点的next要指向None
        cur = p0.next  # cur初始指向left节点（反转区间的起点）
        
        # 4. 逐次反转[left, right]区间内的节点（共right-left+1个节点）
        for _ in range(right - left + 1):
            nxt = cur.next  # 先保存当前节点的下一个节点（防止链表断裂）
            cur.next = pre   # 核心：反转当前节点的指向（指向前驱pre）
            pre = cur        # pre后移：成为下一个节点的前驱
            cur = nxt       # cur后移：处理下一个节点（最终cur会停在right的下一个节点）

        # 5. 连接反转后的链表：修复区间两端的指针
        p0.next.next = cur # 原left节点（现在是反转区间的尾节点）指向right的下一个节点（cur）
        p0.next = pre   # left的前一个节点（p0）指向反转区间的新头节点（pre，原right节点）
        return dummy.next # 6. 返回新链表的头节点（虚拟头节点的next，兼容left=1的情况）
```

#### 链表相加
```python
def addTwo(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
	if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
		return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
	if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
		l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
	carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
	l1.val = carry % 10  # 每个节点保存一个数位
	l1.next = self.addTwo(l1.next, l2.next if l2 else None, carry // 10)  # 进位
	return l1
```
#### 双指针
用两个指针遍历链表，两个指针可以有先后、快慢等关系，可以实现查询链表倒数第n个节点等等，或者使用两个指针分别指示两个链表达到对原**链表分离**的目的（仍旧是O（1）的空间复杂度）。
##### 归并排序
```python
def sortList(self, head: ListNode) -> ListNode:
	"""主函数：对链表进行归并排序"""
	# 终止条件：链表为空 或 只有一个节点（已经有序）
	if self._is_linked_list_empty_or_single_node(head):
		return head
	
	# 步骤1：拆分链表为左右两部分
	left_head, right_head = self._split_linked_list(head)
	
	# 步骤2：递归排序左半和右半链表
	sorted_left = self.sortList(left_head)
	sorted_right = self.sortList(right_head)
	
	# 步骤3：合并两个有序链表
	return self._merge_two_sorted_linked_lists(sorted_left, sorted_right)

def _is_linked_list_empty_or_single_node(self, head: ListNode) -> bool:
	"""辅助函数：判断链表是否为空或只有一个节点"""
	return not head or not head.next

def _find_mid_prev_node(self, head: ListNode) -> ListNode:
	"""
	辅助函数：找到链表中点的前一个节点
	例如：1->2->3->4 返回2；1->2->3 返回1
	"""
	if not head or not head.next:
		return head
	
	slow, fast = head, head.next
	while fast and fast.next:
		slow = slow.next       # 慢指针走1步
		fast = fast.next.next  # 快指针走2步
	return slow

def _split_linked_list(self, head: ListNode) -> tuple[ListNode, ListNode]:
	"""
	辅助函数：将链表拆分为左右两部分
	返回值：(左半部分头节点, 右半部分头节点)
	"""
	# 找到中点前一个节点
	mid_prev = self._find_mid_prev_node(head)
	# 拆分右半部分
	right_head = mid_prev.next
	# 切断左右连接
	mid_prev.next = None
	return head, right_head

def _merge_two_sorted_linked_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
	"""
	辅助函数：合并两个有序链表（原地修改，不开辟新空间）
	返回值：合并后的链表头节点
	"""
	# 创建虚拟头节点简化操作
	dummy = ListNode(0)
	current = dummy
	
	# 循环比较两个链表的节点值，选择更小的节点拼接
	while l1 and l2:
		if l1.val < l2.val:
			current.next = l1
			l1 = self._move_to_next_node(l1)
		else:
			current.next = l2
			l2 = self._move_to_next_node(l2)
		current = self._move_to_next_node(current)
	
	# 拼接剩余节点
	current.next = l1 if l1 else l2
	
	# 返回真实头节点
	return dummy.next

def _move_to_next_node(self, node: ListNode) -> ListNode:
	"""辅助函数：将节点指针移动到下一个节点（边界安全）"""
	return node.next if node else None
```
### 二叉树
### 树（Tree）
**平衡二叉树AVL** 是指该树所有节点的左右子树的高度相差不超过 1，包括AVL树和红黑树。
完全二叉树 是指节点按层紧凑排列，底层靠左连续，必定是平衡二叉树。
满二叉树 就是除最后一层节点外，其他所有节点都有两个子结点，必定是完全二叉树。
**翻转二叉树** 是指该树所有节点的左右子树互换。
哈夫曼树（带权路径长度最短的二叉树，构建方法：选择权值最小的两个节点作为左右子树，父节点权值为两者之和，重复直至形成一棵树。最优前缀编码，压缩算法）。
#### 遍历
**调用自己为递，return就是归**
```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []
	return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
```
**迭代解法本质上是在模拟递归，因为在递归的过程中使用了系统栈，所以在迭代的解法中常用 Stack 来模拟系统栈。**

|遍历方式|顺序|根节点处理时机|能否 “边走边处理”|
|---|---|---|---|
|前序|根→左→右|第一次遇到根节点就处理（加入 res）|✅ 完全同步|
|中序|左→根→右|左子树遍历完，第一次弹栈时处理|✅ 基本同步|
|后序|左→右→根|左右子树都遍历完，第二次遇到根才处理|❌ 必须 “回头处理”|

```python
def preorderTraversal(self,root:Optional[TreeNode]) -> List[int]:
	res = []
	stk = []
	while(root or len(stk)):
		while root:
			res.append(root.val)
			stk.append(root)
			root = root.left
		root = stk.pop()
		root = root.right
	return res

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	res = []
	stk = []
	while(root or len(stk)):
		while root:
			stk.append(root)
			root = root.left
		root = stk.pop()
		res.append(root.val)
		root = root.right
	return res

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	if not root:
		return []
	res = []
	stk = []
	while root or stk:
		while root:
			res.append(root.val)
			stk.append(root)
			root = root.right
		root = stk.pop()
		root = root.left
	return res[::-1]
```

#### 自顶向下 DFS（先序遍历）
在「递」的过程中维护值。
##### 求二叉树最大深度
**树的最大深度就是高度**！一个节点的最大深度 = 1（自身） + max (左子树的最大深度，右子树的最大深度)；如果节点为空，深度为 0（递归终止条件）。
这本质是后序遍历的思想：先递归计算左右子树的深度（处理子节点），再计算当前节点的深度（处理父节点）。
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
	    return 0
	return self.maxDepth(root.left) + self.maxDepth(root.right) + 1
```

#### 自底向上 DFS（后序遍历）
在「归」的过程中计算。
##### 例题—合并二叉树
[617. 合并二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/merge-two-binary-trees/solutions/2387255/kan-dao-di-gui-jiu-yun-dai-ni-li-jie-di-leixm/)
```python
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
	if root1 is None: return root2
	if root2 is None: return root1
	return TreeNode(root1.val + root2.val,
		self.mergeTrees(root1.left, root2.left),    # 合并左子树
		self.mergeTrees(root1.right, root2.right))  # 合并右子树
```
#### 二叉搜索树BST
节点的左子树仅包含键 **小于** 节点键的节点。节点的右子树仅包含键 **大于** 节点键的节点。左右子树也必须是二叉搜索树。
**平衡的二叉搜索树插入、查找的时间复杂度都是 O(logn)**
##### 例题—把二叉搜索树转换为累加树
[538. 把二叉搜索树转换为累加树 - 力扣（LeetCode）](https://leetcode.cn/problems/convert-bst-to-greater-tree/)
遍历顺序是：右、根、左
```python
def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
	s  = 0
	def dfs(node:TreeNode) -> None:
		if node is None:
			return
		dfs(node.right)
		nonlocal s
		s += node.val
		node.val = s
		dfs(node.left)
	dfs(root)
	return root
```
[98. 验证二叉搜索树 - 力扣（LeetCode）](https://leetcode.cn/problems/validate-binary-search-tree/solutions/2020306/qian-xu-zhong-xu-hou-xu-san-chong-fang-f-yxvh/)
```python
def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
	if root is None:
		return True
	x = root.val
	return left < x < right and \
		   self.isValidBST(root.left, left, x) and \
		   self.isValidBST(root.right, x, right)
、
pre = -inf
def isValidBST(self, root: Optional[TreeNode]) -> bool:
	if root is None:
		return True
	if not self.isValidBST(root.left):  # 左
		return False
	if root.val <= self.pre:  # 中
		return False
	self.pre = root.val
	return self.isValidBST(root.right)  # 右
```
##### 例题—将有序数组转换为平衡二叉搜索树
**二叉搜索树中序遍历后就会变成升序数组！**
给定二叉搜索树的中序遍历，不能确定唯一的平衡二叉搜索树。
[108. 将有序数组转换为二叉搜索树 - 力扣（LeetCode）](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)
```python
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
	def dfs(left,right):
		if left> right:
			return None
		mid = left + (right-left)//2 # 升序数组
		root = TreeNode(nums[mid])
		root.left = dfs(left,mid-1)
		root.right = dfs(mid+1,right)
		return root
	return dfs(0,len(nums)-1)
```
##### 例题—删除二叉搜索树中的节点
[450. 删除二叉搜索树中的节点 - 力扣（LeetCode）](https://leetcode.cn/problems/delete-node-in-a-bst/)
**被删除的节点有左右子树的情况下，将比 root 大的最小节点，即它的右子树中的最小节点（记作successor）作为新的根节点替代 root**，简单证明，successor 位于 root 的右子树中，因此大于 root 的所有左子节点；successor 是 root 的右子树中的最小节点，因此小于 root 的右子树中的其他节点。以上两点保持了新子树的有序性。
#### 创建二叉树
仿照遍历的过程构造二叉树，一定要记得调用TreeNode
[654. 最大二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-binary-tree/solutions/1762400/zhua-wa-mou-si-by-muse-77-myd7/)
这道题能用单调栈做，直呼666
#### 二叉树BFS
「层序遍历」、「最短路径」只能用BFS。**双数组（两个列表交替）** 和 **队列** 本质都是实现「先进先出（FIFO）」的遍历逻辑，**绝大多数场景下可以互换**，都是为了保证 “先处理当前层的所有节点，再处理下一层节点”：
##### 层序遍历
[102. 二叉树的层序遍历 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	if not root:
		return []
	res = []
	cur = deque([root])
	while cur:
		value = []
		for _ in range(len(cur)):
			node = cur.popleft()
			value.append(node.val)
			if node.left: cur.append(node.left)
			if node.right: cur.append(node.right)
		res.append(list(value))
	return res
```
#### 二叉树与链表
[114. 二叉树展开为链表 - 力扣（LeetCode）](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)
```python
def flatten(self, root: TreeNode) -> None:
	curr = root
	while curr:
		if curr.left:
			predecessor = nxt = curr.left
			while predecessor.right:
				predecessor = predecessor.right
			predecessor.right = curr.right
			curr.left = None
			curr.right = nxt
		curr = curr.right
```
[1367. 二叉树中的链表 - 力扣（LeetCode）](https://leetcode.cn/problems/linked-list-in-binary-tree/solutions/3034003/dan-di-gui-xie-fa-pythonjavacgo-by-endle-00js/)
```python
# 仔细品这个判断逻辑  
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
	realHead = head
	def dfs(cur: Optional[ListNode], root: Optional[TreeNode]) -> bool:
		res = False
		if not cur:
			return True
		if not root:
			return False
		if cur.val == root.val:
			# 下面这个if很重要，不能直接return
			if dfs(cur.next,root.left) or dfs(cur.next,root.right):return True
		return cur is realHead and (dfs(head,root.right) or dfs(head,root.left))
# 如果不在前面加cur is realHead判断就会导致大量重复递归，超时！请细品
	return dfs(head,root)
```
[109. 有序链表转换平衡二叉搜索树 - 力扣（LeetCode）](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/)
```python
# 学习一下怎么找链表中点！记住
def sortedListToBST(self, head: ListNode) -> TreeNode:
	def getMedian(left: ListNode, right: ListNode) -> ListNode:
		fast = slow = left
		while fast != right and fast.next != right:
			fast = fast.next.next
			slow = slow.next
		return slow
	
	def buildTree(left: ListNode, right: ListNode) -> TreeNode:
		if left == right:
			return None
		mid = getMedian(left, right)
		root = TreeNode(mid.val)
		root.left = buildTree(left, mid)
		root.right = buildTree(mid.next, right)
		return root
	
	return buildTree(head, None)
	
# 方法二：中序遍历还能这么用，666
def sortedListToBST(self, head: ListNode) -> TreeNode:
	def getLength(head: ListNode) -> int:
		ret = 0
		while head:
			ret += 1
			head = head.next
		return ret
	
	def buildTree(left: int, right: int) -> TreeNode:
		if left > right:
			return None
		mid = (left + right + 1) // 2
		root = TreeNode()
		root.left = buildTree(left, mid - 1)
		nonlocal head
		root.val = head.val
		head = head.next
		root.right = buildTree(mid + 1, right)
		return root
	
	length = getLength(head)
	return buildTree(0, length - 1)
```
### 一般树
对于完全一般的树，建议用图论来解决。
#### N叉树
N叉树没有中序遍历，没有前序、后序和层序。
B 树（**平衡多路搜索树**，每个节点最多有 m 个子节点（m 为树的阶数），适用于磁盘索引场景（减少 I/O 次数）） 
B + 树（所有叶子节点包含全部关键字及指向数据的指针，且叶子节点按顺序链接（便于范围查询），数据库索引）
```python
def preorder(self, root: 'Node') -> List[int]:
	res = []
	if root is None:
		return res
	res.append(root.val)
	for child in root.children:
		res += self.preorder(child)
	return res
        
def preorder(self, root: 'Node') -> List[int]:
	if root is None:
		return []
	res = []
	stk = [root]
	while stk:
		node = stk.pop()
		res.append(node.val)
		stk.extend(reversed(node.children))
	return res

def postorder(self, root: 'Node') -> List[int]:
	if not root:
		return []
	res = []
	stk = [root]
	vis = set()
	while stk:
		node = stk[-1]
		if len(node.children) == 0 or node in vis:
			res.append(node.val)
			stk.pop()
			continue
		stk.extend(reversed(node.children))
		vis.add(node)
	return res
```

[2368. 受限条件下可到达节点的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/reachable-nodes-with-restrictions/solutions/2662538/shu-shang-dfspythonjavacgojsrust-by-endl-0r3a/)
```python
# DFS解法
def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
	r = set(restricted)  #提升查询效率，否则超时
	g = [[] for _ in range(n)]
	for x,y in edges:
		if x not in r and y not in r:
			g[x].append(y)
			g[y].append(x)
	def dfs(x:int,fa:int) -> int:
		cnt = 1
		for y in g[x]:
			if y!=fa:
				cnt += dfs(y,x)
		return cnt
	return dfs(0,-1)
#BFS解法 	
def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
	reachable_dict = defaultdict(set)
	ans = set()
	ans.add(0)
	restricted_node = set(restricted)
	for edge in edges:
		if edge[0] not in restricted_node and edge[1] not in restricted_node:
			reachable_dict[edge[0]].add(edge[1])
			reachable_dict[edge[1]].add(edge[0])
	dequeue = deque([0])
	while dequeue:
		node = dequeue.popleft()
		for neighbor in reachable_dict[node]:
			if neighbor not in ans:
				ans.add(neighbor)
				dequeue.append(neighbor)
	return len(ans)
```
### 回溯
回溯是在递归的基础上，尝试所有可能的解，并在不满足条件时回退，撤销上一步的决策。如果在某个选择上不确定它是否能得到想要的答案，或者在相同情况下其他选择也可能得到答案，那么需要用回溯来枚举所有可能。
**回溯有一个增量构造答案的过程，这个过程一般是用DFS实现。** 
#### 二叉树回溯
##### 例题—路径总和
[113. 路径总和 II - 力扣（LeetCode）](https://leetcode.cn/problems/path-sum-ii/submissions/685657397/)
```python
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
	ans = []
	path = []
	def findPath(root:Optional[TreeNode],targetSum:int) -> None:
		if not root:
			return
		path.append(root.val)
		if not root.left and not root.right and targetSum == root.val:
			ans.append(list(path))
		else:
			findPath(root.left,targetSum-root.val)
			findPath(root.right,targetSum-root.val)
		path.pop()
	findPath(root,targetSum)
	return ans
```
[437. 路径总和 III - 力扣（LeetCode）](https://leetcode.cn/problems/path-sum-iii/)
#### 子集型回溯
[78. 子集 - 力扣（LeetCode）](https://leetcode.cn/problems/subsets/)
使用枚举或者选不选的思想，构建一棵树，如果是枚举，那么树上每个节点都是答案，如果是选不选，那么只有树的叶子节点是答案。
回溯三问：当前操作是什么，子问题是什么，下一个子问题是什么。
```python
# 选不选
def subsets(self, nums: List[int]) -> List[List[int]]:
	n = len(nums)
	ans = []
	path = []

	def dfs(i: int) -> None:
		if i == n:  # 子集构造完毕
			ans.append(path.copy())  # 复制 path，也可以写 path[:]
			return
			
		# 不选 nums[i]
		dfs(i + 1)
		
		# 选 nums[i]
		path.append(nums[i])
		dfs(i + 1)
		path.pop()  # 恢复现场

	dfs(0)
	return ans

# 枚举
def subsets(self, nums: List[int]) -> List[List[int]]:
	n = len(nums)
	ans = []
	path = []

	def dfs(i: int) -> None:
		ans.append(path.copy())  # 复制 path
		for j in range(i, n):  # 枚举选择的数字
			path.append(nums[j])
			dfs(j + 1)
			path.pop()  # 恢复现场

	dfs(0)
	return ans
```

## 网格图	
**网格图是一种简化的图，默认是无向无权图。**
存储图的方式有：邻接表（数组存储所有顶点，每个顶点对应一个链表，记录其邻接顶点及边权（带权图），空间省，适合稀疏图；可以用列表、哈希表实现）、邻接矩阵（二维数组存储边的权值S，查询边 O (1)，适合稠密图。用二维列表实现）
### 岛屿问题！
[200. 岛屿数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-islands/solutions/211211/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/)
```python
def dfs(grid: List[List[str]], r: int, c: int) -> None:
    # param grid: 二维网格数组，1=未访问的岛屿，0=海洋/障碍，2=已访问的岛屿
    # 1. 判断 base case：坐标超出网格范围,不是未访问的岛屿（是海洋/已遍历）则返回
    if (not (0 <= r < len(grid) and 0 <= c < len(grid[0]))) or grid[r][c] != '1':
        return
    # 2. 标记当前格子为「已遍历」，避免重复访问
    grid[r][c] = '2'
    
    # 3. 递归访问上、下、左、右四个相邻结点
    dfs(grid, r - 1, c)  # 上
    dfs(grid, r + 1, c)  # 下
    dfs(grid, r, c - 1)  # 左
    dfs(grid, r, c + 1)  # 右
# 普通bfs模板
def bfs(grid, i, j):
    queue = deque()
    queue.extend([[i, j]])
    while queue:
        i, j = queue.popleft()
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '2'  
            queue.extend([[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]])

def numIslands(grid: List[List[str]]) -> int:
	rows = len(grid)
	if rows == 0:
		return 0
	cols = len(grid[0])
	ans = 0
	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == '1':
				ans += 1
				# 二选一运行即可
				bfs(grid,r,c)
				# dfs(grid,r,c)
	return ans
```
### 网格图 DFS
DFS不撞南墙不回头，**适用于需要计算连通块个数、大小的题目。**

|      | 二叉树        | 网格图          |
| ---- | ---------- | ------------ |
| 递归入口 | 根节点        | 网格图的某个格子     |
| 递归方向 | 左儿子和右儿子    | 一般为左右上下的相邻格子 |
| 递归边界 | 空节点（或者叶节点） | 出界、遇到障碍或者已访问 |
```python
# 网格图DFS遍历模板
def dfs(grid: List[List[str]], r: int, c: int) -> None:
    # param grid: 二维网格数组，1=未访问的岛屿，0=海洋/障碍，2=已访问的岛屿
    # 1. 判断 base case：坐标超出网格范围,不是未访问的岛屿（是海洋/已遍历）则返回
    if (not (0 <= r < len(grid) and 0 <= c < len(grid[0]))) or grid[r][c] != '1':
        return
    # 2. 标记当前格子为「已遍历」，避免重复访问
    grid[r][c] = '2'
    
    # 3. 递归访问上、下、左、右四个相邻结点
    dfs(grid, r - 1, c)  # 上
    dfs(grid, r + 1, c)  # 下
    dfs(grid, r, c - 1)  # 左
    dfs(grid, r, c + 1)  # 右
```
### 网格图 BFS
[1926. 迷宫中离入口最近的出口 - 力扣（LeetCode）](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/solutions/869437/go-bfs-by-endlesscheng-k2cu/)
BFSBFS 是先访问近的，再访问远的。**天然具有层序遍历特性，最适合用来解决需要计算最短距离（最短路径）的题目。**
```python
def nearestExit(self,maze: List[List[str]], entrance: List[int]) -> int:
	rows, cols = len(maze), len(maze[0]) if maze else 0
	if rows == 0 or cols == 0:
		return -1
	
	# 初始化队列+访问标记+父节点（用于回溯路径）
	q = deque([entrance])
	vis = [[False] * cols for _ in range(rows)]
	parent = [[None] * cols for _ in range(rows)]
	vis[entrance[0]][entrance[1]] = True
	steps = 0  # 记录步数
	
	while q:
		for _ in range(len(q)):
			r, c = q.popleft()
			
			# 判定出口（边界且非入口）
			if (r in (0, rows-1) or c in (0, cols-1)) and [r, c] != entrance:
				# 回溯路径
				path = []
				curr = (r, c)
				while curr != (entrance[0], entrance[1]):
					path.append(list(curr))
					curr = parent[curr[0]][curr[1]]
				path.append(entrance)
				path.reverse()
				return steps
			
			# 直接枚举上下左右四个方向（取消方向数组）
			for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
				# 边界+可通行+未访问检查
				if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and not vis[nr][nc]:
					vis[nr][nc] = True
					parent[nr][nc] = (r, c)
					q.append([nr, nc])
		steps += 1  # 每一层处理完，步数+1
	# 无出口时返回-1
	return -1
```
#### 网格图 0-1 BFS
边权只有 0 和 1 的题目，也可以用 BFS 做。
[3286. 穿越网格图的安全路径 - 力扣（LeetCode）](https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/description/)
```python
def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
	rows = len(grid)
	if rows == 0:
		return False
	cols = len(grid[0])
	ans = False
	queue = deque()
	queue.append([0,0])
	health_grid = [[0 for _ in range(cols)] for _ in range(rows)]
	health_grid[0][0] = health-grid[0][0] #初始化
	while queue:
		for _ in range(len(queue)):
			r,c = queue.popleft()
			for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
				if 0<=nr<rows and 0<=nc<cols and  health_grid[r][c]-grid[nr][nc] > health_grid[nr][nc] >= 0 :
					health_grid[nr][nc] = health_grid[r][c]-grid[nr][nc]
					queue.append([nr,nc])
	if health_grid[rows-1][cols-1] > 0:
		return True
	return False
```

### 网格图 Dijkstra
BFS 是 Dijkstra 算法的**特殊情况**（所有边的权重为 1 时，Dijkstra 退化为 BFS）。
定义$g[i][j]$表示节点$i$到节点$j$这条边的边权。如果没有$i$到$j$的边，则$g[i][j] = \infty$。
定义$dis[i]$表示起点$k$到节点$i$的最短路长度，一开始$dis[k] = 0$，其余$dis[i] = \infty$表示尚未计算出。
我们的目标是计算出最终的$dis$数组。
- 首先更新起点$k$到其邻居$y$的最短路，即更新$dis[y]$为$g[k][y]$。
- 然后取除了起点$k$以外的$dis[i]$的最小值，假设最小值对应的节点是3。此时可以断言：$dis[3]$已经是$k$到3的最短路长度，不可能有其它$k$到3的路径更短！反证法：假设存在更短的路径，那我们一定会从$k$出发经过一个点$u$，它的$dis[u]$比$dis[3]$还要小，然后再经过一些边到达3，得到更小的$dis[3]$。但$dis[3]$已经是最小的了，并且图中没有负数边权，所以$u$是不存在的，矛盾。故原命题成立，此时我们得到了$dis[3]$的最终值。
- 用节点3到其邻居$y$的边权$g[3][y]$更新$dis[y]$：如果$dis[3] + g[3][y] < dis[y]$，那么更新$dis[y]$为$dis[3] + g[3][y]$，否则不更新。
- 然后取除了节点$k,3$以外的$dis[i]$的最小值，重复上述过程。
- 由数学归纳法可知，这一做法可以得到每个点的最短路。当所有点的最短路都已确定时，算法结束。
#### 例题——网络延迟时间
[743. 网络延迟时间 - 力扣（LeetCode）](https://leetcode.cn/problems/network-delay-time/solutions/2668220/liang-chong-dijkstra-xie-fa-fu-ti-dan-py-ooe8/)
##### 朴素 Dijkstra
```python
# 适用于稠密图：边的数量级和 n2 相当的图。
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
	# 构建邻接矩阵，g[i][j]表示节点i+1到j+1的路径长度，初始为无穷大（不可达）
	g = [[inf for _ in range(n)] for _ in range(n)]  
	for x, y, d in times:
		g[x - 1][y - 1] = d  # 节点编号转0索引
	
	# dis[i]：起点k到节点i+1的当前最短路径长度，初始为无穷大
	dis = [inf] * n
	ans = dis[k - 1] = 0  # 起点到自身路径长度为0，ans存最大最短路径长度
	
	# done[i]=True：节点i+1的最短路径长度已确定
	done = [False] * n

	while True:
		# 找未确定的、路径长度最短的节点x
		x = -1
		for i, ok in enumerate(done):
			if not ok and (x < 0 or dis[i] < dis[x]):
				x = i
		
		if x < 0:  # 所有节点已确定
			return ans
		if dis[x] == inf:  # 存在不可达节点
			return -1
		
		ans = dis[x]  # 最短路径长度递增，最终为最大值
		done[x] = True  # 标记该节点路径长度已确定
		
		# 用节点x更新其邻居的最短路径长度
		for y, d in enumerate(g[x]):
			dis[y] = min(dis[y], dis[x] + d)
```
##### 堆优化 Dijkstra
寻找最小值的过程可以用一个最小堆来快速完成：
- 一开始把$(dis[k], k)$二元组入堆。
- 当节点$x$首次出堆时，$dis[x]$就是写法一中寻找的最小最短路。
- 更新$dis[y]$时，把$(dis[y], y)$二元组入堆。
注意，如果一个节点$x$在出堆前，其最短路长度$dis[x]$被多次更新，那么堆中会有多个重复的$x$，并且包含$x$的二元组中的$dis[x]$是互不相同的（因为我们只在找到更小的最短路时才会把二元组入堆）。
所以写法一中的$done$数组可以省去，取而代之的是用出堆的最短路值（记作$dx$）与当前的$dis[x]$比较，如果$dx > dis[x]$说明$x$之前出堆过，我们已经更新了$x$的邻居的最短路，所以这次就不用更新了，继续外层循环。
```python
# 适用于稀疏图
from typing import List
import heapq
import math

inf = math.inf

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
	# 构建邻接表：g[x]存储(x可直达的邻居y, 路径长度d)
	g = [[] for _ in range(n)]  
	for x, y, d in times:
		g[x - 1].append((y - 1, d))  # 节点编号转0索引

	# 初始化最短路径数组，起点k到自身长度为0
	dis = [inf] * n
	dis[k - 1] = 0

	# 最小堆存储(当前最短路径长度, 节点)，初始加入起点
	h = [(0, k - 1)]  

	while h:
		dx, x = heapq.heappop(h)  # 弹出当前最短路径的节点
		if dx > dis[x]:  # 该节点已处理过，跳过
			continue
		# 遍历邻居并更新最短路径
		for y, d in g[x]:
			new_dis = dx + d
			if new_dis < dis[y]:
				dis[y] = new_dis
				heapq.heappush(h, (new_dis, y))

	mx = max(dis)  # 所有节点最短路径的最大值（最晚到达时间）
	return mx if mx < inf else -1  # 有不可达节点返回-1，否则返回最大值
```
## 图论
#### DFS计算每个连通块的大小
```python
def solve(n: int, edges: List[List[int]]) -> List[int]:
    # 节点编号从 0 到 n-1
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    vis = [False] * n

    def dfs(x: int) -> int:
        vis[x] = True  # 避免重复访问节点
        size = 1
        for y in g[x]:
            if not vis[y]:
                size += dfs(y)
        return size

    # 计算每个连通块的大小
    ans = []
    for i, b in enumerate(vis):
        if not b:  # i 没有访问过
            size = dfs(i)
            ans.append(size)
    return ans
```
#### BFS单源最短路
```python
# 计算从 start 到各个节点的最短路长度
# 如果节点不可达，则最短路长度为 -1
# 节点编号从 0 到 n-1，边权均为 1
def bfs(n: int, edges: List[List[int]], start: int) -> List[int]:
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    dis = [-1] * n  # -1 表示尚未访问到
    dis[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:
                dis[y] = dis[x] + 1
                q.append(y)
    return dis
```
### 拓扑排序
在图上的「排序」，可以把杂乱的点排成一排。前提条件是图中无环，从而保证每条边都是从排在前面的点，指向排在后面的点。
```python
# 返回有向无环图（DAG）的其中一个拓扑序
# 如果图中有环，返回空列表
# 节点编号从 0 到 n-1
def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in edges:
        g[x].append(y)
        in_deg[y] += 1  # 统计 y 的先修课数量

    topo_order = []
    q = deque(i for i, d in enumerate(in_deg) if d == 0)  # 没有先修课，可以直接上
    while q:
        x = q.popleft()
        topo_order.append(x)
        for y in g[x]:
            in_deg[y] -= 1  # 修完 x 后，y 的先修课数量减一
            if in_deg[y] == 0:  # y 的先修课全部上完
                q.append(y)  # 加入学习队列

    if len(topo_order) < n:  # 图中有环
        return []
    return topo_order
```

### 单源最短路：Dijkstra 算法
```python
# 返回从起点 start 到每个点的最短路长度 dis，如果节点 x 不可达，则 dis[x] = math.inf
# 要求：没有负数边权
# 时间复杂度 O(n + mlogm)，其中 m 是 edges 的长度。注意堆中有 O(m) 个元素
def shortestPathDijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    # 注：如果节点编号从 1 开始（而不是从 0 开始），可以把 n 加一
    g = [[] for _ in range(n)]  # 邻接表
    for x, y, wt in edges:
        g[x].append((y, wt))
        # g[y].append((x, wt))  # 无向图加上这行

    dis = [inf] * n
    dis[start] = 0  # 起点到自己的距离是 0
    h = [(0, start)]  # 堆中保存 (起点到节点 x 的最短路长度，节点 x)

    while h:
        dis_x, x = heappop(h)
        if dis_x > dis[x]:  # x 之前出堆过
            continue
        for y, wt in g[x]:
            new_dis_y = dis_x + wt
            if new_dis_y < dis[y]:
                dis[y] = new_dis_y  # 更新 x 的邻居的最短路
                # 懒更新堆：只插入数据，不更新堆中数据
                # 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                heappush(h, (new_dis_y, y))

    return dis

```

### 最小生成树
如果要求最大生成树，把边权从大到小排序。
```python
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一
        return True


# 计算图的最小生成树的边权之和
# 如果图不连通，返回 math.inf
# 节点编号从 0 到 n-1
# 时间复杂度 O(n + mlogm)，其中 m 是 edges 的长度
def mstKruskal(n: int, edges: List[List[int]]) -> int:
    edges.sort(key=lambda e: e[2])

    uf = UnionFind(n)
    sum_wt = 0
    for x, y, wt in edges:
        if uf.merge(x, y):
            sum_wt += wt

    if uf.cc > 1:  # 图不连通
        return inf
    return sum_wt
```

## 动态规划DP
动态规划能解决的问题，必须满足两个核心条件：
**原问题的最优解，可以由子问题的最优解推导出来**。
**一旦确定了子问题的解，后续推导原问题时，不会再改变子问题的解**。
### 入门 DP
**Dynamic Programming，有 记忆化搜索和递推两种基本方法**
**首先找状态方程$dfs(i) = dfs(i - 1) + dfs(i - 2)$ ， 然后确定状态边界**
如果整个递归中有大量重复递归调用（递归入参相同），针对有重复子问题的递归，用**记忆化搜索**来优化，如果一个状态（递归入参）是第一次遇到，那么可以在返回前，把状态及其结果记到一个 memo 数组中。如果一个状态不是第一次遇到（memo 中保存的结果不等于 memo 的初始值），那么可以直接返回 memo 中保存的结果。注意memo 数组的**初始值**一定不能等于要记忆化的值！
Python中可以直接用记忆化神器 函数装饰器@cache ，**自动记录函数的「入参→返回值」映射**，本质是个哈希表字典。
[70. 爬楼梯 - 力扣（LeetCode）](https://leetcode.cn/problems/climbing-stairs/description/)
**递归 + 记录返回值 = 记忆化搜索**
```python
def climbStairs(self, n: int) -> int:
	@cache
	def dfs(i:int) -> int:
		if i == 0:
			return 1
		if i<0:
			return 0
		return dfs(i-1)+dfs(i-2)
	return dfs(n)
```
**使用递推，需要找到递推式$f[i]=f[i−1]+f[i−2]$，然后确定边界**
```python
def climbStairs(self, n: int) -> int:
	f = [0] * (n+1)
	f[0] = f[1] = 1
	for i in range(2,n+1):
		f[i] = f[i-1] + f[i-2]  
	return f[n]  
# 可以优化为O（1）
def climbStairs(self, n: int) -> int:
	f1 = f0 = 1
	for i in range(2,n+1):
		new_f = f1 + f0
		f0 = f1
		f1 = new_f  
	return f1
```
### 网格图 DP
对于一些二维 DP（例如背包、最长公共子序列），如果把 DP 矩阵画出来，其实状态转移可以视作**在网格图上的移动**。
[1594. 矩阵的最大非负积 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/description/)
```python
def maxProductPath(self, grid: List[List[int]]) -> int:
	mod = 10**9 + 7
	m, n = len(grid), len(grid[0])
	# 需要存储的是移动过程中的积的范围
	maxgt = [[0] * n for _ in range(m)]
	minlt = [[0] * n for _ in range(m)]

	maxgt[0][0] = minlt[0][0] = grid[0][0]
	for i in range(1, n):
		maxgt[0][i] = minlt[0][i] = maxgt[0][i - 1] * grid[0][i]
	for i in range(1, m):
		maxgt[i][0] = minlt[i][0] = maxgt[i - 1][0] * grid[i][0]
	
	for i in range(1, m):
		for j in range(1, n):
			if grid[i][j] >= 0:
				maxgt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
				minlt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
			else:
				maxgt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
				minlt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
	
	if maxgt[m - 1][n - 1] < 0:
		return -1
	return maxgt[m - 1][n - 1] % mod
```

### 背包
每个物品只能选一次，即要么选，要么不选。 0-1 背包是「选或不选」的代表。
[416. 分割等和子集 - 力扣（LeetCode）](https://leetcode.cn/problems/partition-equal-subset-sum/solutions/2785266/0-1-bei-bao-cong-ji-yi-hua-sou-suo-dao-d-ev76/)
```python
def canPartition(self, nums: List[int]) -> bool:
	@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
	def dfs(i: int, j: int) -> bool:
		if i < 0:
			return j == 0
		if j < nums[i]:
			return dfs(i - 1, j)  # 只能不选
		return dfs(i - 1, j - nums[i]) or dfs(i - 1, j)  # 选或不选

	s = sum(nums)
	return s % 2 == 0 and dfs(len(nums) - 1, s // 2)
```

### 经典线性 DP
[1143. 最长公共子序列 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-common-subsequence/description/)
```python
def longestCommonSubsequence(self, s: str, t: str) -> int:
	n, m = len(s), len(t)
	@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
	def dfs(i: int, j: int) -> int:
		if i < 0 or j < 0:
			return 0
		if s[i] == t[j]:
			return dfs(i - 1, j - 1) + 1
		return max(dfs(i - 1, j), dfs(i, j - 1))
	return dfs(n - 1, m - 1)
```

### 划分型 DP




### 状态机 DP