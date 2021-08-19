class Furniture:

    def __init__(self, height, width, length, color):
        self.height = height
        self.width = width
        self.length = length
        self.color = color
        self.area = self.length * self.width
        self.volume = self.length * self.width * self.height


class Cupboard(Furniture):

    def __init__(self, height, width, length, color, wood_type):
        super().__init__(height, width, length, color)
        self.wood_type = wood_type

class Couch(Furniture):

    def __init__(self, height, width, length, color, material):
        super().__init__(height, width, length, color)
        self.material = material

class Table(Furniture):

    def __init__(self, height, width, length, color, purpose):
        super().__init__(height, width, length, color)
        self.purpose = purpose


tbl1 = Table(0.8, 0.6, 0.9, "black", "tv")
cch1 = Couch(1, 0.9, 2.5, "white", "leather")
cbd1 = Cupboard(2, 1, 1.2, "brown", "oak")
print(tbl1.volume, "m3")
print(cbd1.area, "m2")