#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
# 题目：给定两个正序数组，找出它们的中位数，要求时间复杂度 O(log(m+n))
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        核心思想：二分查找（在较短的数组上进行二分）

        为什么用二分？
        题目要求 O(log(m+n))，暗示我们要用二分而不是 O(m+n) 的合并方法。

        核心思路：
        中位数的本质是将数组分成左右两部分，使得左边部分的元素个数等于右边部分（或相差1），
        且左边所有元素 <= 右边所有元素。

        对于两个数组，我们需要找到一个切割点 i（在 nums1 中）和 j（在 nums2 中），使得：
        - 左边部分：nums1[0..i-1] + nums2[0..j-1]
        - 右边部分：nums1[i..m-1] + nums2[j..n-1]
        - 左边元素个数 = 右边元素个数（或左边多一个）
        - 左边最大值 <= 右边最小值

        切割点的关系：i + j = (m + n + 1) // 2
        """
        # 确保 nums1 是较短的数组，减少二分查找的范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # 在 nums1 的 [0, m] 范围内二分查找合适的切割点 i
        # i 表示 nums1 中前 i 个元素被分到左边部分
        left, right = 0, m

        while left <= right:
            # i：nums1 的切割位置（表示 nums1[0:i] 在左边）
            i = (left + right) // 2

            # j：nums2 的切割位置，由总数决定
            # 要求：i + j = (m + n + 1) // 2（左边比右边多一个或相等）
            j = (m + n + 1) // 2 - i

            # 计算切割后的四个边界值
            # nums1_left：nums1 左边最后一个元素（切割位置的前一个）
            # 如果 i == 0，说明 nums1 所有元素都在右边，左边没有元素，用 -inf 表示
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]

            # nums1_right：nums1 右边第一个元素（切割位置的元素）
            # 如果 i == m，说明 nums1 所有元素都在左边，右边没有元素，用 +inf 表示
            nums1_right = float('inf') if i == m else nums1[i]

            # 同理计算 nums2 的边界
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]

            # 检查切割是否正确：左边最大值 <= 右边最小值
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 找到正确的切割点！

                # 判断总长度是奇数还是偶数
                if (m + n) % 2 == 0:
                    # 偶数：中位数是左边最大值和右边最小值的平均
                    # 左边最大值 = max(nums1_left, nums2_left)
                    # 右边最小值 = min(nums1_right, nums2_right)
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    # 奇数：中位数是左边最大值（因为左边比右边多一个元素）
                    return max(nums1_left, nums2_left)

            elif nums1_left > nums2_right:
                # nums1 的左边太大了，需要向左移动切割点
                # 让 nums1 贡献更少的元素到左边
                right = i - 1
            else:
                # nums2 的左边太大了（即 nums1_left < nums2_left 且 nums1_left < nums2_right）
                # 需要向右移动切割点，让 nums1 贡献更多元素到左边
                left = i + 1


# ========== 示例推演：nums1 = [1, 3], nums2 = [2] ==========
#
# 确保 nums1 较短：m=2, n=1，交换后 nums1=[2], nums2=[1,3]，m=1, n=2
#
# 第一次循环：left=0, right=1, i=0, j=(3+1)//2-0=2
#   nums1_left=-inf, nums1_right=2
#   nums2_left=3, nums2_right=+inf（j=2 超出 nums2 范围）
#   -inf <= +inf ✓，但 3 <= 2？不满足，进入 else 分支
#   left = 1
#
# 第二次循环：left=1, right=1, i=1, j=2-1=1
#   nums1_left=2, nums1_right=+inf
#   nums2_left=1, nums2_right=3
#   2 <= 3 ✓，1 <= +inf ✓，找到正确切割点！
#
# 总长度 3 是奇数，返回 max(2, 1) = 2
# @lc code=end


# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0], [0], 0.0),
        ([], [1], 1.0),
        ([1, 3, 5], [2, 4, 6], 3.5),
    ]

    for nums1, nums2, expected in tests:
        result = sol.findMedianSortedArrays(nums1, nums2)
        print(f"findMedianSortedArrays({nums1}, {nums2}) = {result}, expected = {expected}")
