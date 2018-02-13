# encoding=utf-8
# @author xupingmao
# @since 2016/12/09
# @modified 2018/02/13 11:22:21

import time


#################################################################
##   各种装饰器
#################################################################

def timeit(repeat=1):
    """简单的计时装饰器，可以指定执行次数"""
    def deco(func):
        def handle(*args):
            t1 = time.time()
            for i in range(repeat):
                ret = func(*args)
            t2 = time.time()
            print("cost time", t2-t1)
            return ret
        return handle
    return deco
