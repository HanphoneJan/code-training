#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import deque


class Solution:
    """
    239. 滑动窗口最大值 - 单调队列解法

    核心思路：
    使用单调递减队列维护窗口内的最大值候选。队列中存储的是元素下标，
    对应的元素值从队首到队尾单调递减。

    为什么这样设计？
    - 队首始终是当前窗口的最大值
    - 新元素入队时，所有比它小的元素都不可能成为后续窗口的最大值，可以直接弹出
    - 使用下标可以判断队首元素是否已经滑出窗口

    算法流程（三步骤）：
    1. 右边入：新元素从队尾入队，维护单调递减性质
    2. 左边出：检查队首是否滑出窗口，若是则弹出
    3. 记录答案：当窗口形成后（i >= k-1），队首即为当前窗口最大值

    时间复杂度: O(n) - 每个元素最多入队出队各一次
    空间复杂度: O(k) - 队列中最多存储 k 个元素
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)  # 窗口个数为 n - k + 1
        q = deque()  # 双端队列，存储下标，对应元素值单调递减

        for i, x in enumerate(nums):
            # 步骤1：右边入 - 维护单调递减性质
            # 新元素 x 入队前，弹出所有比 x 小的元素
            # 这些被弹出的元素不可能成为后续窗口的最大值
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)  # 保存下标以便判断元素是否滑出窗口

            # 步骤2：左边出 - 检查队首是否滑出窗口
            left = i - k + 1  # 当前窗口的左端点
            if q[0] < left:   # 队首元素已不在窗口内
                q.popleft()

            # 步骤3：记录答案
            # 当窗口完全形成后（left >= 0），队首即为当前窗口最大值
            if left >= 0:
                ans[left] = nums[q[0]]

        return ans


# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (nums, k, expected)
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, 2, 12, 3, 7, 8, 1], 3, [12, 12, 12, 8, 8]),
    ]

    for nums, k, expected in tests:
        result = sol.maxSlidingWindow(nums, k)
        print(f"nums={nums}, k={k}")
        print(f"  result = {result}")
        print(f"  expected = {expected}")
        print(f"  {'✓ PASS' if result == expected else '✗ FAIL'}")
        print()
