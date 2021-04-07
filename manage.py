from models.enums.type import Type
from models.enums.sort import SortOrder
from models.hockeygoods import HockeyGoods, Type
from operator import attrgetter


class HockeyClubManage:
    def __init__(self, goods: []):
        self.goods = goods

    def sort_by_price(self, sort_order: SortOrder):
        s = sorted(self.goods, key=attrgetter('price'),
                   reverse=sort_order == SortOrder.DESC)
        for x in range(len(s)):
            print("\t\t", s[x].name, "-", s[x].price, "$")
        return s

    def sort_by_country(self, sort_order: SortOrder):
        s = sorted(self.goods, key=attrgetter('origin_country'),
                   reverse=sort_order == SortOrder.DESC)
        for x in range(len(s)):
            print("\t\t", s[x].name, "-", s[x].origin_country)
        return s

    def search_by_type(self, type: Type):
        new_goods = []
        for hockeyGoods in self.goods:
            if hockeyGoods.type == type:
                new_goods.append(HockeyGoods)
        return new_goods
