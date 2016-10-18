import math
from pico2d import *

class Soldier_Bullet():
    PIXEL_PER_METER = (10.0 / 0.5)
    BULLET_SPEED_KPH = 100
    BULLET_SPEED_MPM = (BULLET_SPEED_KPH * 1000 / 60)
    BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60)
    BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

    GAME_STATE_DEFENCE, GAME_STATE_SHOOTING, GAME_OVER = 0, 1, 2

    NO_SHOT, SHOT = 0, 1
    NO_UPGRADE, UPGRADE = 0, 1

    def in_ship(self):
        self.game_state = self.GAME_STATE_SHOOTING

    def game_over(self):
        self.game_state = self.GAME_OVER

    def it_shot(self):
        if self.bullet_state == self.SHOT:
            return False
        elif self.bullet_state == self.NO_SHOT:
            return True

    def get_bb(self):
        if self.game_state == self.GAME_STATE_DEFENCE:
            if self.bullet_state == self.SHOT:
                return self.x - 4, self.y + 5, self.x + 4, self.y - 5
            else:
                return -99, -99, -99, -99
        else:
            return -99, -99, -99 ,-99

    def hit(self):
        self.bullet_state = self.NO_SHOT
        self.x, self.y = 0, 0

    def shot(self, parent, x, y):
        if self.game_state == self.GAME_STATE_DEFENCE:
            if self.re_load > 0.3:
                rdr = math.pow((x - parent.x), 2) + math.pow((y - parent.y), 2)
                self.x, self.y = parent.x, parent.y
                self.bullet_state = self.SHOT
                self.parent = parent
                self.re_load = 0
                self.cos = (x - parent.x) / math.sqrt(rdr)
                self.sin = (y - parent.y) / math.sqrt(rdr)

    def bullet_upgrade(self):
        self.upgrade_state = self.UPGRADE

    def __init__(self):
        self.x, self.y = 0, 0
        self.parent = None
        self.re_load = 1
        self.cos = 0
        self.sin = 0
        self.bullet_range = 400
        self.game_state = self.GAME_STATE_DEFENCE
        self.bullet_state = self.NO_SHOT
        self.upgrade_state = self.NO_UPGRADE
        self.image_1 = load_image('bullet_1.png')
        self.image_2 = load_image('bullet_2.png')

    def update(self, frame_time):
        destance = (frame_time * self.BULLET_SPEED_PPS)
        if self.game_state == self.GAME_STATE_DEFENCE:
            self.re_load = self.re_load + frame_time
            if self.bullet_state == self.SHOT:
                self.x += (destance * self.cos)
                self.y += (destance * self.sin)
                num_x = math.pow((self.x - self.parent.x), 2)
                num_y = math.pow((self.y - self.parent.y), 2)

                if math.sqrt(num_x + num_y) > self.bullet_range:
                    self.bullet_state = self.NO_SHOT

    def draw(self):
        if self.game_state == self.GAME_STATE_DEFENCE:
            if self.bullet_state == self.SHOT:
                if self.upgrade_state == self.NO_UPGRADE:
                    self.image_1.draw(self.x, self.y)
                elif self.upgrade_state == self.UPGRADE:
                    self.image_2.draw(self.x, self.y)
