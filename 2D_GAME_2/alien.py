from pico2d import*
import random
import math

class Alien():
    PIXEL_PER_METTER = (10 / 0.5)

    ALIEN_KPH = 20
    ALIEN_MPM = (ALIEN_KPH * 1000 / 60)
    ALIEN_MPS = (ALIEN_MPM / 60)
    ALIEN_PPS = (ALIEN_MPS * PIXEL_PER_METTER)

    LIFE, DIE = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2

    ###########################################################################################

    def get_bb(self):
        if self.state == self.LIFE:
            return self.x - 25, self._y + 25, self.x + 25, self._y - 25
        else:
            return -99, -99, -99, -99

    ###########################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE

    ###########################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING

    ###########################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ###########################################################################################

    def bump(self):
        self.state = self.DIE

    ###########################################################################################

    def alien_die(self):
        self.state = self.DIE

    ###########################################################################################

    def hp_zero(self):
        if self.hp <= 0: return True
        else: return False

    ###########################################################################################

    def hit(self):
        self.hp -= self.hit_point

    ###########################################################################################

    def go_defence(self):
        if self.y < self.line: return True
        else: return False

    ###########################################################################################

    def get_tower(self, tower):
        self.tower = tower

        rdr = math.pow(tower.x - self.x, 2) + math.pow(tower.y - self.y, 2)

        self.cos = (tower.x - self.x) / math.sqrt(rdr)
        self.sin = (tower.y - self.y) / math.sqrt(rdr)

    ###########################################################################################

    def get_space(self, space):
        self.space = space
        self.line = 750 - space.frame

    ###########################################################################################

    def __init__(self):
        self.x, self.y = random.randint(25, 775), random.randint(1000, 3000)
        self._y = 0
        self.frame = 0
        self.line = 0
        self.cos, self.sin = 0.0, 0.0

        self.hp = 40
        self.hit_point = 10

        self.space = None
        self.tower = None

        self.state = self.LIFE
        self.game_state = self.GAME_SHOOTING

        self.hp_rad_image = load_image('png_file\hp_rad.png')
        self.hp_black_image = load_image('png_file\hp_brack.png')
        self.image = load_image('png_file\stage1_alien.png')

    ###########################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.ALIEN_PPS)

        if self.state == self.LIFE:
            if self.game_state == self.GAME_SHOOTING:
                self.y -= distance

            elif self.game_state == self.GAME_DEFENCE:
                self.x += (self.cos * distance)
                self.y += (self.sin * distance)

    ###########################################################################################

    def draw(self):
        if self.state == self.LIFE:
            self._y = self.y - self.space.frame
            self.image.clip_draw(self.frame, 0, 57, 50, self.x, self._y)

            self.hp_black_image.draw(self.x, self._y + 55)
            self.hp_rad_image.clip_draw_to_origin(0, 0, self.hp, 4, self.x - 20, self._y + 53)