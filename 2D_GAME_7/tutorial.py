from pico2d import*

class Tutorial:
    MOVE_TUTORIAL, BULLET_TUTORIAL, BUMP_TUTORIAL = 0, 1, 2


    def bullet_tutorial(self):
        if self.state == self.BULLET_TUTORIAL:
            return True
        else:
            return False

    def next_tutorial(self):
        if self.state == self.MOVE_TUTORIAL:
            self.state = self.BULLET_TUTORIAL

    def big_next(self):
        self.next_frame_x = 220
        self.next_frame_y = 120

    def small_next(self):
        self.next_frame_x = 200
        self.next_frame_y = 100

    def handle_event(self, event):
        x, y = event.x, 1000 - event.y

        if x >= 800: return False
        if x <= 600: return False
        if y >= 930: return False
        if y <= 870: return False

        return True


    def __init__(self):
        self.state = self.MOVE_TUTORIAL

        self.next_frame_x, self.next_frame_y = 200, 100

        self.esc_image = load_image('png_file\esc_tutorial.png')
        self.move_image = load_image('png_file\move_tutorial.png')
        self.move_sub_image = load_image('png_file\move_tutorial_sub.png')
        self.bullet_sub_image = load_image('png_file\_bullet_tutorial_sub.png')

        self.next_image = load_image('png_file\_next_tutorial.png')


    def update(self, frame_time):
        pass


    def draw(self):
        self.next_image.clip_draw(0, 0, self.next_frame_x, self.next_frame_y, 700, 900)

        self.esc_image.draw(150, 950)
        if self.state == self.MOVE_TUTORIAL:
            self.move_image.draw(400, 200)
            self.move_sub_image.draw(400, 600)

        elif self.state == self.BULLET_TUTORIAL:
            self.bullet_sub_image.draw(400, 600)