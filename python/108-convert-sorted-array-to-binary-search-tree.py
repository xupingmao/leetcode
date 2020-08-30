# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/08/23 13:45:51
# @modified 2020/08/23 13:58:48

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from run_test import *

class Solution:

    @solution_func
    def sortedArrayToBST(self, nums):
        # 1,2,3 -> 2,1,3
        # 1,2,3,4,5,6 -> 3,2,5,1,null,4,6
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        
        if len(nums) == 0:
            return []
        
        def convert(left, right):
            if left > right:
                return
            if left == right:
                return TreeNode(nums[left])
            if left + 1 == right:
                node = TreeNode(nums[right])
                node.left = TreeNode(nums[left])
                return node
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid-1)
            node.right = convert(mid+1, right)
            return node

        # 把数组转为二叉树
        root = convert(0, len(nums)-1)
        # 把二叉树转成数组
        result = []
        q = [root]
        while len(q) > 0:
            q2 = []
            for node in q:
                if node is None:
                    result.append(None)
                else:
                    result.append(node.val)
                    q2.append(node.left)
                    q2.append(node.right)
            q = q2
        
        # 去除最后的None
        while result[-1] == None:
            result.pop()
        return result

run_test([[]], [])
run_test([[-10,-3,0,5,9]], [0, -3, 9, -10, None, 5])
run_test([[1]], [1])
