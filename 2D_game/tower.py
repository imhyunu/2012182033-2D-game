from pico2d import *

class Tower():
    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2
    GAME_MIDDLE = 3

    ############################################################################################

    def hit(self):
        self.hp -= 10

        if self.hp <= 0:
            self.game_state = self.GAME_OVER

    ############################################################################################

    def get_bb(self):
        return self.x - 45, self.draw_y + 45, self.x + 45, self.draw_y + 45

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

    def get_space(self, _space):
        self.space = _space

    ############################################################################################

    def __init__(self):
        self.x, self.y = 400, 100
        self.draw_y = 0
        self.hp_x, self.hp_y = 0, 0
        self.hp = 200

        self.space = None

        self.game_state = self.GAME_DEFENCE

        self.image = load_image('png_file\defence_tower.png')

        self.hp_brack_image = load_image('png_file\hp_brack_tower.png')
        self.hp_rad_image = load_image('png_file\hp_rad_tower.png')

    ############################################################################################

    def update(self, frame_time):
        pass

    ############################################################################################

    def draw(self):
        self.draw_y = self.y - self.space.frame

        self.image.draw(self.x, self.draw_y)

        self.hp_x = self.x - ((200 - self.hp) / 2)
        self.hp_y = self.draw_y - 70
        self.hp_brack_image.draw(self.x, self.draw_y - 70)
        self.hp_rad_image.clip_draw(0, 0, self.hp, 14, self.hp_x, self.hp_y)