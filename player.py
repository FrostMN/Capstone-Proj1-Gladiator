class Player:
    hp = int
    attack = int
    potions = int
    dr = int
    player_x = int
    player_y = int

    def __init__(self, x, y):
        self.hp = 20
        self.potions = 13
        self.attack = 2
        self.dr = 1
        self.player_x = x
        self.player_y = y

    def up(self, world, enemy):
        if world[self.player_y - 1][self.player_x] == 2:
            world[self.player_y - 1][self.player_x] = 3
            world[self.player_y][self.player_x] = 2
            self.player_y -= 1
        if world[self.player_y - 1][self.player_x] == 4:
            enemy.defend(self.attack, world)
            self.defend(world, enemy.attack)
        return

    def left(self, world, enemy):
        if world[self.player_y][self.player_x - 1] == 2:
            world[self.player_y][self.player_x - 1] = 3
            world[self.player_y][self.player_x] = 2
            self.player_x -= 1
        if world[self.player_y][self.player_x - 1] == 4:
            enemy.defend(self.attack, world)
            self.defend(world, enemy.attack)
        return

    def down(self, world, enemy):
        if world[self.player_y + 1][self.player_x] == 2:
            world[self.player_y + 1][self.player_x] = 3
            world[self.player_y][self.player_x] = 2
            self.player_y += 1
        if world[self.player_y + 1][self.player_x] == 4:
            enemy.defend(self.attack, world)
            self.defend(world, enemy.attack)
        return

    def right(self, world, enemy):
        if world[self.player_y][self.player_x + 1] == 2:
            world[self.player_y][self.player_x + 1] = 3
            world[self.player_y][self.player_x] = 2
            self.player_x += 1
        if world[self.player_y][self.player_x + 1] == 4:
            enemy.defend(self.attack, world)
            self.defend(world, enemy.attack)
        return

    def potion(self, world):
        if self.potions > 10:
            self.potions -= 1
            self.hp = 10
        return

    def defend(self, world, att):
        self.hp -= att - self.dr
        world[6][62] = self.hp
        if self.hp == 10:
            world[self.player_y][self.player_x] = 2
        return
