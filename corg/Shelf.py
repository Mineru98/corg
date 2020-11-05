class Item:
    def __init__(self, obj):
        self.word = obj.word
        self.score = obj.score


class Shelf:
    def __init__(self, list):
        self.items = list
        for item in list:
            self.items.append(Item(item))

    def sort(self):
        print("정렬 완료!!!")

