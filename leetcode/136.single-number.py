#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30204
#
# [136] 只出现一次的数字
#


# @lcpr-template-start
from typing import List
from functools import reduce

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    136. 只出现一次的数字 - 位运算（异或）

    核心思想：
    利用异或运算（XOR）的三个性质：
    1. 任何数和 0 异或等于它本身：a ^ 0 = a
    2. 任何数和自己异或等于 0：a ^ a = 0
    3. 异或运算满足交换律和结合律

    因此，把所有数字异或起来：
    - 出现两次的数字会相互抵消（a ^ a = 0）
    - 最后剩下的就是只出现一次的数字

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:  # 遍历 nums 执行异或运算
            x ^= num
        return x  # 返回出现一次的数字 x

        # 也可以一行写法：
        # return reduce(lambda x, y: x ^ y, nums)


# @lc code=end


#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([0, 1, 0], 1),
        ([-1, -1, 3], 3),
    ]

    print("只出现一次的数字 - 测试开始")
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.singleNumber(nums)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: nums={nums} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
