#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start
from typing import List
from math import inf

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    152. 乘积最大子数组 - 动态规划

    核心思想：
    与 "最大子数组和" 不同，乘法遇到负数时，最小值可能变成最大值。
    因此需要同时维护两个状态：
    - f_max：以当前位置结尾的子数组的最大乘积
    - f_min：以当前位置结尾的子数组的最小乘积

    状态转移：
    对于当前元素 x，以 x 结尾的子数组乘积有三种可能：
    1. f_max * x（之前的最大乘积延续）
    2. f_min * x（之前的最小乘积 * 负数，可能反超）
    3. x 本身（重新开始）

    因此：
    f_max = max(f_max * x, f_min * x, x)
    f_min = min(f_max * x, f_min * x, x)
    ans = max(ans, f_max)

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf   # 注意答案可能是负数，初始化为负无穷
        f_max = 1    # 以当前位置结尾的最大乘积
        f_min = 1    # 以当前位置结尾的最小乘积

        for x in nums:
            # 同时更新 f_max 和 f_min
            # 注意：这里需要用临时变量保存上一轮的值，避免 f_max 被更新后影响 f_min
            f_max, f_min = max(f_max * x, f_min * x, x), \
                           min(f_max * x, f_min * x, x)
            ans = max(ans, f_max)

        return int(ans)


# @lc code=end


#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 3, -2, 4], 6),       # 2*3=6 或 2*3*(-2)*4 不是最大，最大是 6（或 -2 * 4 不是，那是 -8）
                                  # 实际上 2*3*(-2)*4=-48，但子数组 [2,3] 乘积=6
        ([-2, 0, -1], 0),         # 子数组 [0] 或 [-2,0]=0
        ([-2], -2),               # 只有一个负数
        ([-2, 3, -4], 24),        # 3*(-2)*(-4)=24
        ([0, 2], 2),              # [2]
        ([3, -1, 4], 4),          # [3,-1,4] = -12, 但 [4]=4 最大
    ]

    print("乘积最大子数组 - 测试开始")
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.maxProduct(nums)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: nums={nums} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
