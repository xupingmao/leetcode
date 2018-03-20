class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        uniq = i = 1
        length = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                nums[uniq] = nums[i]
                uniq += 1
                length += 1
            i += 1
        return length
            