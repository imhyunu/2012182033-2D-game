from pico2d import*
import random
import math

class Alien():
    PIXEL_PER_METTER = (10 / 0.5)

    ALIEN_KPH = 25
    ALIEN_MPM = (ALIEN_KPH * 1000 / 60)
    ALIEN_MPS = (ALIEN_MPM / 60)
    ALLEN_PPS = (ALIEN_MPS * PIXEL_PER_METTER)

    LIFE, DIE = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2

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

    def his_die(self):
        self.state = self.DIE

    ###########################################################################################

    def dump(self):
        self.state = self.DIE

    ###########################################################################################

    def hp_zero(self):
        if self.hp <= 0: return True
        else: return False

    ###########################################################################################

    def hit(self):
        self.hp -= self.hit_point

    ###########################################################################################

    def get_bb(self):
        if self.state == self.LIFE:
            return self.x - 25, self.draw_y + 25, self.x + 25, self.draw_y - 25
        else:
            return -99, -99, -99, -99

    ###########################################################################################

    def get_tower(self, tower):
        self.tower = tower
        rdr = math.pow((self.x - self.tower.x), 2) + math.pow((self.draw_y - self.tower.draw_y), 2)
        self.cos = (self.tower.x - self.x) / math.sqrt(rdr)
        self.sin = (self.tower.draw_y - self.draw_y) / math.sqrt(rdr)

    ###########################################################################################

    def get_space(self, space):
        self.space = space
        self.draw_y = self.y - self.space.frame
        self.line = 750 - self.space.frame

    ###########################################################################################

    def go_tower(self):
        if self.draw_y < self.line: return True
        else: return False

    ###########################################################################################

    def handle_move(self, distance):
        if self.game_state == self.GAME_SHOOTING:
            self.y -= distance

        elif self.game_state == self.GAME_DEFENCE:
            self.x += (self.cos * distance)
            self.y += (self.sin * distance)

    ###########################################################################################

    def __init__(self):
        self.x, self.y = random.randint(50, 750), random.randint(1500, 3000)
        self.draw_y = 0
        self.frame = 0
        self.line = 750
        self.cos, self.sin = 0, 0

        self.hp = 40
        self.hit_point = 20

        self.space = None
        self.tower = None

        self.state = self.LIFE
        self.game_state = self.GAME_SHOOTING

        self.RED_hp_image = load_image('png_file\hp_red_alien.png')
        self.BLACK_hp_image = load_image('png_file\hp_brack_alien.png')

        self.image = load_image('png_file\stage1_alien.png')

    ###########################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.ALLEN_PPS)

        if self.state == self.LIFE:
            self.handle_move(distance)

    ###########################################################################################

    def draw(self):
        if self.state == self.LIFE:
            self.image.clip_draw(57 * self.frame, 0, 57, 50, self.x, self.draw_y)
            self.BLACK_hp_image.draw(self.x, self.draw_y + 30)
            self.RED_hp_image.clip_draw_to_origin(0, 0, self.hp, 4, self.x - 20, self.draw_y + 28)