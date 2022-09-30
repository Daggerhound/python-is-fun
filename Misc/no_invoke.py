class Item:
    def __init_subclass__(self):
        print(self)


class T_Shirt(Item):...