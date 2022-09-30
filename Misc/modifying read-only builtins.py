class gg:
    def __eq__(self, other):
        other["x"] = 5


str.__dict__ == gg()

print("a".x)