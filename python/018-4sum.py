# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2018/02/15 11:01:59
# @modified 2018/02/15 17:48:22

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

import xutils
import sys

class Solution:

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        results = []
        duplicate = set()
        last = None
        for a in range(length):
            v1 = nums[a]
            for b in range(a + 1, length):
                v2 = nums[b]
                i = b + 1
                j = length - 1
                while i < j:
                    v3 = nums[i]
                    v4 = nums[j]
                    value = v1 + v2 + v3 + v4
                    if value < target:
                        i += 1
                    if value > target:
                        j -= 1
                    if value == target:
                        cur = (v1,v2,v3,v4)
                        if cur not in duplicate:
                            duplicate.add(cur)
                            results.append([v1,v2,v3,v4])
                        i += 1
        return results

def test(nums, target, expected):
    s = Solution()
    v = s.fourSum(nums, target)
    print('got', sorted(nums), v)
    assert sorted(v) == sorted(expected), "failed"


test([1, 0, -1, 0, -2, 2], 0, [
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
])
test([-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
test([-5,-4,-3,-2,-1,0,0,1,2,3,4,5], 0, [[-5,-4,4,5],[-5,-3,3,5],[-5,-2,2,5],[-5,-2,3,4],[-5,-1,1,5],[-5,-1,2,4],[-5,0,0,5],[-5,0,1,4],[-5,0,2,3],[-4,-3,2,5],[-4,-3,3,4],[-4,-2,1,5],[-4,-2,2,4],[-4,-1,0,5],[-4,-1,1,4],[-4,-1,2,3],[-4,0,0,4],[-4,0,1,3],[-3,-2,0,5],[-3,-2,1,4],[-3,-2,2,3],[-3,-1,0,4],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

        