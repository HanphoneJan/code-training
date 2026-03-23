#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
# 题目：找出字符串中最长的回文子串（正读反读都相同的连续子串）
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        核心思想：中心扩展法

        回文串的特点：
        - 奇数长度回文串：以某个字符为中心，向两边对称展开（如 "aba"）
        - 偶数长度回文串：以两个字符之间的空隙为中心（如 "abba"）

        为什么中心扩展是 O(n²)？
        - 中心点有 2n-1 个（n 个字符 + n-1 个间隙）
        - 每次向两边扩展最多 O(n)
        - 总体是 O(n²)

        为什么不用动态规划？
        可以，但中心扩展更直观，且空间复杂度 O(1) 优于 DP 的 O(n²)
        """
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            """
            从中心向两边扩展，找到最长的回文边界

            参数：
            - left, right：初始中心位置的左右指针
              奇数长度：left == right（如 "aba" 从中间的 'b' 开始）
              偶数长度：right = left + 1（如 "abba" 从中间的 "bb" 之间开始）

            返回：
            - (start, end)：回文子串的起始和结束索引（包含）
            """
            # 向两边扩展：条件是边界内且两边字符相等
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1      # 左指针左移
                right += 1     # 右指针右移

            # 循环结束时，left 和 right 指向的是不满足条件的位置
            # 所以回文边界是 left+1 到 right-1
            return left + 1, right - 1

        # 记录最长回文子串的边界
        start, end = 0, 0

        # 遍历每个可能的中心点
        for i in range(len(s)):
            # ========== 奇数长度回文串 ==========
            # 中心是 s[i] 本身
            # 例如 "aba"，i=1，从 'b' 开始向两边扩展
            l1, r1 = expandAroundCenter(i, i)

            # ========== 偶数长度回文串 ==========
            # 中心是 s[i] 和 s[i+1] 之间
            # 例如 "abba"，i=1，从第一个 'b' 和第二个 'b' 之间开始扩展
            l2, r2 = expandAroundCenter(i, i + 1)

            # 更新最长回文子串
            # 情况1：奇数长度回文串更长
            if r1 - l1 > end - start:
                start, end = l1, r1

            # 情况2：偶数长度回文串更长
            if r2 - l2 > end - start:
                start, end = l2, r2

        # 返回最长回文子串（end+1 是因为切片不包含结束位置）
        return s[start:end + 1]


# ========== 示例推演：s = "babad" ==========
#
# i = 0, s[0] = 'b'：
#   奇数：expand(0,0) -> left=-1, right=1，返回 (0,0)，长度1
#   偶数：expand(0,1) -> s[0]='b', s[1]='a' 不等，返回 (0,0)，长度1
#   最长："b"（索引 0-0）
#
# i = 1, s[1] = 'a'：
#   奇数：expand(1,1) -> 先匹配 'a'，然后 s[0]='b', s[2]='b' 匹配
#         然后 s[-1] 越界，返回 (0,2)，长度3
#   偶数：expand(1,2) -> s[1]='a', s[2]='b' 不等，返回 (1,1)，长度1
#   最长："bab"（索引 0-2）
#
# i = 2, s[2] = 'b'：
#   奇数：expand(2,2) -> 匹配 'b'，s[1]='a', s[3]='a' 匹配
#         s[0]='b', s[4]='d' 不等，返回 (1,3)，长度3
#   偶数：expand(2,3) -> s[2]='b', s[3]='a' 不等，返回 (2,2)，长度1
#   最长不变："bab"
#
# i = 3, s[3] = 'a'：
#   奇数：expand(3,3) -> 匹配 'a'，s[2]='b', s[4]='d' 不等，返回 (3,3)，长度1
#   偶数：expand(3,4) -> s[3]='a', s[4]='d' 不等，返回 (3,3)，长度1
#
# i = 4, s[4] = 'd'：
#   类似分析，最长不变
#
# 最终结果："bab"
# 注意："aba" 也是正确答案，取决于遍历顺序中先遇到哪个
# @lc code=end


# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "abacaba",
    ]

    for s in tests:
        result = sol.longestPalindrome(s)
        print(f"longestPalindrome('{s}') = '{result}'")
