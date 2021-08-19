class Furniture():

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '[%s]Land occupation: %.2f' % (self.name, self.area)


# bed = Furniture('bed',4)
# print(bed)

class House():

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        #Residual area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ('Apartment: %s\n total area: %.2f[Residual area: %.2f]\n furniture:%s'
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self,item):
        #1. Judging the area of furniture
        if item.area > self.free_area:
            print('%s The area is too large to add.' %item.name)

        #2. Adding Furniture
        self.item_list.append(item.name)

        #3. Calculating Residual Area
        self.free_area -= item.area

bed = Furniture('bed',4)
print(bed)
yigui = Furniture('yigui',200)
print(yigui)
table = Furniture('table',1.5)
print(table)

my_house = House('Single family',400)

my_house.add_item(bed)
my_house.add_item(yigui)
my_house.add_item(table)
print(my_house)