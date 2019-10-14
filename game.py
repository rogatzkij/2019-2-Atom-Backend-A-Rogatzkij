from enum import Enum


class Game:
    """
        Game - class описывающий игру
    """
    class GameStatus(Enum):
        NO_WIN = 0
        WIN_P_ONE = 1
        WIN_P_TWO = 2
        WIN_BOTH = 3

    class AlreadyExist(Exception):
        """
        AlreadyExist - ошибка, поле уже занято
        """
        pass

    class WrongChoise(Exception):
        """
        WrongChoise - ошибка, поля не существует
        """
        pass

    def __init__(self, size):
        """
        __init__ - конструктор, принимает размер игрового поля
        """
        self.space = ' '
        self.player_one = 'X'
        self.player_two = 'O'
        self.cur_player = self.player_one
        self.empty_fields = size * size

        self.size = size
        self.place = list()

        for x in range(self.size):
            self.place.append(list())
            self.place[x] = [self.space] * self.size

    def print_field(self):
        """
        печать игрового поля
        """
        for x in range(self.size):
            for y in range(self.size):
                print(self.place[x][y], end=self.space)
            print()

    def make_choise(self, x, y):
        """
        произвести ход текущеко игрока
        """
        if x >= self.size or y >= self.size:
            raise self.WrongChoise()

        if self.place[x][y] != self.space:
            raise self.AlreadyExist()

        self.place[x][y] = self.cur_player
        self.empty_fields -= 1

    def change_players(self):
        """
        сменить текущего игрока
        """
        if self.cur_player == self.player_one:
            self.cur_player = self.player_two
        else:
            self.cur_player = self.player_one

    def print_status(self, status):
        """
        печать статуса игры
        """
        if status == Game.GameStatus.WIN_BOTH:
            print("Both players win!")
            return True
        elif status == Game.GameStatus.WIN_P_ONE:
            print("Playe {} win!".format(self.player_one))
            return True
        elif status == Game.GameStatus.WIN_P_TWO:
            print("Playe {} win!".format(self.player_two))
            return True

        return False

    def check(self):
        """
        проверка состояния игры
        """
        # Свободные поля
        if self.empty_fields == 0:
            return self.GameStatus.NO_WIN

        # Горизонталь
        for i in range(self.size):
            flag = True
            for j in range(1, self.size):
                if self.place[i][j] != self.place[i][j-1]:
                    flag = False
                    break
                if self.place[i][j] == self.space:
                    flag = False
                    break

            if flag is True:
                if self.place[i][j] == self.player_one:
                    return self.GameStatus.WIN_P_ONE
                else:
                    return self.GameStatus.WIN_P_TWO
        # Вертикаль
        for j in range(self.size):
            flag = True
            for i in range(1, self.size):
                if self.place[i][j] != self.place[i-1][j]:
                    flag = False
                    break
                if self.place[i][j] == self.space:
                    flag = False
                    break

            if flag is True:
                if self.place[i][j] == self.player_one:
                    return self.GameStatus.WIN_P_ONE
                else:
                    return self.GameStatus.WIN_P_TWO
        # Диагональ
        flag = True
        for i in range(1, self.size):
            if self.place[i][i] != self.place[i-1][i-1]:
                flag = False
                break
            if self.place[i][i] == self.space:
                flag = False
                break
        if flag is True:
            if self.place[i][i] == self.player_one:
                return self.GameStatus.WIN_P_ONE
            else:
                return self.GameStatus.WIN_P_TWO

        # Побочная диагональ
        flag = True
        for i in range(1, self.size):
            if self.place[self.size-i][i-1] != self.place[self.size-i-1][i]:
                flag = False
                break
            if self.place[self.size-i][i-1] == self.space:
                flag = False
                break
        if flag is True:
            if self.place[self.size-i][i-1] == self.player_one:
                return self.GameStatus.WIN_P_ONE
            else:
                return self.GameStatus.WIN_P_TWO
            # return "Player {} win!".format(self.place[self.size-i][i-1])

        return False

    def new_game(self):
        """
        запуск игры
        """
        print(self.logo)

        while True:
            try:
                x, y = input("Player {} make choise: ".format(
                    self.cur_player)).split()
                self.make_choise(int(x), int(y))
            except Game.AlreadyExist:
                print("Field is already taken. Try again!")
                continue
            except Game.WrongChoise:
                print("Field not found. Try again!")
                continue
            except ValueError:
                print("Write only numbers. Try again!")
                continue

            self.print_field()
            self.change_players()

            result = self.print_status(self.check())
            if result is not False:
                break
    logo = r'''
_   _        _               _
| | (_)      | |             | |
| |_ _  ___  | |_ __ _  ___  | |_ ___   ___
| __| |/ __| | __/ _` |/ __| | __/ _ \ / _ \
| |_| | (__  | || (_| | (__  | || (_) |  __/
 \__|_|\___|  \__\__,_|\___|  \__\___/ \___|

rogatzkij(2019)
            '''


if __name__ == '__main__':
    game = Game(3)
    game.new_game()
