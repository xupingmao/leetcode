class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opstack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in '([{':
                opstack.append(c)
            if c in ')]}':
                if len(opstack) == 0:
                    return False
                last = opstack.pop()
                if mapping[last] != c:
                    return False
        return len(opstack) == 0
                
def test(expected, input):
    s = Solution()
    r = s.isValid(input)
    assert r == expected
    
test(True, '[]')
test(True, '{[]123213}')
test(False, '[{]}')