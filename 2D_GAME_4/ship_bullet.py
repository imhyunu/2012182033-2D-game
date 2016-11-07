from pico2d import *

class Ship_Bullet():
    PIXEL_PER_METTER = (10 / 0.5)

    BULLET_KPH = 120
    BULLET_MPM = (BULLET_KPH * 1000 / 60)
    BULLET_MPS = (BULLET_MPM / 60)
    BULLET_PPS = (BULLET_MPS * PIXEL_PER_METTER)

    NO_SHOT, SHOT = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2

    ###########################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE
        self.state = self.NO_SHOT

    ###########################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING

    ###########################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ###########################################################################################

    def hit(self):
        self.state = self.NO_SHOT

    ###########################################################################################

    def get_bb(self):
        if self.state == self.SHOT:
            return self.x - 4, self.y + 5, self.x + 4, self.y - 5
        else:
            return -99, -99, -99, -99

    ###########################################################################################

    def what_state(self):
        if self.state == self.NO_SHOT:
            return True
        else:
            return False

    ###########################################################################################

    def shot(self, soldier):
        if self.game_state == self.GAME_SHOOTING:
            self.soldier = soldier
            self.state = self.SHOT
            self.x, self.y = self.soldier.x, self.soldier.y

    ###########################################################################################

    def __init__(self):
        self.x, self.y = 0, 0
        self.range = 1000

        self.soldier = None

        self.state = self.NO_SHOT
        self.game_state = self.GAME_DEFENCE

        self.image = load_image('png_file\ship_bullet.png')

    ###########################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.BULLET_PPS)

        if self.game_state == self.GAME_SHOOTING:
            if self.state == self.SHOT:
                self.y += distance

                if (self.y - self.soldier.x) > self.range:
                    self.state = self.NO_SHOT

    ###########################################################################################

    def draw(self):
        if self.state == self.SHOT:
            self.image.draw(self.x, self.y)