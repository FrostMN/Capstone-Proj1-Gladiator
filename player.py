class Player:
    hp = int
    potions = 13
    player_x = int
    player_y = int

    def __init__(self, x, y):
        self.hp = 10
        self.player_x = x
        self.player_y = y

    def up(self, world):
        if world[self.player_y - 1][self.player_x] == 2:
            world[self.player_y - 1][self.player_x] = 3
            world[self.player_y][self.player_x] = 2
            self.player_y -= 1

        return

    def left(self, world):
        if world[self.player_y][self.player_x - 1] == 2:
            world[self.player_y][self.player_x - 1] = 3
            world[self.player_y][self.player_x] = 2
            self.player_x -= 1

        return

    def down(self, world):
        if world[self.player_y + 1][self.player_x] == 2:
            world[self.player_y + 1][self.player_x] = 3
            world[self.player_y][self.player_x] = 2
            self.player_y += 1

        return

    def right(self, world):
        if world[self.player_y][self.player_x + 1] == 2:
            world[self.player_y][self.player_x + 1] = 3
            world[self.player_y][self.player_x] = 2
            self.player_x += 1

        return

    def potion(self, world):
        if self.potions > 10:
            self.potions -= 1
            self.hp = 10
        return
