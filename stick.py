from models.hockeygoods import HockeyGoods, Country, Type


class Stick (HockeyGoods):
    def __init__(self, name: str, price: float, weight_in_grams: int,
                 brand: str, origin_country: Country, color: str,
                 type: Type, material: str, length: float, rigidity: int,
                 angle_of_inclination_in_degrees: int):
        super().__init__(name, price, weight_in_grams, brand, origin_country,
                         color, type, material)
        self.length = length
        self.rigidity = rigidity
        self.angle_of_inclination_in_degrees = angle_of_inclination_in_degrees

    def __str__(self):
        return super(Stick, self).__str__() + ("Length: {self.length}\n \
        Rigidity: {self.rigidity}\nAngle_of_inclination_in_degrees: \
        {self.angle_of_inclination_in_degrees}").format(self=self)
