from unittest import TestCase

from Model.Game import Game
from Model.GameData import GameData
from Model.Player import Player


class TestPlayer(TestCase):
    def setUp(self) -> None:
        self.game = Game()
        self.player = Player(self.game.game_data, self.game)
        self.game.game_data.shuffle_devcard_deck()
        self.game.game_data.shuffle_tiles_deck()
        self.game.game_data.remove_two_devcards()
        self.game.game_data.map[self.player.y][
            self.player.x
        ] = self.game.game_data.get_tile_by_name("Foyer")

    def test_set_health(self):
        initial_health = self.player.health
        add_amount = 2
        self.player.set_health(add_amount)
        expected = initial_health + add_amount

        self.assertEqual(self.player.health, expected)

    def test_add_attack(self):
        initial_attack = self.player.attack
        add_amount = 2
        self.player.add_attack(add_amount)
        expected = initial_attack + add_amount

        self.assertEqual(self.player.attack, expected)

    def test_add_item(self):
        item = "Machete"
        self.player.add_item(item)
        expected = [["Machete", 1]]

        self.assertEqual(self.player.items, expected)

    def test_delete_item(self):
        item = "Machete"
        self.player.add_item(item)
        self.player.delete_item("Machete")
        expected = []

        self.assertEqual(self.player.items, expected)

    def test_do_attack(self):
        self.game.current_zombie_count = 1
        self.player.do_attack()

        expected_zombies = 0
        expected_health = 6
        expected_attack = 0

        self.assertEqual(self.game.current_zombie_count, expected_zombies)
        self.assertEqual(self.player.health, expected_health)
        self.assertEqual(self.player.attack, expected_attack)

    def test_do_run(self):
        self.game.current_zombie_count = 1
        current_health = self.player.health
        self.player.do_run()
        expected_health = current_health - 1
        expected_zombies = 0

        self.assertEqual(self.player.health, expected_health)
        self.assertEqual(self.game.current_zombie_count, expected_zombies)

    def test_kill_all_zombies(self):
        self.game.current_zombie_count = 10
        self.player.kill_all_zombies("Oil")
        expected_zombies = 0

        self.assertEqual(self.game.current_zombie_count, expected_zombies)

    def test_negate_damage(self):
        self.game.current_zombie_count = 10
        self.player.negate_damage()

        expected_zombies = 0
        expected_health = self.player.health

        self.assertEqual(self.game.current_zombie_count, expected_zombies)
        self.assertEqual(self.player.health, expected_health)
