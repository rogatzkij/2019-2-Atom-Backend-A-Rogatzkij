import unittest
from game import Game


class TestGame(unittest.TestCase):

    size = 3
    isPrint = True

    def test_already_exist(self):
        print("test_already_exist")

        g = Game(self.size)
        g.makeChoise(0, 0)

        with self.assertRaises(Game.AlreadyExist):
            g.makeChoise(0, 0)

    def test_wrong_choise(self):
        print("test_wrong_choise")

        g = Game(self.size)
        with self.assertRaises(Game.WrongChoise):
            g.makeChoise(self.size, self.size)

    def test_diag(self):
        print("test_diag")

        g = Game(self.size)
        for i in range(self.size):
            g.makeChoise(i, i)

        if self.isPrint is True:
            print("-"*(self.size+2))
            g.print()

        self.assertEqual(g.check(), "Player {} win!".format(g.curPlayer))

    def test_side_diag(self):
        print("test_side_diag")

        g = Game(self.size)

        for i in range(self.size):
            g.makeChoise(i, self.size-i-1)

        if self.isPrint is True:
            print("-"*(self.size+2))
            g.print()

        self.assertEqual(g.check(), "Player {} win!".format(g.curPlayer))

    def test_vertical(self):
        print("test_vertical")

        for j in range(self.size):
            g = Game(self.size)
            for i in range(self.size):
                g.makeChoise(j, i)
            if self.isPrint is True:
                print("-"*(self.size+2))
                g.print()

            self.assertEqual(g.check(), "Player {} win!".format(g.curPlayer))

    def test_all_fields(self):
        print("test_all_fields")
        g = Game(self.size)

        for i in range(self.size):
            for j in range(self.size):
                g.makeChoise(i, j)
        if self.isPrint is True:
            print("-"*(self.size+2))
            g.print()

            self.assertEqual(g.check(), "Players don't win!")

    def test_horizontal(self):
        print("test_horizontal")

        for j in range(self.size):
            g = Game(self.size)
            for i in range(self.size):
                g.makeChoise(i, j)
            if self.isPrint is True:
                print("-"*(self.size+2))
                g.print()

            self.assertEqual(g.check(), "Player {} win!".format(g.curPlayer))


if __name__ == '__main__':
    unittest.main()
