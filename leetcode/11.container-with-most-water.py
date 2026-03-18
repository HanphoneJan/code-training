#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
# 题目：给定 n 个非负整数表示高度，找出两条线使它们与 x 轴构成的容器能盛最多的水
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        核心思想：双指针法

        容器盛水量的计算：
        面积 = 宽度 × 高度 = (right - left) × min(height[left], height[right])
        宽度是两条线之间的距离，高度由较短的线决定（木桶原理）

        为什么移动较短的指针？
        假设 height[left] < height[right]，当前面积为 S = (right-left) × height[left]
        - 如果移动 right 指针：宽度减小，高度最多还是 height[left]，面积必然减小
        - 如果移动 left 指针：宽度减小，但可能遇到更高的线，面积可能增大
        因此，移动较短的指针才有可能找到更大的面积。

        时间复杂度：O(n)，每个指针最多移动 n 次
        空间复杂度：O(1)，只使用常数额外空间
        """
        # 左指针从数组开头
        left = 0
        # 右指针从数组末尾
        right = len(height) - 1

        # 记录最大面积
        max_area = 0

        # 当两个指针相遇时停止
        while left < right:
            # 计算当前容器的宽度
            width = right - left

            # 高度由较短的线决定（木桶原理）
            current_height = min(height[left], height[right])

            # 计算当前面积
            current_area = width * current_height

            # 更新最大面积
            max_area = max(max_area, current_area)

            # 移动较短的指针，寻找可能更大的面积
            if height[left] < height[right]:
                left += 1  # 左指针右移
            else:
                right -= 1  # 右指针左移

        return max_area


# ========== 示例推演：height = [1,8,6,2,5,4,8,3,7] ==========
#
# 初始：left=0, right=8, max_area=0
#
# 第1轮：width=8, height=min(1,7)=1, area=8
#       height[0]=1 < height[8]=7，left++，left=1
#
# 第2轮：width=7, height=min(8,7)=7, area=49
#       max_area=49
#       height[1]=8 > height[8]=7，right--，right=7
#
# 第3轮：width=6, height=min(8,3)=3, area=18
#       height[1]=8 > height[7]=3，right--，right=6
#
# 第4轮：width=5, height=min(8,8)=8, area=40
#       height[1]=8 == height[6]=8，可以移动任意一个，假设移动right
#
# ... 继续直到 left >= right
#
# 最终结果：49
# @lc code=end


# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
