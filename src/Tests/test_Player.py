from unittest import TestCase
from Model.Player import Player


class TestPlayer(TestCase):
    def setUp(self) -> None:
        self.player = Player()

    def test_get_health(self):
        self.assertEqual(self.player.health, 6)

    def test_set_health(self):
        self.player.health += 3
        self.assertEqual(self.player.health, 9)

    def test_get_attack(self):
        self.assertEqual(self.player.attack, 1)

    def test_set_attack(self):
        self.player.attack += 3
        self.assertEqual(self.player.attack, 4)

    def test_get_pos_x(self):
        self.assertEqual(self.player.pos_x, 0)

    def test_set_pos_x(self):
        self.player.pos_x += 2
        self.assertEqual(self.player.pos_x, 2)

    def test_get_pos_y(self):
        self.player.pos_y = 0

    def test_set_pos_y(self):
        self.player.pos_y += 5
        self.assertEqual(self.player.pos_y, 5)

    def test_get_hold_totem(self):
        self.assertEqual(self.player.hold_totem, False)

    def test_set_hold_totem(self):
        self.player.hold_totem = True
        self.assertEqual(self.player.hold_totem, True)

    def test_get_items(self):
        self.assertEqual(self.player.items, [])

    def test_add_item(self):
        self.player.add_item("Item 1", 1)
        self.player.add_item("Item 2", 2)
        self.assertListEqual(self.player.items, [["Item 1", 1], ["Item 2", 2]])

    def test_delete_item(self):
        self.player.add_item("Item 3", 3)
        self.player.add_item("Item 1", 1)
        self.player.add_item("Item 2", 2)
        self.player.delete_item("Item 1")
        self.assertListEqual(self.player.items, [["Item 3", 3], ["Item 2", 2]])
