from models.hockeygoods import HockeyGoods, Country, Type
from models.enums.protection import Protection


class ProtectiveEquipment (HockeyGoods):
    def __init__(self, name: str, price: float, weight_in_grams: int,
                 brand: str, origin_country: Country, color: str, type: Type,
                 material: str, age_category: str,
                 elements_of_protection: Protection):
        super().__init__(name, price, weight_in_grams, brand, origin_country,
                         color, type, material)
        self.age_category = age_category
        self.elements_of_protection = elements_of_protection

    def __str__(self):
        return super(ProtectiveEquipment, self).__str__() + \
            ("Age_category: {self.age_category}\n \
            Elements_of_protection: {self.elements_of_protection}") \
            .format(self=self)
