# encoding=utf-8


class Solution(object):

    def isOverflow(self, numVal):
        """int32范围 -2147483648~2147483647"""
        return numVal > 2147483647 or numVal < -2147483648

    def isPalindrome0(self, str):
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
        for i in range(mid + 1):
            if str[i] != str[length - i - 1]:
                return False
        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if self.isOverflow(x):
            return False
        int_str = str(x)
        return self.isPalindrome0(int_str)


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(0) == True
    assert s.isPalindrome(1) == True
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(123) == False
    assert s.isPalindrome(-1) == False
    assert s.isPalindrome(2147483648) == False
    assert s.isPalindrome(-2147483649) == False
