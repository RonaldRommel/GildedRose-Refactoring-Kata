# -*- coding: utf-8 -*-


class Item:
    """DO NOT MODIFY — belongs to the goblin in the corner."""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


# ---------------------------------------------------------------------------
# Strategy base class
# ---------------------------------------------------------------------------

class UpdateStrategy:
    """Base strategy: defines the interface for updating an item."""

    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def update(self, item):
        raise NotImplementedError

    def _clamp(self, value):
        return max(self.MIN_QUALITY, min(self.MAX_QUALITY, value))


# ---------------------------------------------------------------------------
# Concrete strategies — one per item type
# ---------------------------------------------------------------------------

class NormalItemStrategy(UpdateStrategy):
    """Standard item: quality degrades by 1 per day, 2x after sell_in."""

    def update(self, item):
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        item.quality = self._clamp(item.quality - degradation)


class AgedBrieStrategy(UpdateStrategy):
    """Aged Brie: quality increases by 1 per day, 2x after sell_in."""

    def update(self, item):
        item.sell_in -= 1
        increase = 2 if item.sell_in < 0 else 1
        item.quality = self._clamp(item.quality + increase)


class SulfurasStrategy(UpdateStrategy):
    """Sulfuras: legendary item — never changes, never sold."""

    def update(self, item):
        pass  # Sulfuras never degrades and sell_in never decreases


class BackstagePassStrategy(UpdateStrategy):
    """
    Backstage passes:
    - quality increases by 1 when > 10 days remaining
    - increases by 2 when 6–10 days remaining
    - increases by 3 when 1–5 days remaining
    - drops to 0 after the concert (sell_in < 0)
    """

    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = self._clamp(item.quality + 3)
        elif item.sell_in < 10:
            item.quality = self._clamp(item.quality + 2)
        else:
            item.quality = self._clamp(item.quality + 1)


class ConjuredItemStrategy(UpdateStrategy):
    """Conjured items: degrade in quality twice as fast as normal items."""

    def update(self, item):
        item.sell_in -= 1
        degradation = 4 if item.sell_in < 0 else 2
        item.quality = self._clamp(item.quality - degradation)


# ---------------------------------------------------------------------------
# Strategy Factory — maps item names to strategies
# ---------------------------------------------------------------------------

class StrategyFactory:
    """
    Factory that returns the correct UpdateStrategy for a given item.
    To support a new item type, simply add an entry to _strategies —
    no other code needs to change (Open/Closed Principle).
    """

    _strategies = {
        "Aged Brie":                          AgedBrieStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Sulfuras, Hand of Ragnaros":         SulfurasStrategy(),
        "Conjured Mana Cake":                 ConjuredItemStrategy(),
    }
    _default = NormalItemStrategy()

    @classmethod
    def get_strategy(cls, item_name):
        return cls._strategies.get(item_name, cls._default)


# ---------------------------------------------------------------------------
# GildedRose — now clean and trivially extensible
# ---------------------------------------------------------------------------

class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = StrategyFactory.get_strategy(item.name)
            strategy.update(item)