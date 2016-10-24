from pico2d import *
import random

class Alien():
    image = None
    hp_brack_image =None
    hp_rad_image = None

    PIXEL_PER_METER = (10.0 / 0.5)

    AILEN_KPH = 20
    AILEN_MPM = (AILEN_KPH * 1000 / 60)
    AILEN_MPS = (AILEN_MPM / 60)
    AILEN_PPS = (AILEN_MPS * PIXEL_PER_METER)

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2
    GAME_MIDDLE = 3

    MOVE, STOP = 0, 1

    LIFE, DIE = 0, 1

    ############################################################################################

    def bump_soldier(self):
        self.state = self.DIE

    ############################################################################################

    def get_bb(self):
        if self.state == self.LIFE:
            return self.x - 23, self._y + 25, self.x + 23, self._y - 25
        elif self.state == self.DIE:
            return -99, -99, -99, -99

    ############################################################################################

    def hit(self):
        self.hp -= self.hp_hit_point

        if self.hp <= 0:
            self.state = self.DIE

    ############################################################################################

    def get_tower(self, _tower):
        self.tower = _tower

    ############################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ############################################################################################

    def soldier_in_ship(self):
        self.game_state = self.GAME_MIDDLE

    ############################################################################################

    def handle_move(self, distance):
        if self.state == self.LIFE:
            if self.move_state == self.MOVE:
                if self.game_state != self.GAME_OVER:
                    rdr = math.pow((self.x - self.tower.x), 2) + math.pow((self._y - self.tower.draw_y), 2)
                    cos = (int(self.x) - self.tower.x) / math.sqrt(rdr)
                    sin = (int(self._y) - self.tower.draw_y) / math.sqrt(rdr)

                    self.frame_state = (self.frame_state % 10) + 1
                    if self.frame_state == 1:
                        self.frame = (self.frame % 2) + 1

                    self.x -= (distance * cos)
                    self.y -= (distance * sin)

                    self._y = self.y + self.tower.draw_y

    ############################################################################################

    def __init__(self):
        self.x, self.y = random.randint(-100, 900), random.randint(800, 2800)
        self._y = 0
        self.frame = 0
        self.line = 700
        self.frame_state = 0
        self.hp_x, self._hp_y = 0, 0
        self.hp_hit_point = 10
        self.hp = 40

        self.game_state = self.GAME_SHOOTING
        self.move_state = self.MOVE
        self.state = self.LIFE

        self.tower = None

        if Alien.image == None:
            Alien.image = load_image('png_file\_alien_1.png')

        if Alien.hp_brack_image == None:
            Alien.hp_brack_image = load_image('png_file\hp_brack.png')

        if Alien.hp_rad_image == None:
            Alien.hp_rad_image = load_image('png_file\hp_rad.png')

    ############################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.AILEN_PPS)

        self.handle_move(distance)

    ############################################################################################

    def draw(self):
        if self.state == self.LIFE:

            self.image.clip_draw(self.frame, 0, 56, 50, self.x, self._y)

            self.hp_brack_image.draw(self.x, self._y + 30)

            self.hp_x = self.x - ((40 - self.hp) / 2)
            self.hp_y = self._y + 30
            self.hp_rad_image.clip_draw(0, 0, self.hp, 4, self.hp_x, self.hp_y)
