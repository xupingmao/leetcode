class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0 for x in range(m+n)]

        i = 0
        j = 0
        k = 0

        # 多路合并算法
        len1 = len(nums1)
        len2 = len(nums2)

        while True:
            if i < m:
                v1 = nums1[i]
            else:
                v1 = None

            if j < n:
                v2 = nums2[j]
            else:
                v2 = None
            
            if v1 == None and v2 == None:
                break
            elif v1 == None or v2 < v1:
                result[k] = v2
                j += 1
            elif v2 == None or v1 < v2:
                result[k] = v1
                i += 1
            else:
                # 相等
                result[k] = v1
                result[k+1] = v2
                k += 1
                i += 1
                j += 1
            k += 1
        
        for i in range(m+n):
            nums1[i] = result[i]
    
s = Solution()
nums1 = [1,2,3,0,0,0]
s.merge(nums1, 3, [2,5,6], 3)
print(nums1)
