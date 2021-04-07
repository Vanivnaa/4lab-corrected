from models.hockeygoods import HockeyGoods
from models.manage import HockeyClubManage
from models.enums.type import Type
from models.enums.fixing import Fixing
from models.enums.country import Country
from models.enums.sort import SortOrder
from models.skates import Skates
from models.stick import Stick
from models.protectiveequipment import ProtectiveEquipment, Protection


def main():

    skates = Skates("Skates", 1500, 1148, "TECNOPRO", "China", "black",
                    Type.FIELD_PLAYER, "pvc leather", Fixing.SHOELACE, 39)
    stick = Stick("Stick", 1752, 500, "FISHER", "Germany", "yellow",
                  Type.FIELD_PLAYER, "carbon fiber, fiberglass", 166, 85, 135)
    helmet = ProtectiveEquipment("Helmet", 1248, 600, "Bauer", "Poland",
                                 "white", Type.GOALKEEPER, "plastic", "Adult",
                                 "Helmet")

    manage = HockeyClubManage([skates, stick, helmet])

    print("\n\t\tGoods for field hockey players \n")
    print(manage.search_by_type(Type.FIELD_PLAYER))
    print("___________________________________________________________")
    print("\n\t\tSorting goods by price:\n")
    manage.sort_by_price(SortOrder.DESC)
    print("___________________________________________________________")
    print("\n\t\tSorting goods by country:\n")
    manage.sort_by_country(SortOrder.ASC)
    print("___________________________________________________________")
    print("\n\n\t\tCharacteristics of goods\n\n\t", skates, "\n\n\t", stick,
          "\n\n\t", helmet)


if __name__ == "__main__":
    main()
