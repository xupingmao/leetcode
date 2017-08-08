"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = []
        solutions_set = set()
        nums_set = set(nums)
        length = len(nums)
        mid = int(length/2)
        nums = sorted(nums)
        # [0,mid)
        for i in range(length-2):
            # (mid+1,length-1]
            if nums[i]>0:
                break
            for j in range(i+1, length-1):
                expect = - (nums[i] + nums[j])
                if expect in nums_set and expect >= nums[j+1]:
                    n1 = nums[i]
                    n2 = nums[j]
                    n3 = expect
                    key = '%s|%s|%s' % (n1,n2,n3)
                    if key not in solutions_set:
                        solutions.append([n1,n2,n3])
                        solutions_set.add(key)
                if expect <= nums[j]:
                    break
        # return solutions
        return sorted(solutions)
        
