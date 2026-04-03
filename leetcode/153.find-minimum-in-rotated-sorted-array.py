#
# @lc app=leetcode.cn id=153 lang=python3
# @lcpr version=30204
#
# [153] 寻找旋转排序数组中的最小值
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    153. 寻找旋转排序数组中的最小值 - 二分查找

    核心思想：
    数组原本是升序的，但被旋转了（把前面一部分移到后面）。
    旋转后有一个特性：最小值右边全是大于它的，最小值左边也全是大于它的（除了它自己）。

    二分策略：
    取中间元素 nums[mid]，和右边界 nums[right] 比较：
    - 如果 nums[mid] > nums[right]：说明最小值一定在 mid 右侧，left = mid + 1
    - 如果 nums[mid] < nums[right]：说明最小值在 mid 左侧（包括 mid），right = mid
    - 如果相等：无法判断，right -= 1（本题元素互不相同，不会出现相等）

    为什么要和 right 比较而不是 left？
    因为数组旋转后，右半边一定是有序的或包含最小值的，和 right 比较能更快缩小范围。
    另外，如果使用 left < right 的循环条件，最终 left == right 就是答案，不会出现死循环。

    时间复杂度：O(log n)
    空间复杂度：O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 最小值在 mid 右侧
                left = mid + 1
            else:
                # nums[mid] < nums[right]，最小值在 mid 左侧（包括 mid）
                # 这里不可能等于，因为题目保证元素互不相同
                right = mid

        return nums[left]


# @lc code=end


#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),   # 未旋转
        ([2, 1], 1),              # 两个元素
        ([1], 1),                 # 单个元素
    ]

    print("寻找旋转排序数组中的最小值 - 测试开始")
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.findMin(nums)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: nums={nums} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
