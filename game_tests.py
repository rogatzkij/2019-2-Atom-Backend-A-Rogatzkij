import unittest
from game import Game


class TestGame(unittest.TestCase):

    size = 3
    is_print = True

    def test_full_game(self):
        g = Game(3)
        hody = [(0, 0), (2, 2), (0, 1), (1, 1), (0, 2)]

        for x, y in hody:
            g.make_choise(x, y)
            g.change_players()

        self.assertEqual(g.check(), Game.GameStatus.WIN_P_ONE)

    def test_already_exist(self):
        print("test_already_exist")

        g = Game(self.size)
        g.make_choise(0, 0)

        with self.assertRaises(Game.AlreadyExist):
            g.make_choise(0, 0)

    def test_wrong_choise(self):
        print("test_wrong_choise")

        g = Game(self.size)
        with self.assertRaises(Game.WrongChoise):
            g.make_choise(self.size, self.size)

    def test_diag(self):
        print("test_diag")

        g = Game(self.size)
        for i in range(self.size):
            g.make_choise(i, i)

        if self.is_print is True:
            print("-"*(self.size+2))
            g.print_field()

        self.assertEqual(g.check(), Game.GameStatus.WIN_P_ONE)

    def test_side_diag(self):
        print("test_side_diag")

        g = Game(self.size)

        for i in range(self.size):
            g.make_choise(i, self.size-i-1)

        if self.is_print is True:
            print("-"*(self.size+2))
            g.print_field()

        self.assertEqual(g.check(), Game.GameStatus.WIN_P_ONE)

    def test_vertical(self):
        print("test_vertical")

        for j in range(self.size):
            g = Game(self.size)
            for i in range(self.size):
                g.make_choise(j, i)
            if self.is_print is True:
                print("-"*(self.size+2))
                g.print_field()

            self.assertEqual(g.check(), Game.GameStatus.WIN_P_ONE)

    def test_all_fields(self):
        print("test_all_fields")
        g = Game(self.size)

        for i in range(self.size):
            for j in range(self.size):
                g.make_choise(i, j)
        if self.is_print is True:
            print("-"*(self.size+2))
            g.print_field()

            self.assertEqual(g.check(), Game.GameStatus.NO_WIN)

    def test_horizontal(self):
        print("test_horizontal")

        for j in range(self.size):
            g = Game(self.size)
            for i in range(self.size):
                g.make_choise(i, j)
            if self.is_print is True:
                print("-"*(self.size+2))
                g.print_field()

            self.assertEqual(g.check(), Game.GameStatus.WIN_P_ONE)


if __name__ == '__main__':
    unittest.main()
