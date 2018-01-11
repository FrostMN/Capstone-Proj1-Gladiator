class Enemy:
    hp = int
    dr = int
    enemy_x = int
    enemy_y = int

    def __init__(self, x, y):
        self.hp = 10
        self.dr = 1
        self.attack = 2
        self.enemy_x = x
        self.enemy_y = y

    def up(self, world):
        if world[self.enemy_y - 1][self.enemy_x] == 2:
            world[self.enemy_y - 1][self.enemy_x] = 3
            world[self.enemy_y][self.enemy_x] = 2
            self.enemy_y -= 1

        return

    def left(self, world):
        if world[self.enemy_y][self.enemy_x - 1] == 2:
            world[self.enemy_y][self.enemy_x - 1] = 3
            world[self.enemy_y][self.enemy_x] = 2
            self.enemy_x -= 1

        return

    def down(self, world):
        if world[self.enemy_y + 1][self.enemy_x] == 2:
            world[self.enemy_y + 1][self.enemy_x] = 3
            world[self.enemy_y][self.enemy_x] = 2
            self.enemy_y += 1

        return

    def right(self, world):
        if world[self.enemy_y][self.enemy_x + 1] == 2:
            world[self.enemy_y][self.enemy_x + 1] = 3
            world[self.enemy_y][self.enemy_x] = 2
            self.enemy_x += 1

        return

    def defend(self, att, world):
        self.hp -= att - self.dr
        if self.hp == 0:
            world[self.enemy_y][self.enemy_x] = 2
        return

    def potion(self):

        return
