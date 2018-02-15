# encoding=utf-8
# @author xupingmao
# @since 2016/12/09
# @modified 2018/02/15 17:46:08

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

def profile():
    """Profile装饰器,打印信息到标准输出,不支持递归函数"""
    import profile as pf
    def deco(func):
        def handle(*args, **kw):
            vars = dict()
            vars["_f"] = func
            vars["_args"] = args
            vars["_kw"] = kw
            pf.runctx("r=_f(*_args, **_kw)", globals(), vars, sort="time")
            return vars["r"]
        return handle
    return deco