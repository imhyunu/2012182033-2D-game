import math

from pico2d import *

import game_framework
import menu_state

class Kpu_logo():
    def __init__(self):
        self.x, self.y = 200, 0
        self.r = 200
        self.angle = 0
        self.radian_angle = 0
        self.image = load_image('kpu_logo.png')

    def update(self, frame_time):
        self.angle += (500 * frame_time)
        if self.angle >= 360:
            self.angle = 0
        self.radian_angle = math.radians(self.angle)
        self.x = (400 + (self.r * math.cos(self.radian_angle)))
        self.y = (300 + (self.r * math.sin(self.radian_angle)))
        self.r -= (200 * frame_time)
        if self.r <= 0:
            self.r = 0
            game_framework.change_state(menu_state)

    def draw(self):
        self.image.draw(self.x, self.y)