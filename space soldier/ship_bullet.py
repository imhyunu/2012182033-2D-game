from pico2d import *

class Ship_Bullet():
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

    def hit(self):
        self.state = self.NO_SHOT
        self.x, self.y = 0, 0

    def game_over(self):
        self.game_state = self.GAME_OVER

    def get_bb(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if self.state == self.SHOT:
                return self.x - 3, self.y + 7, self.x + 3, self.y - 7
            else:
                return -99, -99, -99, -99
        else:
            return -999, -999, -999, -999

    def it_shot(self):
        if self.state == self.SHOT:
            return False
        elif self.state == self.NO_SHOT:
            return True

    def shot(self, ship):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if self.re_load > 0.2:
                self.ship = ship
                self.x, self.y = ship.x, ship.y
                self.state = self.SHOT
                self.re_load = 0


    ################################################################################################


    def __init__(self):
        self.x, self.y = 0, 0
        self.state = self.NO_SHOT
        self.ship = None
        self.re_load = 1
        self.game_state = self.GAME_STATE_DEFENCE
        self.image = load_image('ship_bullet.png')


    ################################################################################################


    def update(self, frame_time):
        distance = (frame_time * self.BULLET_SPEED_PPS)
        if self.game_state == self.GAME_STATE_SHOOTING:
            self.re_load += frame_time
            if self.state == self.SHOT:
                self.y += distance
                if (self.y - self.ship.y) > 600:
                    self.state = self.NO_SHOT


    ################################################################################################


    def draw(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if self.state == self.SHOT:
                self.image.draw(self.x, self.y)