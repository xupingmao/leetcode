'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

from xutils import timeit

def cache(store = None):
    if store is None:
        store = {}
    def deco(func):
        def handle(*args):
            cache_key = args
            obj = store.get(cache_key)
            if obj != None:
                return obj
            value = func(*args)
            store[cache_key] = value
            return value
        return handle
    return deco

class Solution:
        
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_value = 0
        current = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            if c == ')':
                if len(stack) > 0:
                    stack.pop()
                    current += 2
                    max_value = max(max_value, current)
                else:
                    current = 0
        return max_value
       
@timeit()
def test(expected, input):
    s = Solution()
    r = s.longestValidParentheses(input)
    print('expected:', expected)
    print('result:', r)
    assert r == expected
    
test(2, '()')
test(2, '((()')
test(4, '((())')
test(0, '(((')
test(6, ")(())))(())())")
test(4, "((())((()")
test(68,"((()(())(((((((()((((()())))()(((()()))))(()(()))())(()(())(()((()()(((((()())(())))())(()(((()()))()(()()()(())))))(()())(())())()(()((((()()()())(((()()))((()()((((()(((((()((()())))()()))")
test(68,"((()(())(((((((()((((()())))()(((()()))))(()(()))())(()(())(()((()()(((((()())(())))())(()(((()()))()(()()()(())))))(()())(())())()(()((((()()()())(((()()))((()()((((()(((((()((()())))()())))))))))))))")
test(150,"(()())()(()(((()(((())((((()())()(((((((()())(())((()(((())(()())())))))(((((())))(()(())())))((((()))(())(()))()))(()())))())))))()(()())()())))(()((()))(()))(())(((())((((())()(()(()(())))))())()(")
test(168,"((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))")
