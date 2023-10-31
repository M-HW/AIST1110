import sys
into = '|-> '
out = '|<- '
space = '|   '




"""def trace(func):
    variable_list = func.__code__.co_varnames[:func.__code__.co_argcount]
    def f(*args):
        into = '|-> '
        outo = '|<- '
        space = '|   '
        global space_count
        print((space * space_count) + into, end='')
        print(func.__name__, end=' ')
        for i in args:
            print(i, end='')
        space_count += 1
        print()
        out = func(*args)
        space_count -= 1
        print(space * space_count + outo, end = '')
        print(f"return {out}")
        return out
    return f
    print(func.__name__, end=' ')
    variable_list = func.__code__.co_varnames[:func.__code__.co_argcount]
    import inspect 
    variable_list = inspect.signature(func)
    for i in variable_list:
        print(i, end = ' ')
    output = func(variable_list)
    return output
    pass"""

def trace(func):
    trace.depth = 0
    def f(*args):
        into = '|-> '
        outo = '|<- '
        space = '|   '
        print((space * trace.depth) + into, end='')
        trace.depth += 1
        print(func.__name__, end=' ')
        for i in args:
            print(i, end='')
        print()
        out = func(*args)
        print(space * trace.depth + outo, end = '')
        trace.depth -= 1
        print(f"return {out}")
        return out
    return f

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

space_count = 0
factorial = trace(factorial)
print(factorial(4))