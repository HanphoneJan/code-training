#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 相向双指针经典例题
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        核心思想：相向双指针（空间优化版）

        每个位置能接的雨水量 = min(左边最高柱, 右边最高柱) - 当前柱高度

        双指针策略：
        - pre_max：左指针左侧（含当前位置）的最大高度
        - suf_max：右指针右侧（含当前位置）的最大高度，suf是suffix（后缀）
        - 若 pre_max < suf_max：
            左指针处的积水由 pre_max 决定（右边至少有 suf_max 这么高作为右边界）
            积水量 = pre_max - height[left]，左指针右移
        - 若 pre_max >= suf_max：
            右指针处的积水由 suf_max 决定（左边至少有 pre_max 这么高作为左边界）
            积水量 = suf_max - height[right]，右指针左移

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        ans = pre_max = suf_max = 0  # ans：总积水量，pre_max：左最大，suf_max：右最大
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])   # 更新左侧最大高度
            suf_max = max(suf_max, height[right])  # 更新右侧最大高度
            if pre_max < suf_max:
                # 左侧较矮，当前位置积水由 pre_max 决定
                ans += pre_max - height[left]
                left += 1   # 左指针右移
            else:
                # 右侧较矮（或相等），当前位置积水由 suf_max 决定
                ans += suf_max - height[right]
                right -= 1  # 右指针左移
        return ans
            
                
            


# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

