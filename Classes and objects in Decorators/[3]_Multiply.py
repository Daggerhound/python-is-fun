class Multiply:

    def __init__(self, x):
        self.x = x

    def __call__(self, a = lambda: 1):
        if a() == None:
            a = lambda: 1

        try:
            self.x *= a()
        except TypeError:
            self.x *= a().x

        return self

    def __repr__(self):
        return str(self.x)


@Multiply(1)
@Multiply(2)
@Multiply(3)
@Multiply(4)
@Multiply(5)
def nice():
    pass

print(nice)