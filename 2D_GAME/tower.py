from pico2d import*

class Tower():
    ###########################################################################################

    def get_space(self, space):
        self.space = space

    ##############################################################################################

    def __init__(self):
        self.x, self.y = 400, 80

        self.hp = 200
        self.hit_point = 10

        self.space = None

        self.image = load_image('png_file\defence_tower.png')

        self.rd_hp_image = load_image('png_file\hp_rad_tower.png')
        self.bk_hp_image = load_image('png_file\hp_brack_tower.png')

    ##############################################################################################

    def update(self, frame_time):
        pass

    ##############################################################################################

    def draw(self):
        y = self.y - self.space.frame
        self.image.draw(self.x, y)

        self.bk_hp_image.draw(self.x, y - 65)
        self.rd_hp_image.clip_draw_to_origin(0, 0, self.hp, 14, self.x - 100, y - 72)