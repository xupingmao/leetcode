# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/08/29 13:02:42
# @modified 2020/08/29 13:04:00

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        # 深度优先遍历
        def calc_depth(node):
            if node is None:
                return 0
            left = calc_depth(node.left)
            right = calc_depth(node.right)
            return 1 + min(left, right)
        
        return calc_depth(root)


