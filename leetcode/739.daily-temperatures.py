#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    每日温度 - 单调栈

    问题描述：
    给定一个整数数组 temperatures，表示每天的温度，
    返回一个数组 answer，其中 answer[i] 是指对于第 i 天，
    下一个更高温度出现在几天后。
    如果气温在这之后都不会升高，请在该位置用 0 来代替。

    核心思路：
    使用单调递减栈来维护还没有找到下一个更高温度的天数。

    单调栈的性质：
    - 栈中存储的是天数的下标
    - 栈中对应的温度是单调递减的
    - 栈顶元素是最近的一天，栈底是最早的一天

    算法步骤：
    1. 从右向左遍历温度数组（或从左向右）
    2. 对于当前温度，弹出栈中所有温度小于等于当前温度的元素
    3. 此时栈顶就是下一个更高温度的天数
    4. 将当前天数入栈

    两种遍历方式：
    - 从右向左：栈中保存的是「下一个更高温度的候选」
    - 从左向右：栈中保存的是「等待找到下一个更高温度的天数」

    时间复杂度: O(n) - 每个元素最多入栈出栈一次
    空间复杂度: O(n) - 栈的空间
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        从右向左遍历的写法
        """
        n = len(temperatures)
        ans = [0] * n  # 默认为 0，表示后面没有更高的温度
        st = []        # 单调递减栈，存储下标

        # 从右向左遍历
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            # 弹出栈中温度小于等于当前温度的元素
            # 这些元素不可能是左边元素的「下一个更高温度」
            while st and t >= temperatures[st[-1]]:
                st.pop()

            # 如果栈不为空，栈顶就是下一个更高温度的天数
            if st:
                ans[i] = st[-1] - i

            # 当前天数入栈
            st.append(i)

        return ans

    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """
    #     从左向右遍历的写法（更常见）
    #     """
    #     n = len(temperatures)
    #     ans = [0] * n
    #     st = []  # 单调递减栈，存储等待找到下一个更高温度的天数
    #
    #     for i, t in enumerate(temperatures):
    #         # 当前温度是栈中某些天的「下一个更高温度」
    #         while st and t > temperatures[st[-1]]:
    #             j = st.pop()
    #             ans[j] = i - j
    #         st.append(i)
    #
    #     return ans


# 暴力解法（会超时）
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         """
#         对于每一天，向后遍历找到第一个更高的温度
#         时间复杂度: O(n^2)
#         """
#         n = len(temperatures)
#         ans = [0] * n
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if temperatures[j] > temperatures[i]:
#                     ans[i] = j - i
#                     break
#         return ans

# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = sol.dailyTemperatures(temps1)
    print(f"Test 1: temperatures={temps1}")
    print(f"Result: {result1}")
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    print("Passed!\n")

    # 测试用例 2：递增序列
    temps2 = [30, 40, 50, 60]
    result2 = sol.dailyTemperatures(temps2)
    print(f"Test 2: temperatures={temps2}")
    print(f"Result: {result2}")
    expected2 = [1, 1, 1, 0]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    print("Passed!\n")

    # 测试用例 3：递减序列
    temps3 = [60, 50, 40, 30]
    result3 = sol.dailyTemperatures(temps3)
    print(f"Test 3: temperatures={temps3}")
    print(f"Result: {result3}")
    expected3 = [0, 0, 0, 0]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    print("Passed!\n")

    # 测试用例 4：相同温度
    temps4 = [30, 30, 30, 40]
    result4 = sol.dailyTemperatures(temps4)
    print(f"Test 4: temperatures={temps4}")
    print(f"Result: {result4}")
    expected4 = [3, 2, 1, 0]
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    print("Passed!\n")

    # 测试用例 5：单个元素
    temps5 = [30]
    result5 = sol.dailyTemperatures(temps5)
    print(f"Test 5: temperatures={temps5}")
    print(f"Result: {result5}")
    expected5 = [0]
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    print("Passed!\n")

    print("All tests passed!")
