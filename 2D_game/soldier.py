from pico2d import *

class Soldier():
    PIXEL_PER_METER = (10.0 / 0.5)

    SOLDIER_KPH = 25
    SOLDIER_MPM = (SOLDIER_KPH * 1000 / 60)
    SOLDIER_MPS = (SOLDIER_MPM / 60)
    SOLDIER_PPS = (SOLDIER_MPS * PIXEL_PER_METER)

    SHIP_KPH = 60
    SHIP_MPM = (SHIP_KPH * 1000 / 60)
    SHIP_MPS = (SHIP_MPM / 60)
    SHIP_PPS = (SHIP_MPS * PIXEL_PER_METER)

    UP_MOVE, DOWN_MOVE, RIGHT_MOVE, LEFT_MOVE, STOP = 0, 1, 2, 3, 4
    UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT = 5, 6, 7, 8
    LEFT_UP_RIGHT, LEFT_DOWN_RIGHT = 9, 10
    LEFT_RIGHT = 11

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1 ,2
    GAME_MIDDLE_SHOOTING, GAME_MIDDLE_DEFENCE = 3, 4

    ############################################################################################

    def what_hp(self):
        if self.hp <= 0: return True
        if self.shild_o_state < 0.25: return True

        return False

    ############################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ############################################################################################

    def hit(self):
        if self.game_state == self.GAME_DEFENCE:
            self.hp -= self.hit_point
            self.hp_y -= (self.hit_point / 2)

        elif self.game_state == self.GAME_SHOOTING:
            self.shild_o_state = self.shild_o_state * 0.5

    ############################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING

    ############################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE

    ############################################################################################

    def get_space(self, _space):
        self.space = _space

    ############################################################################################

    def in_home(self):
        if self.game_state != self.GAME_DEFENCE: return False
        if self.x > 780: return False
        if self.x < 720: return False
        if self.y > 150: return False
        if self.y < 50: return False

        return True

    ############################################################################################

    def out_ship(self, x, y):
        if self.game_state != self.GAME_SHOOTING: return False
        if x > 780: return False
        if x < 720: return False
        if y > 50: return False
        if y < 20: return False

        return True

    ############################################################################################

    def soldier_in_ship(self):
        self.game_state = self.GAME_MIDDLE_SHOOTING
        self.soldier_state = self.STOP

    ############################################################################################

    def get_bb(self):
        if self.game_state != self.GAME_OVER:
            return self.x - 15, self.y + 20, self.x + 15, self.y - 20
        else:
            return -99, -99, -99, -99

    ############################################################################################

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                if self.soldier_state == self.STOP:
                    self.soldier_state = self.UP_MOVE

                elif self.soldier_state == self.LEFT_MOVE:
                    self.soldier_state = self.UP_LEFT

                elif self.soldier_state == self.RIGHT_MOVE:
                    self.soldier_state = self.UP_RIGHT

                elif self.soldier_state == self.LEFT_RIGHT:
                    self.soldier_state = self.LEFT_UP_RIGHT

                self.frame_y = 3

            if event.key == SDLK_s:
                if self.soldier_state == self.STOP:
                    self.soldier_state = self.DOWN_MOVE

                elif self.soldier_state == self.LEFT_MOVE:
                    self.soldier_state = self.DOWN_LEFT

                elif self.soldier_state == self.RIGHT_MOVE:
                    self.soldier_state = self.DOWN_RIGHT

                elif self.soldier_state == self.LEFT_RIGHT:
                    self.soldier_state = self.LEFT_DOWN_RIGHT

                self.frame_y = 1

            if event.key == SDLK_a:
                if self.soldier_state == self.STOP:
                    self.soldier_state = self.LEFT_MOVE

                elif self.soldier_state == self.UP_MOVE:
                    self.soldier_state = self.UP_LEFT

                elif self.soldier_state == self.DOWN_MOVE:
                    self.soldier_state = self.DOWN_LEFT

                elif self.soldier_state == self.UP_RIGHT:
                    self.soldier_state = self.LEFT_UP_RIGHT

                elif self.soldier_state == self.DOWN_RIGHT:
                    self.soldier_state = self.LEFT_DOWN_RIGHT

                elif self.soldier_state == self.RIGHT_MOVE:
                    self.soldier_state = self.LEFT_RIGHT

                self.frame_y = 0

            if event.key == SDLK_d:
                if self.soldier_state == self.STOP:
                    self.soldier_state = self.RIGHT_MOVE

                elif self.soldier_state == self.UP_MOVE:
                    self.soldier_state = self.UP_RIGHT

                elif self.soldier_state == self.DOWN_MOVE:
                    self.soldier_state = self.DOWN_RIGHT

                elif self.soldier_state == self.UP_LEFT:
                    self.soldier_state = self.LEFT_UP_RIGHT

                elif self.soldier_state == self.DOWN_LEFT:
                    self.soldier_state = self.LEFT_DOWN_RIGHT

                elif self.soldier_state == self.LEFT_MOVE:
                    self.soldier_state = self.LEFT_RIGHT

                self.frame_y = 2

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                if self.soldier_state == self.UP_MOVE:
                    self.soldier_state = self.STOP

                elif self.soldier_state == self.UP_LEFT:
                    self.soldier_state = self.LEFT_MOVE
                    self.frame_y = 0

                elif self.soldier_state == self.UP_RIGHT:
                    self.soldier_state = self.RIGHT_MOVE
                    self.frame_y = 2

                elif self.soldier_state == self.LEFT_UP_RIGHT:
                    self.soldier_state = self.LEFT_RIGHT

            if event.key == SDLK_s:
                if self.soldier_state == self.DOWN_MOVE:
                    self.soldier_state = self.STOP

                elif self.soldier_state == self.DOWN_LEFT:
                    self.soldier_state = self.LEFT_MOVE
                    self.frame_y = 0

                elif self.soldier_state == self.DOWN_RIGHT:
                    self.soldier_state = self.RIGHT_MOVE
                    self.frame_y = 2

                elif self.soldier_state == self.LEFT_DOWN_RIGHT:
                    self.soldier_state = self.LEFT_RIGHT

            if event.key == SDLK_a:
                if self.soldier_state == self.LEFT_MOVE:
                    self.soldier_state = self.STOP

                elif self.soldier_state == self.UP_LEFT:
                    self.soldier_state = self.UP_MOVE
                    self.frame_y = 3

                elif self.soldier_state == self.DOWN_LEFT:
                    self.soldier_state = self.DOWN_MOVE
                    self.frame_y = 1

                elif self.soldier_state == self.LEFT_RIGHT:
                    self.soldier_state = self.RIGHT_MOVE
                    self.frame_y = 2

                elif self.soldier_state == self.LEFT_UP_RIGHT:
                    self.soldier_state = self.UP_RIGHT
                    self.frame_y = 2

                elif self.soldier_state == self.LEFT_DOWN_RIGHT:
                    self.soldier_state = self.DOWN_RIGHT
                    self.frame_y = 2

            if event.key == SDLK_d:
                if self.soldier_state == self.RIGHT_MOVE:
                    self.soldier_state = self.STOP

                elif self.soldier_state == self.UP_RIGHT:
                    self.soldier_state = self.UP_MOVE
                    self.frame_y = 3

                elif self.soldier_state == self.DOWN_RIGHT:
                    self.soldier_state = self.DOWN_MOVE
                    self.frame_y = 1

                elif self.soldier_state == self.LEFT_RIGHT:
                    self.soldier_state = self.LEFT_MOVE
                    self.frame_y = 0

                elif self.soldier_state == self.LEFT_UP_RIGHT:
                    self.soldier_state = self.UP_LEFT
                    self.frame_y = 0

                elif self.soldier_state == self.LEFT_DOWN_RIGHT:
                    self.soldier_state = self.DOWN_LEFT
                    self.frame_y = 0

    ############################################################################################

    def handle_move(self, distance):
        if self.soldier_state == self.UP_MOVE:
            self.y += distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.DOWN_MOVE:
            self.y -= distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.RIGHT_MOVE:
            self.x += distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.LEFT_MOVE:
            self.x -= distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.UP_RIGHT:
            self.x += (distance * math.cos(math.radians(45)))
            self.y += (distance * math.sin(math.radians(45)))
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.UP_LEFT:
            self.x -= (distance * math.cos(math.radians(45)))
            self.y += (distance * math.sin(math.radians(45)))
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.DOWN_RIGHT:
            self.x += (distance * math.cos(math.radians(45)))
            self.y -= (distance * math.sin(math.radians(45)))
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.DOWN_LEFT:
            self.x -= (distance * math.cos(math.radians(45)))
            self.y -= (distance * math.sin(math.radians(45)))
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.LEFT_UP_RIGHT:
            self.y += distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

        elif self.soldier_state == self.LEFT_DOWN_RIGHT:
            self.y -= distance
            self.move_state = (self.move_state % 10) + 1
            if self.move_state == 3:
                self.frame_x = (self.frame_x % 2) + 1

    ############################################################################################

    def __init__(self):
        self.x, self.y = 400, 200
        self.frame_x, self.frame_y = 0, 3
        self.move_state = 0
        self.home_y = 110

        self.hp = 200
        self.hp_y = 110
        self.hit_point = 20
        self.shild_state = 100
        self.shild_o_state = 0.5

        self.space = None

        self.soldier_state = self.STOP
        self.game_state = self.GAME_DEFENCE

        self.font = load_font('font_file\ENCR10B.TTF', 100)

        self.image = load_image('png_file\soldier.png')
        self.ship_image = load_image('png_file\ship.png')
        self.hp_black = load_image('png_file\soldier_hp_black.png')
        self.hp_rad = load_image('png_file\soldier_hp_rad.png')
        self.hp_green = load_image('png_file\ship_shild.png')
        self.ship_home  = load_image('png_file\ship_home.png')

    ############################################################################################

    def update(self, frame_time):
        if self.game_state == self.GAME_DEFENCE:
            distance = (frame_time * self.SOLDIER_PPS)

        elif self.game_state == self.GAME_SHOOTING:
            distance = (frame_time * self.SHIP_PPS)

        if (self.game_state != self.GAME_MIDDLE_SHOOTING) and (self.game_state != self.GAME_OVER):
            self.handle_move(distance)

    ############################################################################################

    def draw(self):
        if self.game_state == self.GAME_OVER:
            self.font.draw(150, 300, 'You Die!!', (255, 0, 0))

        else:
            if self.game_state == self.GAME_DEFENCE:
                self.image.clip_draw(self.frame_x * 30, self.frame_y * 40, 30, 40, self.x, self.y)

                self.hp_black.draw(60, 110)
                self.hp_rad.clip_draw(0, 0, 100, self.hp, 60, self.hp_y)

            elif self.game_state == self.GAME_MIDDLE_SHOOTING:
                self.ship_image.draw(self.x, self.y)

            elif self.game_state == self.GAME_SHOOTING:
                self.ship_image.draw(self.x, self.y)
                self.hp_green.opacify(self.shild_o_state)
                self.hp_green.rotate_draw(0, self.x, self.y, self.shild_state, self.shild_state)

            self.ship_home.draw(750, self.home_y - self.space.frame)