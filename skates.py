from models.hockeygoods import HockeyGoods, Country, Type
from models.enums.fixing import Fixing


class Skates (HockeyGoods):
    def __init__(self, name: str, price: float, weight_in_grams: int,
                 brand: str, origin_country: Country, color: str,
                 type: Type, material: str, type_of_fixing: Fixing,
                 size: int):
        super().__init__(name, price, weight_in_grams, brand, origin_country,
                         color, type, material)
        self.type_of_fixing = type_of_fixing
        self.size = size

    def __str__(self):
        return super(Skates, self).__str__() + \
            ("Type_of_fixing: {self.type_of_fixing}\nSize: {self.size}") \
            .format(self=self)
