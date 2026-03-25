#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    字母异位词分组 - 哈希表

    核心思想：
    字母异位词（anagram）的特点是：排序后的字符串相同。
    例如 "eat", "tea", "ate" 排序后都是 "aet"。

    算法步骤：
    1. 遍历每个字符串，将其排序作为 key
    2. 将原字符串加入 key 对应的列表
    3. 返回所有列表

    为什么用排序作为 key？
    因为异位词的字母组成完全相同，排序后必然相同。

    时间复杂度：O(n * k log k)，n 是字符串数量，k 是最大字符串长度
    空间复杂度：O(n * k)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))  # 排序作为 key
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())


# ========== 示例推演：strs = ["eat","tea","tan","ate","nat","bat"] ==========
#
# "eat" 排序后 "aet"，anagrams = {"aet": ["eat"]}
# "tea" 排序后 "aet"，anagrams = {"aet": ["eat", "tea"]}
# "tan" 排序后 "ant"，anagrams = {"aet": ["eat", "tea"], "ant": ["tan"]}
# "ate" 排序后 "aet"，anagrams = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
# "nat" 排序后 "ant"，anagrams = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
# "bat" 排序后 "abt"，anagrams = {"aet": [...], "ant": [...], "abt": ["bat"]}
#
# 结果：[["eat","tea","ate"], ["tan","nat"], ["bat"]]
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for strs, expected in tests:
        result = sol.groupAnagrams(strs)
        print(f"groupAnagrams({strs}) = {result}")
