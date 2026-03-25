#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    颜色分类 - 荷兰国旗问题

    核心思想：
    数组中只有 0, 1, 2 三个值，需要原地排序。
    这是经典的"荷兰国旗问题"。

    三指针法（最优）：
    - p0：指向0应该放置的位置（从数组开头）
    - p2：指向2应该放置的位置（从数组末尾）
    - i：当前遍历位置

    遍历策略：
    - nums[i] == 0：与 p0 位置交换，p0++，i++
    - nums[i] == 1：i++
    - nums[i] == 2：与 p2 位置交换，p2--（i 不递增，因为交换过来的元素需要再判断）

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2 = 0, n - 1  # p0指向0该放的位置，p2指向2该放的位置
        i = 0

        while i <= p2:
            if nums[i] == 0:
                # 0 放到 p0 位置
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                # 1 不动
                i += 1
            else:  # nums[i] == 2
                # 2 放到 p2 位置
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # i 不递增，因为交换过来的元素需要再判断


# ========== 示例推演：nums = [2,0,2,1,1,0] ==========
#
# 初始：p0=0, p2=5, i=0
# nums = [2, 0, 2, 1, 1, 0]
#
# i=0, nums[0]=2: 与 nums[5]交换，p2=4
#   nums = [0, 0, 2, 1, 1, 2]
#
# i=0, nums[0]=0: 与 nums[0]交换，p0=1, i=1
#   nums = [0, 0, 2, 1, 1, 2]
#
# i=1, nums[1]=0: 与 nums[1]交换，p0=2, i=2
#   nums = [0, 0, 2, 1, 1, 2]
#
# i=2, nums[2]=2: 与 nums[4]交换，p2=3
#   nums = [0, 0, 1, 1, 2, 2]
#
# i=2, nums[2]=1: i=3
#
# i=3, nums[3]=1: i=4
#
# i=4 > p2=3，结束
# 结果：[0, 0, 1, 1, 2, 2]
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
        [2, 1, 0],
    ]

    for nums in tests:
        nums_copy = nums.copy()
        sol.sortColors(nums_copy)
        print(f"sortColors({nums}) = {nums_copy}")
