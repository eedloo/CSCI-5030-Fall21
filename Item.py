class Item:
    item = ''
    item_type = ''

    def create_item(self, item, item_type):
        self.item = item
        self.item_type = item_type
        return [f'CreateItem({self.item}, {self.item_type})']

