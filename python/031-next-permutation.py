'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = len(nums)-1
        while p > 0:
            i = p-1
            while i >= 0:
                if nums[p] > nums[i]:
                    k = p
                    temp = nums[p]
                    while k > i:
                        nums[k] = nums[k-1]
                        k -= 1
                    nums[i] = temp
                    return
                i -= 1
            p -= 1
        nums.reverse()
        
def test(nums, expected):
    s = Solution()
    s.nextPermutation(nums)
    print(expected, nums)
    assert expected == nums
    
test([1,2,3], [1,3,2])
test([3,2,1], [1,2,3])
test([1,1,5], [1,5,1])
test([1,3,2], [2,1,3])
test([3,2,1,3,3,5,6,7,2], [3,2,1,3,3,5,7,2,6])