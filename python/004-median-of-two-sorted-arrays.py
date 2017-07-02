# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/03/21
# 

"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):

    def findMedian(self, sortedArray):
        length = len(sortedArray)
        if length % 2 == 0:
            # 4 -> 1,2
            # 6 -> 2,3
            median = int(length / 2)
            # for python 2
            return median-1, float(sortedArray[median-1] + sortedArray[median]) / 2
        else:
            # 3 -> 1
            # 5 -> 2
            median = int(length / 2)
            return median, sortedArray[median]

    def findMedianSimple(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        half1, medianValue = self.findMedian(nums)
        return medianValue

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 使用二分法

        if len(nums1) == 0:
            return self.findMedian(nums2)[1]
        elif len(nums2) == 0:
            return self.findMedian(nums1)[1]

        if len(nums1) <= 2 or len(nums2) <= 2:
            return self.findMedianSimple(nums1, nums2)
        else:
            half1, value1 = self.findMedian(nums1)
            half2, value2 = self.findMedian(nums2)
            cut = min(half1, half2)
            if value1 == value2:
                return value1
            elif value1 > value2:
                # num1的左边, num2的右边
                # 左包含右不包含
                return self.findMedianSortedArrays(nums1[:len(nums1) - cut], nums2[cut:])
            else:
                return self.findMedianSortedArrays(nums1[cut:], nums2[:len(nums2) - cut])

def testCase(nums1, nums2, expected):
    solution = Solution()
    actual = solution.findMedianSortedArrays(nums1, nums2)
    assert actual == expected, "expected %s but get %s" % (expected, actual)

def _test():
    """
        >>> _test()
        'OK'
    """
    testCase([1,3], [2], 2)
    testCase([1,2], [3,4], 2.5)
    testCase([1,2,3,4,5,6], [1], 3)
    testCase([1,2,3,4,5,6,7,8], [8,9,10,11,12,13], 7.5)
    return "OK"