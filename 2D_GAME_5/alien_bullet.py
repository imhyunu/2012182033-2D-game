from pico2d import*
import math

class Alien_Bullet:
    image = None

    PIXEL_PER_METTER = (10 / 0.5)

    BULLET_KPH = 80
    BULLET_MPM = (BULLET_KPH * 1000 / 60)
    BULLET_MPS = (BULLET_MPM / 60)
    BULLET_PPS = (BULLET_MPS * PIXEL_PER_METTER)

    NO_SHOT, SHOT = 0, 1

    def what_state(self):
        if self.state == self.NO_SHOT:
            return True
        else: return False

    def shot(self, soldier, alien):
        self.state = self.SHOT

        self.alien = alien

        self.x = alien.x
        self.y = alien.draw_y

        rdr = math.pow(soldier.x - alien.x, 2) + math.pow(soldier.y - alien.draw_y, 2)

        self.cos = (soldier.x - alien.x) / math.sqrt(rdr)
        self.sin = (soldier.y - alien.draw_y) / math.sqrt(rdr)

    def __init__(self):
        self.x, self.y = 0, 0
        self.range = 800

        self.cos, self.sin = 0, 0

        self.alien = None

        self.state = self.NO_SHOT

        if Alien_Bullet.image == None:
            Alien_Bullet.image = load_image('png_file\_alien_bullet.png')

    def update(self, frame_time):
        distance = (frame_time * self.BULLET_PPS)

        if self.state == self.SHOT:
            self.x += (distance * self.cos)
            self.y += (distance * self.sin)

            rdr = math.pow(self.alien.x - self.x, 2) + math.pow(self.alien.draw_y - self.y, 2)

            if math.sqrt(rdr) >= self.range:
                self.state = self.NO_SHOT

    def draw(self):
        if self.state == self.SHOT:
            self.image.draw(self.x, self.y)