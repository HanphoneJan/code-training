#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    核心思想：原地哈希

    缺失的第一个正整数一定在 [1, n+1] 范围内（n 是数组长度）。
    因此可以把数组本身当作哈希表，将数值 i 放到下标 i-1 的位置。
    整理完成后，第一个 nums[i] != i+1 的位置，i+1 就是答案。

    时间复杂度：O(n)，虽然有嵌套循环，但每个数字最多被交换一次
    空间复杂度：O(1)，原地修改不需要额外空间
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 条件1：nums[i] 在有效范围 [1, size] 内，才有对应的目标位置 nums[i]-1
            # 条件2：nums[i] 还未放到正确位置（正确位置是下标 nums[i]-1 处存放 nums[i]）
            # 为什么用 while 而不是 if？
            # 交换后，新来到下标 i 的数字可能仍需要继续交换到它的正确位置
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # 注意：必须用辅助函数，不能直接写 nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                # 原因：Python 右侧表达式先计算，但 nums[i] 赋值后，nums[nums[i]-1] 的索引就变了
                self.__swap(nums, i, nums[i] - 1)
        # 遍历找第一个不满足"位置对应"的下标
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1  # i+1 就是缺失的最小正整数
        # 所有位置都满足 nums[i] == i+1，说明 1~size 全部存在，答案是 size+1
        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [1],
        [2],
        [1, 2, 3],
    ]

    for nums in tests:
        result = sol.firstMissingPositive(nums)
        print(f"firstMissingPositive({nums}) = {result}")
