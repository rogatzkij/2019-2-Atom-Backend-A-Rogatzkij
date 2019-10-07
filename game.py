class Game:
    class AlreadyExist(Exception):
        pass

    class WrongChoise(Exception):
        pass

    def __init__(self, size):
        self.space = ' '
        self.playerOne = 'X'
        self.playerTwo = 'O'
        self.curPlayer = self.playerOne
        self.emptyFields = size * size

        self.size = size
        self.place = list()

        for x in range(self.size):
            self.place.append(list())
            self.place[x] = [self.space] * self.size

    def print(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.place[x][y], end=self.space)
            print()

    def makeChoise(self, x, y):
        if x >= self.size or y >= self.size:
            raise self.WrongChoise()

        if self.place[x][y] != self.space:
            raise self.AlreadyExist()

        self.place[x][y] = self.curPlayer
        self.emptyFields -= 1

    def changePlayers(self):
        if self.curPlayer == self.playerOne:
            self.curPlayer = self.playerTwo
        else:
            self.curPlayer = self.playerOne

    def check(self):
        # Свободные поля
        if self.emptyFields == 0:
            return "Players don't win!"

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
                return "Player {} win!".format(self.place[i][j])
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
                return "Player {} win!".format(self.place[i][j])
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
            return "Player {} win!".format(self.place[i][i])

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
            return "Player {} win!".format(self.place[self.size-i][i-1])

        return False


if __name__ == '__main__':
    logo = r'''
 _   _        _               _
| | (_)      | |             | |
| |_ _  ___  | |_ __ _  ___  | |_ ___   ___
| __| |/ __| | __/ _` |/ __| | __/ _ \ / _ \
| |_| | (__  | || (_| | (__  | || (_) |  __/
 \__|_|\___|  \__\__,_|\___|  \__\___/ \___|

rogatzkij(2019)
'''

    print(logo)
    game = Game(3)

    while True:
        try:
            x, y = input("Player {} make choise: ".format(
                game.curPlayer)).split()
            game.makeChoise(int(x), int(y))
        except Game.AlreadyExist:
            print("Field is already taken. Try again!")
            continue
        except Game.WrongChoise:
            print("Field not found. Try again!")
            continue
        except ValueError:
            print("Write only numbers. Try again!")
            continue

        game.print()
        game.changePlayers()

        result = game.check()
        if result is not False:
            print(result)
            break
