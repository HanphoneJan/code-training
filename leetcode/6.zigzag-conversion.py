#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
# 题目：将字符串按照指定行数进行Z字形排列，然后按行读取
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        核心思想：模拟Z字形行走过程

        Z字形排列的特点：
        - 第一行：从上到下到达底部
        - 然后斜向上到达第一行
        - 然后再次向下到达底部
        - 如此反复...

        为什么用 flag 控制方向？
        我们不需要真的按Z字形存储，只需要知道每个字符应该放到哪一行。
        用一个 index 表示当前行，flag 表示移动方向（+1 向下，-1 向上）。

        时间复杂度：O(n)，每个字符只访问一次
        空间复杂度：O(n)，存储所有字符
        """
        # 特殊情况：只有1行，Z字形就是原字符串
        if numRows == 1:
            return s

        # 初始化 numRows 个空字符串，分别存储每一行的字符
        # 常用技巧：[''] * numRows 快速创建列表
        rows = [''] * numRows

        # index：当前所在的行号（0 到 numRows-1）
        index = 0

        # flag：移动方向，1 表示向下，-1 表示向上
        # 巧妙之处：用 +1/-1 可以直接加到 index 上，不用写 if-else
        flag = 1

        for i in range(len(s)):
            # 将当前字符放到对应的行
            rows[index] += s[i]

            # 到达第一行，改为向下移动
            if index == 0:
                flag = 1
            # 到达最后一行，改为向上移动
            elif index == numRows - 1:
                flag = -1

            # 根据 flag 更新行号
            # flag = 1 时，index 增加（向下）
            # flag = -1 时，index 减少（向上）
            index += flag

        # 将所有行的字符拼接起来
        return ''.join(rows)


# ========== 示例推演：s = "PAYPALISHIRING", numRows = 3 ==========
#
# Z字形排列应该是：
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 行走过程模拟：
# i=0, 'P': index=0, rows[0]="P",     到底部？否，flag=1, index变为1
# i=1, 'A': index=1, rows[1]="A",     到底部？否，flag=1, index变为2
# i=2, 'Y': index=2, rows[2]="Y",     到底部？是，flag=-1, index变为1
# i=3, 'P': index=1, rows[1]="AP",    到顶部？否，flag=-1, index变为0
# i=4, 'A': index=0, rows[0]="PA",    到顶部？是，flag=1, index变为1
# i=5, 'L': index=1, rows[1]="APL",   ...
# ...
#
# 最终：
# rows[0] = "PAHN"
# rows[1] = "APLSIIG"
# rows[2] = "YIR"
#
# 结果："PAHNAPLSIIGYIR"
# @lc code=end


# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#
