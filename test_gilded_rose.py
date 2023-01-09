import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_decreases_quality_by_one_before_sellin_date(self):
        items = [Item(name="normal", sell_in=10, quality=5)]
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("normal", updated_items[0].name)
        self.assertEqual(9, updated_items[0].sell_in)
        self.assertEqual(4, updated_items[0].quality)

    def test_normal_item_quality_does_not_become_negative(self):
        items = [Item(name="normal", sell_in=10, quality=0)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("normal", updated_items[0].name)
        self.assertEqual(9, updated_items[0].sell_in)
        self.assertEqual(0 , updated_items[0].quality)


    def test_normal_item_quality_decreases_by_two_after_sell_in(self):
        items = [Item(name="normal", sell_in=0, quality=10)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual(-1, updated_items[0].sell_in)
        self.assertEqual(8, updated_items[0].quality)

    def test_aged_brie_quality_increases_by_one_before_sellin_date(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=10)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Aged Brie", updated_items[0].name)
        self.assertEqual(4, updated_items[0].sell_in)
        self.assertEqual(11, updated_items[0].quality)

    def test_aged_brie_item_quality_does_not_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=50)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Aged Brie", updated_items[0].name)
        self.assertEqual(4, updated_items[0].sell_in)
        self.assertEqual(50, updated_items[0].quality)
        
    def test_sulfuras_item_quality_or_sellin_never_decreases(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=50)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", updated_items[0].name)
        self.assertEqual(5, updated_items[0].sell_in)
        self.assertEqual(50, updated_items[0].quality)

    def test_backstage_passes_increases_quality_by_one_before_10_days_sellin(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=47)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", updated_items[0].name)
        self.assertEqual(10, updated_items[0].sell_in)
        self.assertEqual(48, updated_items[0].quality)

    def test_backstage_passes_increases_quality_by_two_between_10_to_6_days_sellin(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=40)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", updated_items[0].name)
        self.assertEqual(9, updated_items[0].sell_in)
        self.assertEqual(42, updated_items[0].quality)

    def test_backstage_passes_increases_quality_by_three_between_5_to_0_days_sellin(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", updated_items[0].name)
        self.assertEqual(4, updated_items[0].sell_in)
        self.assertEqual(43, updated_items[0].quality)
        
    def test_backstage_passes_quality_drops_to_0_after_0_sellin(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=40)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", updated_items[0].name)
        self.assertEqual(-1, updated_items[0].sell_in)
        self.assertEqual(0, updated_items[0].quality)

    def test_backstage_passes_quality_never_exceeds_50(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)]   
        gilded_rose = GildedRose(items)

        updated_items = gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", updated_items[0].name)
        self.assertEqual(9, updated_items[0].sell_in)
        self.assertEqual(50, updated_items[0].quality)

        
if __name__ == '__main__':
    unittest.main()