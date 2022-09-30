class overload:
    """
    Decorating multiple functions with same name with this class
    will make it possible to, run different code, depending on how many,
    and, what type of arguments, you give the function.
    """
    overloaded = {}
    def __init__(self, func):
        self.__qualname__ = func.__qualname__
        self.funcs_update(func)

    def __call__(self, *args):
        for func_name, functions in overload.overloaded.items():
            if self.__qualname__ == func_name:
                for function in functions:
                    vals = list(function.__annotations__.values())
                    if len(vals) == len(args) == len(list(filter(lambda pair: pair[0] == type(pair[1]), zip(vals, args)))):
                        return function(*args)


    def funcs_update(self, func):
        functions = overload.overloaded
        func_name = func.__qualname__
        functions.update(
            {
                func_name: 
                functions.get(func_name, []) + [func]
            }
        )


@overload
def f(x: int):
    print(2*x)

@overload
def f(x: str):
    print(x)

@overload
def g(x : int, y : float):
    print(x+y)

f(5)
f("4")
g(3, 2.0)