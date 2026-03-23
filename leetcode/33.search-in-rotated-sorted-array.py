#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        核心思想：二分查找（处理旋转后的有序数组）

        旋转后的数组特点：[4,5,6,7,0,1,2]
        以任意 mid 为分界，左半段或右半段 必有一段是严格有序的。

        判断逻辑：
        1. 若 nums[left] <= nums[mid]：左半段 [left, mid] 有序
           - 若 target 在 [nums[left], nums[mid]) 范围内 → 在左半段搜索（right = mid-1）
           - 否则 → 在右半段搜索（left = mid+1）
        2. 若 nums[left] > nums[mid]：右半段 [mid, right] 有序
           - 若 target 在 (nums[mid], nums[right]] 范围内 → 在右半段搜索（left = mid+1）
           - 否则 → 在左半段搜索（right = mid-1）

        时间复杂度：O(log n)，本质上只是多了一步判断有序段，不影响复杂度
        """
        n = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left  # 防止整数溢出的写法
            if nums[mid] == target:
                return mid
            # 判断左半段 [left, mid] 是否有序
            if nums[left] <= nums[mid]:
                # 左半段有序：判断 target 是否落在左半段的范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target 在左半段，搜索范围缩小到左边
                else:
                    left = mid + 1   # target 不在左半段，去右边找
            else:
                # 左半段无序，则右半段 [mid, right] 一定有序
                # 判断 target 是否落在右半段的范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target 在右半段，搜索范围缩小到右边
                else:
                    right = mid - 1  # target 不在右半段，去左边找
        return -1
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
        ([5, 1, 3], 3, 2),
    ]

    for nums, target, expected in tests:
        result = sol.search(nums, target)
        print(f"search({nums}, {target}) = {result}, expected = {expected}")
