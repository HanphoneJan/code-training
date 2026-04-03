#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start
# @lcpr-template-end
# @lc code=start
# 方法一：双栈实现
class MinStack:
    """
    155. 最小栈 - 双栈实现

    核心思想：
    普通栈只能 O(1) 获取栈顶，但要 O(1) 获取最小值，需要额外维护一个最小值栈。
    - stack：主栈，存储所有元素
    - min_stack：辅助栈，存储每个状态下的最小值

    操作流程：
    - push(x)：主栈 push(x)，辅助栈 push(min(x, 当前最小值))
    - pop()：两个栈同时 pop
    - top()：返回主栈栈顶
    - getMin()：返回辅助栈栈顶

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


# 方法二：单栈元组实现
class MinStack2:
    """
    155. 最小栈 - 单栈元组实现

    核心思想：
    每个栈元素存储一个元组 (val, min_val)，表示当前值和栈底到当前位置的最小值。
    栈底哨兵 (0, inf) 避免空栈判断。
    """

    def __init__(self):
        # 这里的 0 写成任意数都可以，反正用不到
        self.st = [(0, 2**31)]  # 栈底哨兵

    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end


if __name__ == "__main__":
    print("最小栈 - 测试开始")

    # 测试 MinStack
    print("测试 MinStack:")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"  getMin() = {minStack.getMin()}, 期望 = -3")
    minStack.pop()
    print(f"  top() = {minStack.top()}, 期望 = 0")
    print(f"  getMin() = {minStack.getMin()}, 期望 = -2")

    # 测试 MinStack2
    print("测试 MinStack2:")
    minStack2 = MinStack2()
    minStack2.push(-2)
    minStack2.push(0)
    minStack2.push(-3)
    print(f"  getMin() = {minStack2.getMin()}, 期望 = -3")
    minStack2.pop()
    print(f"  top() = {minStack2.top()}, 期望 = 0")
    print(f"  getMin() = {minStack2.getMin()}, 期望 = -2")

    print("测试结束")
