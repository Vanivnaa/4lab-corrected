from models.hockeygoods import HockeyGoods
from models.enums.color import Color


class Puck (HockeyGoods):
    def __init__(self, name: str, price: float, weight_in_grams: int,
                 brand: str, origin_country: Country, color: str, type: Type,
                 material: str, thickness: float, diameter: float,
                 destination_color: Color):
        super().__init__(name, price, weight_in_grams, brand, origin_country,
                         color, type, material)
        self.thickness = thickness
        self.diameter = diameter
        self.destination_color = destination_color

    def __str__(self):
        return super(Puck, self).__str__() + ("Thickness: {self.thickness}\n \
        Diameter: {self.diameter}\n \
        Destination_color: {self.destination_color}").format(self=self)
