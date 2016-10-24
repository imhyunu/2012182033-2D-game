from pico2d import *

class Space_World():

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2
    GAME_MIDDLE = 3

    ############################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE
        self.frame = 10

    ############################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ############################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING

    ############################################################################################

    def what_frame(self):
        if self.frame > 800:
            self.frame = 800
            return True
        else:
            return  False

    ############################################################################################

    def soldier_in_ship(self):
        self.game_state = self.GAME_MIDDLE

    ############################################################################################

    def __init__(self):
        self.frame = 10

        self.game_state = self.GAME_DEFENCE

        self.image = load_image('png_file\space_2.png')

    ############################################################################################

    def update(self, frame_time):
        if self.game_state == self.GAME_MIDDLE:
            self.frame += 10

    ############################################################################################

    def draw(self):
        self.image.clip_draw(0, self.frame, 800, 600, 400, 300)