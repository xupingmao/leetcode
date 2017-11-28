# -*- coding:utf-8 -*-
# Created on 2017/07/02
# Author: xupingmao 578749341@qq.com
# Copyright (c) 2017
#
# Last Modified

"""Description here"""


"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

PRINT=False

class State:

    def __init__(self, type, value=None, next=None):
        self.type = type
        self.value = value
        self.next = next

    def __repr__(self):
        return self.type

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value


def build(pattern):
    start = State("^")
    state_list = [start]
    for c in pattern:
        if c == '*':
            last = state_list.pop()
            star = State("*", last)
            state_list.append(star)
        elif c == ".":
            state = State(".")
            state_list.append(state)
        else:
            state = State(c, c)
            state_list.append(state)
    prev = start
    for state in state_list[1:]:
        prev.next = state
        prev = state
    prev.next = State('$')
    return start


def match_here(state, index, text):
    # 使用动态规划优化可以大幅提升性能
    # print(index, state)
    if state is None:
        return False
    if state.type == '^':
        return match_here(state.next, index, text)
    if state.type == '*':
        return match_star(state, index, text)
    if state.type == '$':
        return index == len(text)
    if state.type == '.':
        return match_here(state.next, index+1, text)
    if index < len(text) and state.type == text[index]:
        return match_here(state.next, index+1, text)
    return False

def match_star(state, index, text):
    match_value = state.value.type
    next_state  = state.next
    length = len(text)
    while index <= length:
        # 先忽略star匹配直接匹配后面的
        if match_here(next_state, index, text):
            return True
        if index == length:
            return False
        # 匹配失败，使用当前的pattern匹配
        if match_value == text[index] or match_value == '.':
            # 移到下一位
            index += 1
        else:
            # 全部匹配失败
            return False
    return False

class Solution(object):

    def isMatch(self, s, p):
        pattern = build(p)
        return match_here(pattern, 0, s)


def isMatch(s, p):
    sl = Solution()
    return sl.isMatch(s, p)

if __name__ == '__main__':
    assert isMatch("aa", "a") == False
    assert isMatch("aa", "aa") == True
    assert isMatch("aaa", "aa") == False
    assert isMatch("aaa", "a*a") == True # TODO
    assert isMatch("aa", "a*") == True
    assert isMatch("aa", ".*") == True
    assert isMatch("ab", ".*") == True
    assert isMatch("aab", "c*a*b") == True
    assert isMatch("ab", ".*c") == False
    assert isMatch("aaa", "aaaa") == False
    assert isMatch("aa", "aa.*") == True
    assert isMatch("aaa", "ab*a*c*a") == True
