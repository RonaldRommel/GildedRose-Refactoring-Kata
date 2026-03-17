# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # ------------------------------------------------------------------
    # Test 1: Normal item degrades in quality by 1 before sell_in date
    # ------------------------------------------------------------------
    def test_normal_item_degrades_by_1_before_sell_date(self):
        """A normal item loses 1 quality per day while sell_in > 0."""
        items = [Item("Elixir of the Mongoose", 5, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 9)

    # ------------------------------------------------------------------
    # Test 2: Normal item degrades TWICE as fast after sell_in date
    # ------------------------------------------------------------------
    def test_normal_item_degrades_twice_as_fast_after_sell_date(self):
        """Once sell_in < 0, a normal item loses 2 quality per day."""
        items = [Item("Elixir of the Mongoose", 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        # sell_in goes to -1, so degradation should be 2
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 8)

    # ------------------------------------------------------------------
    # Test 3: Aged Brie increases in quality over time
    # ------------------------------------------------------------------
    def test_aged_brie_increases_in_quality(self):
        """Aged Brie gains 1 quality per day before the sell_in date."""
        items = [Item("Aged Brie", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 21)

    # ------------------------------------------------------------------
    # Test 4: Conjured items degrade twice as fast as normal items
    # ------------------------------------------------------------------
    def test_conjured_item_degrades_twice_as_fast(self):
        """Conjured Mana Cake loses 2 quality per day before sell_in."""
        items = [Item("Conjured Mana Cake", 5, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 18)  # degraded by 2

    # ------------------------------------------------------------------
    # Bonus: Additional edge-case tests
    # ------------------------------------------------------------------
    def test_quality_never_goes_below_zero(self):
        """Quality should never become negative."""
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_never_exceeds_50(self):
        """Quality should never exceed 50 (Aged Brie at max)."""
        items = [Item("Aged Brie", 10, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_never_changes(self):
        """Sulfuras sell_in and quality should never change."""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_pass_drops_to_zero_after_concert(self):
        """Backstage pass quality becomes 0 after the concert (sell_in < 0)."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    def test_backstage_pass_increases_by_3_within_5_days(self):
        """Backstage pass gains 3 quality when sell_in is 5 or fewer days."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 33)


if __name__ == "__main__":
    unittest.main()