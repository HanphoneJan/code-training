#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    """
    283. 移动零 - 双指针解法

    核心思路：
    使用双指针将数组分为两部分：左边是非零元素，右边是零。

    解法一：两次遍历（当前实现）
    - 第一遍：统计零的个数
    - 第二遍：将所有非零元素移到前面
    - 第三遍：将剩余位置填充为零

    解法二：一次遍历（快慢指针）
    - 慢指针指向当前可以放置非零元素的位置
    - 快指针遍历数组，遇到非零元素就与慢指针交换

    为什么双指针有效？
    - 快指针负责"发现"非零元素
    - 慢指针负责"定位"放置位置
    - 两者之间的区域就是已经被处理过的零

    时间复杂度: O(n) - 遍历数组一次或两次
    空间复杂度: O(1) - 原地修改，只使用常数额外空间
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        两次遍历法：先将非零元素前移，再填充零
        不返回任何值，直接修改输入数组
        """
        n = len(nums)
        # 统计零的个数
        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1

        # 将所有非零元素移到数组前面
        left = 0  # 指向下一个可以放置非零元素的位置
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1

        # 将剩余位置填充为零
        for i in range(n - count, n):
            nums[i] = 0

    def moveZeroes_two_pointers(self, nums: List[int]) -> None:
        """
        快慢指针法：一次遍历完成
        - 慢指针：指向下一个非零元素应该放置的位置
        - 快指针：遍历数组寻找非零元素
        """
        slow = 0  # 慢指针：指向下一个非零元素的位置
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 交换快慢指针指向的元素
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (nums, expected)
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
    ]

    for nums, expected in tests:
        # 复制数组，因为会原地修改
        nums_copy = nums.copy()
        sol.moveZeroes(nums_copy)
        result = nums_copy
        print(f"nums={nums}")
        print(f"  result = {result}")
        print(f"  expected = {expected}")
        print(f"  {'✓ PASS' if result == expected else '✗ FAIL'}")
        print()
