#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    无重复字符的最长子串 - 滑动窗口

    核心思想：
    用滑动窗口维护一个不包含重复字符的子串，窗口右边界不断右移扩展，
    遇到重复字符时收缩左边界，保证窗口内无重复字符。

    为什么用哈希表？
    哈希表记录每个字符最后一次出现的位置，可以在 O(1) 时间内判断字符是否重复，
    并快速确定左边界应该移动到哪里。

    滑动窗口的关键：
    1. left：窗口左边界
    2. i：窗口右边界（当前遍历位置）
    3. hash_dict：记录字符最后一次出现的索引

    时间复杂度：O(n)，每个字符只访问一次
    空间复杂度：O(min(m,n))，m 是字符集大小
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}  # 记录字符最后一次出现的索引
        n = len(s)
        left, ans, result = 0, 0, 0  # left:左边界, ans:当前窗口长度, result:最大长度

        for i in range(0, n):
            if hash_dict.get(s[i], -1) == -1:
                # 字符未出现过，窗口直接扩展
                ans += 1
            else:
                # 字符出现过，需要收缩左边界
                # 注意：left 只能右移不能左移（取 max 保证）
                if left < hash_dict[s[i]]:
                    left = hash_dict[s[i]]
                ans = i - left  # 重新计算当前窗口长度

            hash_dict[s[i]] = i  # 更新字符位置
            result = max(ans, result)  # 更新最大长度

        return result


# ========== 示例推演：s = "abcabcbb" ==========
#
# i=0, 'a': hash_dict={}, left=0, ans=1, result=1, hash_dict={'a':0}
# i=1, 'b': hash_dict中没有b, ans=2, result=2, hash_dict={'a':0,'b':1}
# i=2, 'c': hash_dict中没有c, ans=3, result=3, hash_dict={'a':0,'b':1,'c':2}
# i=3, 'a': 'a'在hash_dict中，left=max(0,0)=0, left更新为1, ans=3-1=2
#       hash_dict={'a':3,'b':1,'c':2}, result=3
# i=4, 'b': 'b'在hash_dict中，left=max(1,1)=1, left更新为2, ans=4-2=2
# ...
# 最终结果：3
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
    ]

    for s, expected in tests:
        result = sol.lengthOfLongestSubstring(s)
        print(f"lengthOfLongestSubstring('{s}') = {result}, expected = {expected}")
