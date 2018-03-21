class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = j = 0
        removed = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == val:
                removed += 1
            else:
                length += 1
                if i != j:
                    nums[j] = nums[i]
                j += 1
        return length
        