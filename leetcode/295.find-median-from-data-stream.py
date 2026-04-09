#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
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

    为什么这样设计？
    - 通过 heappushpop 保证每次插入后堆的平衡性
    - Python 的 heapq 只支持小顶堆，大顶堆用负数模拟

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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



#


if __name__ == "__main__":
    # 测试用例 1
    print("Test 1:")
    mf = MedianFinder()
    operations = [("addNum", 1), ("addNum", 2), ("findMedian", None), ("addNum", 3), ("findMedian", None)]
    expected = [None, None, 1.5, None, 2.0]

    results = []
    for op, val in operations:
        if op == "addNum":
            mf.addNum(val)
            results.append(None)
        else:
            results.append(mf.findMedian())

    print(f"Operations: {operations}")
    print(f"Results: {results}")
    print(f"Expected: {expected}")
    print(f"{'✓ PASS' if results == expected else '✗ FAIL'}")
    print()

    # 测试用例 2
    print("Test 2:")
    mf2 = MedianFinder()
    mf2.addNum(-1)
    print(f"addNum(-1), median = {mf2.findMedian()}")  # -1
    mf2.addNum(-2)
    print(f"addNum(-2), median = {mf2.findMedian()}")  # -1.5
    mf2.addNum(-3)
    print(f"addNum(-3), median = {mf2.findMedian()}")  # -2
    mf2.addNum(-4)
    print(f"addNum(-4), median = {mf2.findMedian()}")  # -2.5
    mf2.addNum(-5)
    print(f"addNum(-5), median = {mf2.findMedian()}")  # -3
