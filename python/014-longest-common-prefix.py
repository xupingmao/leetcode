# encoding=utf-8

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) > 2:
            mid = int(len(strs) / 2)
            left = self.longestCommonPrefix(strs[:mid])
            right = self.longestCommonPrefix(strs[mid:])
        else:
            left = strs[0]
            right = strs[1]
        common = ''
        for i in range(min(len(left), len(right))):
            c1=left[i]
            c2=right[i]
            if c1==c2:
                common+=c1
            else:
                break
        return common
    
def check(expect, strs):
    s = Solution()
    r = s.longestCommonPrefix(strs)
    print(r, strs)
    assert expect == r
    
if __name__ == "__main__":
    check('abc', ['abc', 'abcd'])
    check('abc', ['abcd1', 'abce', 'abcd2'])
    
