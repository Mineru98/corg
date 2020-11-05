from Shelf import Shelf


class Item:
    def __init__(self, obj):
        self.content_title = obj.content_title
        self.content_type = obj.content_type
        self.affect_area = obj.affect_area
        self.export_date = obj.export_date
        self.content = obj.content
        self.content_url = obj.content_url
        self.view_count = obj.view_count


class Content(Shelf):
    def __init__(self, list):
        self.score = 0
        self.list = []
        for item in list:
            self.list.append(item)

    def sort(self):
        print("정렬 완료!!!")

