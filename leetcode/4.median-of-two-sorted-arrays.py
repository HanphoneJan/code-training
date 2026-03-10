#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:

            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
        
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]

            nums1_right = float('inf') if i == m else nums1[i]

            nums2_left = float('-inf') if j == 0 else nums2[j - 1]

            nums2_right = float('inf') if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                if (m + n) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

