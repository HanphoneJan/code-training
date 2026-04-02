#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30204
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    搜索插入位置 - 二分查找

    核心思想：
    在有序数组中找 target 的插入位置，使得插入后数组仍然有序。
    这等价于找第一个大于等于 target 的元素位置。

    二分查找的变体：
    - 如果找到 target，返回其索引
    - 如果没找到，循环结束时 left == right，即为应该插入的位置

    为什么返回 left？
    循环不变式：nums[0..left-1] < target，nums[right..n-1] >= target
    当循环结束时，left == right，left 就是插入位置

    时间复杂度：O(log n)
    空间复杂度：O(1)
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n  # 右边界设为 n，左闭右开区间

        while left < right:  # 不使用 <=：左闭右开写法更统一，循环结束时 left == right 即为答案
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid       # 收缩右边界到 mid
            else:
                left = mid + 1    # target 在右半区

        return left


# ========== 示例推演：nums = [1,3,5,6], target = 2 ==========
#
# left=0, right=4, mid=2, nums[2]=5 >= 2, right=2
# left=0, right=2, mid=1, nums[1]=3 >= 2, right=1
# left=0, right=1, mid=0, nums[0]=1 < 2, left=1
# left=1 == right=1，循环结束
#
# 返回 left=1，即 2 应该插入到索引 1 的位置
# 结果数组：[1,2,3,5,6]
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ]

    for nums, target, expected in tests:
        result = sol.searchInsert(nums, target)
        print(f"searchInsert({nums}, {target}) = {result}, expected = {expected}")
