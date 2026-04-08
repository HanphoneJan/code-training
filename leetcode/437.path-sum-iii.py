#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from typing import Optional
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        def dfs(node:Optional[TreeNode],s:int) ->None:
            if not node:
                return
            s += node.val
            nonlocal ans
            ans += cnt[s-targetSum]
            cnt[s] += 1
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s] -=1
        dfs(root,0)
        return ans     

        
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

