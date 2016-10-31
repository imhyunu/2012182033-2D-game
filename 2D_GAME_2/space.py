from pico2d import*

class Space():
    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2

    ###########################################################################################

    def game_defence(self):
        self.game_state = self.GAME_DEFENCE
        self.frame = 0

    ###########################################################################################

    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING
        self.frame = 1000

    ###########################################################################################

    def game_over(self):
        self.game_state = self.GAME_OVER

    ###########################################################################################

    def __init__(self):
        self.frame = 0

        self.game_state = self.GAME_DEFENCE

        self.game_over_font = load_font('font_file\ENCR10B.TTF', 100)

        self.image = load_image('png_file\space_2.png')

    ###########################################################################################

    def update(self, frame_time):
        pass

    ###########################################################################################

    def draw(self):
        self.image.clip_draw(0, self.frame, 800, 1000, 400, 500)