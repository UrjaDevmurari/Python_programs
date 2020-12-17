# this program is to show inheritance in python
# Composition is better is widely used approach than inheritance


class House:
    def __init__(self, floors, carpet_area):
        self.floors = floors
        self.carpet_area = carpet_area
        self.painted = False

    def paintTheHouse(self):
        self.painted = True

    def __str__(self):
        return f"This house has {self.floors} floors and {self.carpet_area} sqft carpet area."


class HouseType(House):
    def __init__(self, floors, carpet_area, type):
        super().__init__(floors, carpet_area)
        self.type = type

    def __str__(self):
        return f"{super().__str__()} and is a {self.type}"


house1 = HouseType(1, 1500, "Appartment")
print(house1)
