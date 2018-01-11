from player import Player
from enemy import Enemy


class Game:
    window_x = int
    window_y = int
    world = []

    player = Player
    enemy = Enemy

    state = 1

    def __init__(self, stdscr=None):
        def initialize_world(x, y):

            room_top = int(y) // 8
            room_bottom = room_top * 7
            room_left = int(x) // 6
            room_right = room_left * 5

            room_left -= 10
            room_right -= 10

            player_y_start = room_top + 3
            player_x_start = room_left + 3

            enemy_y_start = room_bottom - 3
            enemy_x_start = room_right - 3

            info_top = room_top
            info_bottom = room_bottom
            info_left = room_right + 2
            info_right = room_right + 23

            world = []

            # populate world array
            for cord in range(self.window_y):
                world.append([])
            for y in world:
                for x in range(self.window_x):
                    y.append(0)

            # make world view
            for y in range(self.window_y):
                for x in range(self.window_x):
                    if room_bottom > y > room_top:
                        if room_left < x < room_right:
                            world[y][x] = 1
            for y in range(self.window_y):
                for x in range(self.window_x):
                    if room_bottom - 1 > y > room_top + 1:
                        if room_left + 1 < x < room_right - 1:
                            world[y][x] = 2
            # make info pane
            for y in range(self.window_y):
                for x in range(self.window_x):
                    if info_bottom > y > info_top:
                        if info_left < x < info_right:
                            world[y][x] = 1
            for y in range(self.window_y):
                for x in range(self.window_x):
                    if info_bottom - 1 > y > info_top + 1:
                        if info_left + 1 < x < info_right - 1:
                            world[y][x] = 6

            # places hero and enemy in world and instantiates them
            world[player_y_start][player_x_start] = 3
            world[enemy_y_start][enemy_x_start] = 4
            player = Player(player_x_start, player_y_start)
            enemy = Enemy(enemy_x_start, enemy_y_start)

            world[6][60] = 7
            world[6][61] = 9
            world[6][62] = 20
            world[6][63] = 21
            world[6][64] = 20

            return world, player, enemy

        if stdscr:
            self.window_x = stdscr.getmaxyx()[1]
            self.window_y = stdscr.getmaxyx()[0]
            self.world, self.player, self.enemy = initialize_world(self.window_x, self.window_y)
        else:
            self.window_x = 80
            self.window_y = 24
            self.world, self.player, self.enemy = initialize_world(self.window_x, self.window_y)

    def get_window(self):
        view = " "
        for y in self.world:
            for x in y:
                view += str(self.tile_lookup(x))
            # view += " "
        return view

    def get_view(self):
        view = ""
        for y in range(self.window_y):
            for x in range(self.window_x):
                view += self.tile_lookup(self.world[y][x])
        return view

    def tile_lookup(self, key):
        key = int(key)
        if key == 0:
            return "🔲"
        if key == 1:
            return "⬜"
        if key == 2:
            return "⬛"
        if key == 3:
            return "🧔"
        if key == 4:
            return "🧟"
        if key == 5:
            return "💟"
        if key == 6:
            return "  "
        if key == 7:
            return "HP"
        if key == 8:
            return "PT"
        if key == 9:
            return ": "
        if key == 10:
            return " 0"
        if key == 11:
            return " 1"
        if key == 12:
            return " 2"
        if key == 13:
            return " 3"
        if key == 14:
            return " 4"
        if key == 15:
            return " 5"
        if key == 16:
            return " 6"
        if key == 17:
            return " 7"
        if key == 18:
            return " 8"
        if key == 19:
            return " 9"
        if key == 20:
            return "10"
        if key == 21:
            return " /"
        return "?"

    def do_turn(self, key_press):
        # print(key_press)
        if key_press == 113:
            return 0
        if key_press == 119:   # up
            self.player.up(self.world, self.enemy)
            # print("up")
        if key_press == 97:    # left
            self.player.left(self.world, self.enemy)
            # print("left")
        if key_press == 115:   # down
            self.player.down(self.world, self.enemy)
            # print("down")
        if key_press == 100:   # right
            self.player.right(self.world, self.enemy)
            # print("right")
        if key_press == 32:   # potion
            self.player.potion(self.world)
            # print("potion")

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
