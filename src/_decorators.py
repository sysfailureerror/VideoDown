#by SysFailureError
#date: 06/2020

import functools
import sys

# decorators

def d_pshow(arg1=None, arg2=None, arg3=None):

    def pshow(dfunc):
        @functools.wraps(dfunc)
        def pshow_wrapper(*args, **kwargs):
                
            if arg1 == "generator" or arg1 == "l_iter":
                for i in dfunc(*args, **kwargs):
                    
                    if arg2 == "end":
                        print(str(i), end=arg3)
                    else:
                        print(str(i))

                if arg2 == "end":
                    print("")
            else:
                print(dfunc(*args, **kwargs))

        return pshow_wrapper
    return pshow


def d_upper(func):
    @functools.wraps(func)
    def upper_wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return upper_wrapper


def d_exit_msg(func):
    @functools.wraps(func)
    def exit_msg_wrapper(*args, **kwargs):
        sys.exit(func(*args, **kwargs))

    return exit_msg_wrapper


def d_pinfor(func):
    @functools.wraps(func)
    def d_pinfor_wrapper(*args, **kwargs):
        for i in func(*args, **kwargs):
            yield i

    return d_pinfor_wrapper


def d_input(func):
    @functools.wraps(func)
    def p_input_wrapper(*args):
        return input(func(*args))

    return p_input_wrapper