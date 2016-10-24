from pico2d import *

class Ship_Bullet():
    image = None

    PIXEL_PER_METER = (10.0 / 0.5)
    BULLET_SPEED_KPH = 150
    BULLET_SPEED_MPM = (BULLET_SPEED_KPH * 1000 / 60)
    BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60)
    BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

    NO_SHOT, SHOT = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2
    GAME_MIDDLE = 3

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
        return self.x - 3, self.y + 7, self.x + 3, self.y - 7

    ############################################################################################

    def what_state(self):
        if self.state == self.SHOT:
            return False
        elif self.state == self.NO_SHOT:
            return True

    ############################################################################################

    def shot(self, ship):
        if self.game_state == self.GAME_SHOOTING:
            if self.reload > 0.4:
                self.x, self.y = ship.x, ship.y + 50
                self.state = self.SHOT
                self.re_load = 0

    ############################################################################################

    def __init__(self):
        self.x, self.y = 0, 0
        self.reload = 1
        self.range = 800
        self.cos, self.sin = 0, 0

        self.game_state = self.GAME_DEFENCE
        self.state = self.NO_SHOT

        if Ship_Bullet.image == None:
            Ship_Bullet.image = load_image('png_file\ship_bullet.png')

    ############################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.BULLET_SPEED_PPS)

        if self.game_state == self.GAME_SHOOTING:
            self.reload += frame_time

            if self.state == self.SHOT:
                self.y += distance

        if self.y > self.range:
            self.state = self.NO_SHOT

    ############################################################################################

    def draw(self):
        if self.state == self.SHOT:
            self.image.draw(self.x, self.y)