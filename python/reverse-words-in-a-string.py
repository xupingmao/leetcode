# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/04/10
# 

"""Description here"""
class Solution(object):
    def reverse(self, word):
        v = list(word)
        v.reverse()
        return ''.join(v)
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        out = []
        for word in words:
            out.append(self.reverse(word))
        return " ".join(out)

def test():
    assert 
    """
        >>> test()
        'OK'
    """
    return 'OK'