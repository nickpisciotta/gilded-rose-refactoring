import pdb

class GildedRose(object):
    def __init__(self, items):
        self.items = ItemFactory(items).get_items()

    def update_quality(self):
        updated_items = [] 
        for item in self.items:
            item.update_quality()
            updated_items.append(item)
        return updated_items

class ItemFactory():
    def __init__(self, items):
        self.items = items

    def get_items(self):
        new_items = []
        for item in self.items:
            if item.name == "normal":
                new_items.append(Normal(name=item.name, sell_in=item.sell_in, quality=item.quality))
            if item.name == "Aged Brie":
                new_items.append(Aged_Brie(name=item.name, sell_in=item.sell_in, quality=item.quality))
            if item.name == "Sulfuras, Hand of Ragnaros":
                new_items.append(Item(name=item.name, sell_in=item.sell_in, quality=item.quality))
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                new_items.append(Backstage(name=item.name, sell_in=item.sell_in, quality=item.quality))
        return new_items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        return 

class Normal(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality == 0:
            return 
        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1 
    
class Aged_Brie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality == 50:
            return 
        self.quality += 1

class Backstage(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
            return 
        self.quality += 1
        if self.quality == 50:
            return
        if self.sell_in < 10:
            self.quality += 1
        if self.sell_in < 5:
            self.quality += 1