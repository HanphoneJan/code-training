#
# @lc app=leetcode.cn id=957 lang=python3
# @lcpr version=30204
#
# [957] N 天后的牢房
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    N 天后的牢房 - 找循环周期

    问题描述：
    8 间牢房排成一排，每间牢房不是有人住就是空着。
    每天，根据牢房前一天的状态，所有牢房的状态都会发生变化。

    状态变化规则：
    - 如果一间牢房的两个相邻的房间都被占用或都是空的，则该牢房变为占用
    - 否则，该牢房变为空着

    注意：第一个和最后一个牢房没有两个相邻的房间，它们的状态永远为 0。

    给定初始状态数组 cells，返回 N 天后的状态。

    核心思路：
    由于牢房状态只有 8 间，且首尾固定为 0，实际只有 6 个位置会变化。
    6 个位置最多有 2^6 = 64 种状态，因此状态必然会出现循环。

    算法步骤：
    1. 模拟每一天的状态变化
    2. 用哈希表记录每个状态出现的天数
    3. 如果发现重复状态，说明找到了循环周期
    4. 利用循环周期跳过大量天数
    5. 继续模拟剩余的天数

    时间复杂度: O(min(N, 2^6) * 8) = O(1) - 状态数有限，最多模拟 64 个状态
    空间复杂度: O(2^6) = O(1) - 哈希表最多存储 64 个状态
    """
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(curr_cells: List[int]) -> List[int]:
            """
            计算下一天的牢房状态
            """
            next_cells = [0] * 8  # 首尾固定为 0
            for i in range(1, 7):  # 只有中间 6 间会变化
                # 如果两个相邻房间状态相同，则变为占用(1)
                # 否则变为空(0)
                next_cells[i] = 1 if curr_cells[i-1] == curr_cells[i+1] else 0
            return next_cells

        # 记录每个状态出现的天数
        seen = {}

        while n > 0:
            # 将当前状态转为元组（可哈希）
            state = tuple(cells)

            if state in seen:
                # 发现循环，计算循环周期
                cycle_length = seen[state] - n
                # 跳过完整的循环周期
                n %= cycle_length
                break

            # 记录当前状态和剩余天数
            seen[state] = n

            # 模拟下一天
            if n >= 1:
                n -= 1
                cells = next_day(cells)

        # 继续模拟剩余的天数
        while n > 0:
            cells = next_day(cells)
            n -= 1

        return cells


# 另一种写法：直接找规律，先找到循环周期
# class Solution:
#     def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
#         """
#         先找到所有状态，然后利用周期
#         """
#         def next_day(curr):
#             return [0] + [1 if curr[i-1] == curr[i+1] else 0 for i in range(1, 7)] + [0]
#
#         # 记录所有出现过的状态
#         history = [cells[:]]
#         seen = {tuple(cells): 0}
#
#         for day in range(1, n + 1):
#             cells = next_day(cells)
#             state = tuple(cells)
#
#             if state in seen:
#                 # 找到循环
#                 cycle_start = seen[state]
#                 cycle_len = day - cycle_start
#                 remaining = (n - cycle_start) % cycle_len
#                 return history[cycle_start + remaining]
#
#             seen[state] = day
#             history.append(cells[:])
#
#         return cells

# 暴力解法（N 很大时会超时）
# class Solution:
#     def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
#         """
#         暴力模拟每一天
#         时间复杂度: O(n * 8)
#         """
#         for _ in range(n):
#             new_cells = [0] * 8
#             for i in range(1, 7):
#                 new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
#             cells = new_cells
#         return cells

# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0,1]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,0]\n1000000000\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    cells1 = [0, 1, 0, 1, 1, 0, 0, 1]
    n1 = 7
    result1 = sol.prisonAfterNDays(cells1, n1)
    print(f"Test 1: cells={cells1}, n={n1}")
    print(f"Result: {result1}")
    expected1 = [0, 0, 1, 1, 0, 0, 0, 0]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    print("Passed!\n")

    # 测试用例 2：大 N 值，利用循环周期
    cells2 = [1, 0, 0, 1, 0, 0, 1, 0]
    n2 = 1000000000
    result2 = sol.prisonAfterNDays(cells2, n2)
    print(f"Test 2: cells={cells2}, n={n2}")
    print(f"Result: {result2}")
    expected2 = [0, 0, 1, 1, 1, 1, 1, 0]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    print("Passed!\n")

    # 测试用例 3：N = 1
    cells3 = [0, 0, 0, 0, 0, 0, 0, 0]
    n3 = 1
    result3 = sol.prisonAfterNDays(cells3, n3)
    print(f"Test 3: cells={cells3}, n={n3}")
    print(f"Result: {result3}")
    # 所有相邻都相同，中间都变为 1
    expected3 = [0, 1, 1, 1, 1, 1, 1, 0]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    print("Passed!\n")

    # 测试用例 4：N = 0
    cells4 = [1, 1, 1, 1, 1, 1, 1, 1]
    n4 = 0
    result4 = sol.prisonAfterNDays(cells4, n4)
    print(f"Test 4: cells={cells4}, n={n4}")
    print(f"Result: {result4}")
    assert result4 == cells4, f"Expected {cells4}, got {result4}"
    print("Passed!\n")

    # 测试用例 5：小 N 值多次验证
    cells5 = [0, 1, 0, 1, 0, 1, 0, 1]
    n5 = 1
    result5 = sol.prisonAfterNDays(cells5, n5)
    print(f"Test 5: cells={cells5}, n={n5}")
    print(f"Result: {result5}")
    # 计算下一天的状态
    # cells[1]: cells[0]==cells[2] -> 0==0 -> 1
    # cells[2]: cells[1]==cells[3] -> 1==1 -> 1
    # ...
    expected5 = [0, 1, 1, 1, 1, 1, 1, 0]
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    print("Passed!\n")

    print("All tests passed!")
