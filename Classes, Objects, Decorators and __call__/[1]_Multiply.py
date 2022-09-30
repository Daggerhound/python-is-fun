class Multiply:

    def __init__(self, x):
        self.x = x

    def __call__(self, a):
        return self.x * a

    def __repr__(self):
        return str(self.x)


print(Multiply(Multiply(Multiply(Multiply(Multiply(1)(2))(3))(4))(5)))