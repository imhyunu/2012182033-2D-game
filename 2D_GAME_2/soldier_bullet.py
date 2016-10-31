from pico2d import*
import math

class Soldier_Bullet():
    PIXEL_PER_METTER = (10 / 0.5)

    BULLET_KPH = 100
    BULLET_MPM = (BULLET_KPH * 1000 / 60)
    BULLET_MPS = (BULLET_MPM / 60)
    BULLET_PPS = (BULLET_MPS * PIXEL_PER_METTER)

    NO_SHOT, SHOT = 0, 1

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

    def what_state(self):
        if self.state == self.NO_SHOT:
            return True
        else:
            return False

    ###########################################################################################

    def get_bb(self):
        if self.state == self.SHOT:
            return self.x - 4, self.y + 5, self.x + 4, self.y - 5
        else:
            return -99, -99, -99, -99

    ###########################################################################################

    def shot(self, soldier, x, y):
        if self.game_state == self.GAME_DEFENCE:
            if self.reload > 0.5:
                rdr = math.pow((x - soldier.x), 2) + math.pow((y - soldier.y), 2)
                self.soldier = soldier
                self.state = self.SHOT
                self.x, self.y = soldier.x, soldier.y
                self.cos = (x - soldier.x) / math.sqrt(rdr)
                self.sin = (y - soldier.y) / math.sqrt(rdr)
                self.reload = 0

    ###########################################################################################

    def __init__(self):
        self.x, self.y = 0, 0
        self.cos, self.sin = 0, 0
        self.reload = 2
        self.range = 400

        self.soldier = None

        self.state = self.NO_SHOT
        self.game_state = self.GAME_DEFENCE

        self.image = load_image('png_file\soldier_bullet.png')

    ###########################################################################################

    def update(self, frame_time):
        distance = (frame_time * self.BULLET_PPS)

        if self.game_state == self.GAME_DEFENCE:
            self.reload += frame_time
            if self.state == self.SHOT:
                self.x += (distance * self.cos)
                self.y += (distance * self.sin)
                num_1 = math.pow((self.x - self.soldier.x ), 2)
                num_2 = math.pow((self.y - self.soldier.y), 2)

                if math.sqrt(num_1 + num_2) > self.range:
                    self.state = self.NO_SHOT

    ###########################################################################################

    def draw(self):
        if self.state == self.SHOT:
            self.image.draw(self.x, self.y)
