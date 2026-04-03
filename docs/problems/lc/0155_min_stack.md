---
title: 最小栈
platform: LeetCode
difficulty: 简单
id: 155
url: https://leetcode.cn/problems/min-stack/
tags:
  - 栈
  - 设计
topics:
  - ../../topics/stack.md
  - ../../topics/design.md
patterns:
  - ../../topics/stack.md
date_added: 2026-04-03
date_reviewed: []
---

# 0155. 最小栈

## 题目描述

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

## 示例

**示例:**
```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

---

## 解题思路

### 第一步：分析需求

普通栈的操作（push、pop、top）本来就是 `O(1)`。难点在于 `getMin()` 也要求 `O(1)`。

如果每次 `getMin()` 时遍历整个栈，时间复杂度是 `O(n)`，不满足要求。

### 第二步：暴力解法

维护一个变量记录当前最小值。但 `pop` 时如果弹出的正好是最小值，就需要重新遍历找新的最小值，最坏 `O(n)`。

### 第三步：最优解法 - 双栈 / 单栈元组

#### 方法一：双栈实现
- 主栈 `stack`：正常存储所有元素
- 辅助栈 `min_stack`：存储每个状态下的最小值

每次 `push` 时，`min_stack` 同步 push 当前最小值。
每次 `pop` 时，两个栈同时 pop。
`getMin()` 直接返回 `min_stack` 栈顶。

#### 方法二：单栈元组
每个栈元素存一个元组 `(val, 当前最小值)`，栈底放一个哨兵。

两种方法的时间和空间复杂度相同。

---

## 完整代码实现

```python
class MinStack:
    """
    155. 最小栈 - 双栈实现

    核心思想：
    主栈正常存数据，辅助栈存每个状态下的最小值。
    这样 getMin() 永远是 O(1)。

    时间复杂度：所有操作 O(1)
    空间复杂度：O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = [2**31]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack2:
    """
    155. 最小栈 - 单栈元组实现

    核心思想：
    每个栈元素存储 (val, 当前最小值)，用栈底哨兵简化空栈判断。
    """

    def __init__(self):
        self.st = [(0, 2**31)]

    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
```

---

## 示例推演

操作序列：`push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()`

**双栈实现**：

| 操作 | stack | min_stack |
|------|-------|-----------|
| init | [] | [inf] |
| push(-2) | [-2] | [inf, -2] |
| push(0) | [-2, 0] | [inf, -2, -2] |
| push(-3) | [-2, 0, -3] | [inf, -2, -2, -3] |
| getMin() | | 返回 -3 |
| pop() | [-2, 0] | [inf, -2, -2] |
| top() | | 返回 0 |
| getMin() | | 返回 -2 |

**单栈元组实现**：

| 操作 | st |
|------|-----|
| init | [(0, inf)] |
| push(-2) | [(0, inf), (-2, -2)] |
| push(0) | [(0, inf), (-2, -2), (0, -2)] |
| push(-3) | [(0, inf), (-2, -2), (0, -2), (-3, -3)] |

两种实现效果完全一致。

---

## 复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 | 说明 |
|------|-----------|-----------|------|
| push | O(1) | O(n) | 主栈 + 辅助信息 |
| pop | O(1) | O(n) | |
| top | O(1) | O(n) | |
| getMin | O(1) | O(n) | **关键优化** |

---

## 易错点总结

### 1. 辅助栈的长度

辅助栈应该和主栈等长（或比主栈多一个哨兵），这样 `pop` 时才能同步。

### 2. getMin 时栈不能为空

题目保证 `getMin()` 调用时栈非空。

### 3. 哨兵值的选择

哨兵值要选得足够大（大于所有可能的输入），这样第一个元素 push 时不会影响最小值计算。

---

## 扩展思考

### 如果要求实现最大栈？

和最小栈完全对称，辅助栈存最大值即可。

### O(1) 返回中位数？

需要用两个堆（大顶堆 + 小顶堆），就是 [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/)。

## 相关题目

- [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)
- [225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)
- [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)
