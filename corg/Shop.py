from Shelf import Shelf


class Shop(Shelf):
    def __init__(self, obj):
        self.shop_name = obj.shop_name
        self.shop_type = obj.shop_type
        self.local_area = obj.local_area
        self.retention_period = obj.retention_period
        self.handling_type = obj.handling_type
        self.handling_type_p = obj.handling_type_p
        self.search_log = obj.search_log

    def export(self, word):
        print(word)

    def sort(self):
        print("정렬 완료!!!")

