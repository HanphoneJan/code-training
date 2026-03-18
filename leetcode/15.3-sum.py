#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
# 题目：找出所有和为0且不重复的三元组
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        核心思想：排序 + 双指针

        为什么排序？
        1. 去重更容易：相同数字会排在一起，方便跳过
        2. 双指针的前提：有序数组才能根据大小关系移动指针

        为什么固定一个数，剩下两个用双指针？
        三数之和为0 → nums[i] + nums[j] + nums[k] = 0
        固定 nums[i] 后，问题变成：在 i 之后的区间找两数之和等于 -nums[i]
        两数之和用双指针可以做到 O(n)，所以总体是 O(n²)
        """
        n = len(nums)

        # 边界情况：不足3个数，无法组成三元组
        if n < 3:
            return []

        # 排序是前提，让双指针和去重成为可能
        nums.sort()

        ans = list()

        # 外层循环：固定第一个数
        # 为什么复杂度是 O(n²)？
        # - 外层循环 n 次
        # - 内层双指针总共移动 n 次（third 从右往左，second 从左往右）
        # - 所以是 n × n = O(n²)
        for first in range(n):

            # ========== 第一个数的去重 ==========
            # 为什么要排除？
            # 如果 nums[first] == nums[first-1]，说明这个数在上一次循环已经用过了
            # 再用一次会产生重复的三元组
            # 例如：[-1, -1, 0, 1]，第一个 -1 已经找完了所有搭配
            # 第二个 -1 会找到完全一样的组合，所以跳过
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # 优化：如果最小的三个数之和都大于0，后面不可能有答案
            if nums[first] > 0:
                break

            # third 是右指针，从数组末尾开始向左移动
            # 注意：third 不会重置，它在上一个 second 循环中已经被移动到合适位置
            # 因为 second 向右移动，sum 会变大，所以 third 只能向左移动（或不动）
            third = n - 1

            # 目标：找到两数之和等于 target
            # 即 nums[second] + nums[third] = target
            target = -nums[first]

            # 内层循环：移动第二个数，配合双指针找第三个数
            for second in range(first + 1, n):

                # ========== 第二个数的去重 ==========
                # 为什么要排除？
                # 和第一个数的去重同理
                # 注意条件是 second > first + 1，确保是"连续重复"才跳过
                # 例如 first=0, nums=[-1, -1, 0, 1]
                # second=1 时，nums[1]==nums[0]，但这是第一次，不跳过
                # second=2 时，如果 nums[2]==nums[1]，才跳过
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # 双指针核心逻辑：
                # 如果当前和太大，说明 third 太大了，需要左移
                # 注意 third 要始终大于 second，不能重合
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                # second 和 third 重合了，说明没有合适的 third 了
                # 因为 third 在 second 右边，重合意味着没有可选的第三个数
                if second == third:
                    break

                # 找到满足条件的三元组
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# ========== 示例推演：nums = [-1, 0, 1, 2, -1, -4] ==========
#
# 排序后：[-4, -1, -1, 0, 1, 2]
#
# first = 0, nums[0] = -4:
#   target = 4
#   second=1, third=5: nums[1]+nums[5]=-1+2=1 < 4，不进入while
#   -1+2=1 ≠ 4，不记录
#   second=2: 去重跳过（nums[2]==nums[1]）
#   second=3: 0+2=2 < 4
#   ... 找不到答案
#
# first = 1, nums[1] = -1:
#   target = 1
#   second=2, third=5: nums[2]+nums[5]=-1+2=1 == target！
#   记录 [-1, -1, 2]
#   second=3: 进入while，0+2=2>1，third减到4
#   0+1=1 == target！记录 [-1, 0, 1]
#
# first = 2, nums[2] = -1:
#   去重跳过（和 first=1 的值相同）
#
# first = 3, nums[3] = 0:
#   target = 0
#   second=4, third=4: second==third，break，没有答案
#
# 最终结果：[[-1, -1, 2], [-1, 0, 1]]
# @lc code=end


# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#