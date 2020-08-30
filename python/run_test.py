# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/08/23 13:46:12
# @modified 2020/08/23 13:58:27

TARGET_CLASS = None
TEST_CASE_NO = 0

def run_test(args, expect):
    global TEST_CASE_NO
    TEST_CASE_NO += 1
    # print(dir(SOLUTION_FUNC))
    # print(dir(SOLUTION_FUNC.__class__))
    solution_class = SOLUTION_FUNC.__globals__["Solution"]
    # solution  = SOLUTION_FUNC.__class__()
    solution  = solution_class()
    func_name = SOLUTION_FUNC.func_name
    function  = getattr(solution, func_name)
    result = function(*args)
    assert result == expect, "expect %s but see %s" % (expect, result)

    print("Case %03d pass" % TEST_CASE_NO)


def solution_func(func):
    global SOLUTION_FUNC
    SOLUTION_FUNC = func
    return func
