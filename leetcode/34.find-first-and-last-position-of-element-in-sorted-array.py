#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    在排序数组中查找元素的第一个和最后一个位置 - 二分查找

    核心思想：
    排序数组中找 target 的范围，等价于找 target 的左边界和右边界。
    用两次二分查找分别定位左边界和右边界。

    找左边界的技巧：
    当 nums[mid] == target 时，不立即返回，而是收缩右边界（right = mid），
    继续向左查找，看是否还有更小的索引也是 target。

    找右边界的技巧：
    当 nums[mid] == target 时，收缩左边界（left = mid + 1），
    继续向右查找，看是否还有更大的索引也是 target。

    时间复杂度：O(log n)，两次二分查找
    空间复杂度：O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result_left, result_right = -1, -1

        # 第一次二分：找左边界
        left, right = 0, n  # 左闭右开区间
        while left < right:  # 不使用 <=：左闭右开写法更统一，循环结束时 left 指向第一个 >= target 的位置
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result_left = mid   # 记录当前位置
                right = mid         # 继续向左查找
            elif nums[mid] < target:
                left = mid + 1      # 目标在右半区
            else:
                right = mid         # 目标在左半区

        # 第二次二分：找右边界
        left, right = 0, n
        while left < right:  # 不使用 <=：左闭右开写法更统一
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result_right = mid  # 记录当前位置
                left = mid + 1      # 继续向右查找
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return [result_left, result_right]


# ========== 示例推演：nums = [5,7,7,8,8,10], target = 8 ==========
#
# 找左边界：
#   left=0, right=6, mid=3, nums[3]=8 == 8, result_left=3, right=3
#   left=0, right=3, mid=1, nums[1]=7 < 8, left=2
#   left=2, right=3, mid=2, nums[2]=7 < 8, left=3
#   left=3 == right=3，结束，result_left=3
#
# 找右边界：
#   left=0, right=6, mid=3, nums[3]=8 == 8, result_right=3, left=4
#   left=4, right=6, mid=5, nums[5]=10 > 8, right=5
#   left=4, right=5, mid=4, nums[4]=8 == 8, result_right=4, left=5
#   left=5 == right=5，结束，result_right=4
#
# 结果：[3, 4]
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 2, [0, 1]),
    ]

    for nums, target, expected in tests:
        result = sol.searchRange(nums, target)
        print(f"searchRange({nums}, {target}) = {result}, expected = {expected}")
