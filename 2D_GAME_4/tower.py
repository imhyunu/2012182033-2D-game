from pico2d import*

class Tower():
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

    def hp_zero(self):
        if self.hp <= 0: return True
        else: return False

    ###########################################################################################

    def dump(self):
        self.hp -= self.hit_point

    ###########################################################################################

    def get_bb(self):
        return self.x - 45, self.draw_y + 45, self.x + 45, self.draw_y - 45

    ###########################################################################################

    def get_space(self, space):
        self.space = space
        self.draw_y = self.y - self.space.frame

    ##############################################################################################

    def __init__(self):
        self.x, self.y = 400, 80
        self.draw_y = 0

        self.hp = 200
        self.hit_point = 10

        self.space = None

        self.game_state = self.GAME_DEFENCE

        self.image = load_image('png_file\defence_tower.png')

        self.rd_hp_image = load_image('png_file\hp_red_tower.png')
        self.bk_hp_image = load_image('png_file\hp_brack_tower.png')

    ##############################################################################################

    def update(self, frame_time):
        pass

    ##############################################################################################

    def draw(self):
        self.image.draw(self.x, self.draw_y)

        self.bk_hp_image.draw(self.x, self.draw_y - 65)
        self.rd_hp_image.clip_draw_to_origin(0, 0, self.hp, 14, self.x - 100, self.draw_y - 72)