class Multiply:

    def __init__(self, x):
        self.x = x

    def __call__(self, a):
        try:
            self.x *= a()
        except TypeError:
            self.x *= a().x

        return self

    def __repr__(self):
        return str(self.x)


def five_factorial():
    @Multiply(1)
    def two():
        @Multiply(2)
        def three():
            @Multiply(3)
            def four():
                @Multiply(4)
                def five():
                    return 5
                return five
            return four
        return three
    return two

print(five_factorial())