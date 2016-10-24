from pico2d import *
import math

class Soldier_Bullet():
    image = None

    PIXEL_PER_METER = (10.0 / 0.5)
    BULLET_SPEED_KPH = 100
    BULLET_SPEED_MPM = (BULLET_SPEED_KPH * 1000 / 60)
    BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60)
    BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

    NO_SHOT, SHOT = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2
    GAME_MIDDLE = 3

    ############################################################################################

    def hit(self):
        self.state = self.NO_SHOT

    ############################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE

    ############################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ############################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING

    ############################################################################################

    def soldier_in_ship(self):
        self.game_state = self.GAME_MIDDLE

    ############################################################################################

    def get_bb(self):
        if self.state == self.SHOT:
            return self.x - 4, self.y + 5, self.x + 4, self.y - 5
        elif self.state == self.NO_SHOT:
            return -99, -99, -99, -99

    ############################################################################################

    def what_state(self):
        if self.state == self.SHOT:
            return False
        elif self.state == self.NO_SHOT:
            return True

    ############################################################################################

    def shot(self, soldier, x, y):
        if self.game_state == self.GAME_DEFENCE:
            if self.reload > 0.4:
                rdr = math.pow((x - soldier.x), 2) + math.pow((y - soldier.y), 2)
                self.x, self.y = soldier.x, soldier.y
                self.parent = soldier
                self.state = self.SHOT
                self.re_load = 0
                self.cos = (x - soldier.x) / math.sqrt(rdr)
                self.sin = (y - soldier.y) / math.sqrt(rdr)

    ############################################################################################

    def __init__(self):
        self.x, self.y = 0, 0
        self.reload = 0
        self.cos, self.sin = 0, 0
        self.bullet_range = 400

        self.parent = None

        self.state = self.NO_SHOT
        self.game_state = self.GAME_DEFENCE

        if Soldier_Bullet.image == None:
            Soldier_Bullet.image = load_image('png_file\soldier_bullet.png')

    ############################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.BULLET_SPEED_PPS)

        if self.game_state == self.GAME_DEFENCE:
            self.reload += frame_time

            if self.state == self.SHOT:
                self.x += (distance * self.cos)
                self.y += (distance * self.sin)
                num_x = math.pow((self.x - self.parent.x), 2)
                num_y = math.pow((self.y - self.parent.y), 2)

                if math.sqrt(num_x + num_y) > self.bullet_range:
                    self.state = self.NO_SHOT

    ############################################################################################

    def draw(self):
        if self.state == self.SHOT:
            self.image.draw(self.x, self.y)