# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/03/21
# 

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

"""

def isPalindrome(str):
    """
    >>> isPalindrome("abc")
    False
    >>> isPalindrome("aba")
    True
    >>> isPalindrome('a')
    True
    >>> isPalindrome('bb')
    True
    >>> isPalindrome('')
    True
    """
    if str == "":
        return True
    mid = int(len(str) / 2)
    length = len(str)
    for i in range(mid+1):
        if str[i] != str[length-i-1]:
            return False
    return True

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        hit = ""
        for start in range(len(s)+1):
            # 比hit短的就不用试了
            for i in range(start + len(hit),len(s)+1):
                sub = s[start:i]
                # LeetCode答案是取后匹配上的
                # if isPalindrome(sub) and len(sub) >= len(hit):
                if isPalindrome(sub):
                    hit = sub
        return hit


def testCase(s, expected):
    sol = Solution()
    actual = sol.longestPalindrome(s)
    assert actual == expected, "expected %s but got %s" % (expected, actual)

def _test():
    """
    >>> _test()
    'OK'
    """

    long_str = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

    testCase("babad", "aba")
    testCase("cbbd", "bb")
    testCase("caaaabaaaaaaaaa", "aaaaaaaaa")
    testCase(long_str, long_str)
    return 'OK'

def profile():
    import profile
    lstr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    profile.runctx("testCase(lstr, lstr)", globals(), locals())

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "profile":
        profile()