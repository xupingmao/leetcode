# encoding=utf-8
import xutils
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
        
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            raise Exception("nums length must bigger than 3")
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]
        last = closest
        length = len(nums)
        for a in range(length):
            v1 = nums[a]
            i = a + 1
            j = length - 1
            while i < j:
                v2 = nums[i]
                v3 = nums[j]
                last = v1+v2+v3
                if abs(last-target) < abs(closest-target):
                    closest = last
                if last < target:
                    i += 1
                if last > target:
                    j -= 1
                if last == target:
                    return target
        return closest
    
    def threeSumClosest_simple(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            raise Exception("nums length must bigger than 3")
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]
        length = len(nums)
        for a in range(length):
            v1 = nums[a]
            for b in range(a+1, length):
                v2 = nums[b]
                for c in range(b+1, length):
                    v3 = nums[c]
                    v = v1 + v2 + v3
                    if abs(v-target) < abs(closest - target):
                        closest = v
        return closest
                    
@xutils.timeit()
def test(nums, target, expected):
    s = Solution()
    v = s.threeSumClosest(nums, target)
    assert v == expected, 'nums=%s failed expect %s but see %s' % (nums, expected, v)
    
test([0,0,0], 1, 0)
test([0,1,2,3], 1, 3)
test([0,1,2,3,4], 1, 3)
test([-1,0,1,1,55],3,2)
test([0,5,-1,-2,4,-1,0,-3,4,-5],1,1)
test([1,2,4,8,16,32,64,128],82,82)
test([89,-17,-41,9,56,-8,40,38,98,-31,80,-1,-40,-73,28,55,15,89,-83,87,-42,-22,61,64,-94,-33,-38,25,-20,-80,37,99,-72,74,16,-25,-21,-73,-73,-72,65,-4,-72,46,60,7,-25,-14,-58,-50,14,-99,88,50,75,-59,94,-74,25,23,-10,-47,-1,-30,81,-66,54,-64,-1,68,-1,47,55,-59,5,64,45,83,-3,-38,-59,46,33,54,55,9,-13,50,-43,-48,57,97,-55,-13,-25,-9,-20,63,30,88,-4,74,19,-87,-32], -297, -280)
test([6,-34,70,-43,1,-74,56,-18,-47,44,43,-96,-81,-65,68,60,-9,59,-52,32,61,41,31,56,94,-53,-94,-35,38,55,20,-12,40,-41,-38,-10,10,16,-42,85,-38,4,-18,72,-39,95,-73,-55,-43,-70,0,46,97,-84,-67,-5,-37,68,15,-78,31,-80,-44,-48,-28,-100,-97,-4,6,-29,-21,-76,10,46,-49,80,27,-16,92,-90,-82,-13,-67,70,37,79,34,-48,-65,70,-15,60,6,45,41,16,56,67,-79,28,2,39,28,-80,-13,-72,-97,-37,-8,-100,-83,-37,-77,26,74,-36,-28,-78,-95,-81,39,-1,-50,4,87,-39,-52,6,-13,-16,-53,-95,94,2,-61,61,-1,-68,-33,-76,-41,54,57,-54,-24,-55,88,-58,53,0,76,-46,56,-95,17,-74,50,84,-19,-9,39,20,46,40,38,-46,-68,57,38,-44,-53,80], 0, 0)
test([-43,61,-62,24,73,64,-23,94,-65,-27,24,-56,8,54,0,19,-100,-64,-53,6,-22,13,-18,55,-41,37,34,-43,0,-8,-95,76,73,21,-93,16,98,60,70,-32,30,-7,-27,-73,79,-26,41,32,41,-5,82,-14,50,-94,22,62,60,-48,51,12,-34,68,-40,-20,-20,46,46,-79,1,82,-98,41,-79,-43,-76,-25,-94,-16,-25,46,-95,-79,53,-1,-30,43,93,17,72,66,83,-89,-16,42,40,87,-46,40,22,85,-91,46,-77,19,-56,-28,8,47,-20,65,8,60,-49,-86,-74,56,30,79,97,-89,14,-90,66,-12,-57,46,-61,87,72,13,75,75,36,79,-16,84,-49,-86,76,68,-8,-65,-86,-11,55,-69,-59,34,63,59,-11,43,16,7,93,57,-55,2,38,64,3,22,-9,-22,-34,-84,90,-71,-88,64,-19,13,-8,-81,-95,-38,-9,-25,82,57,60,-26,66,21,8,65,-38,-68,-59,24,91],-231,-231)


