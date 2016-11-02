from pico2d import*
import math

class Soldier():
    PIXEL_PER_METTER = (10 / 0.5)

    SOLDIER_KPH = 25
    SOLDIER_MPM = (SOLDIER_KPH * 1000 / 60)
    SOLDIER_MPS = (SOLDIER_MPM / 60)
    SOLDIER_PPS = (SOLDIER_MPS * PIXEL_PER_METTER)

    SHIP_KPH = 50
    SHIP_MPM = (SHIP_KPH * 1000 / 60)
    SHIP_MPS = (SHIP_MPM / 60)
    SHIP_PPS = (SHIP_MPS * PIXEL_PER_METTER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    STAND, UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3, 4
    UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, LEFT_RIGHT = 5, 6, 7, 8, 9
    LEFT_UP_RIGHT, LEFT_DOWN_RIGHT =  10, 11

    NO_SHOT, SHOT = 0, 1

    GAME_DEFENCE, GAME_SHOOTING, GAME_OVER = 0, 1, 2

    ###########################################################################################


    def game_defence(self):
        self.game_state = self.GAME_DEFENCE
        self.x, self.y = 740, 600


    ###########################################################################################


    def game_shooting(self):
        self.game_state = self.GAME_SHOOTING
        self.x, self.y = self.home_x, self.home_y


    ###########################################################################################


    def game_over(self):
        self.game_state = self.GAME_OVER


    ###########################################################################################


    def shild_break(self):
        if self.game_state != self.GAME_SHOOTING: return False
        if self.shild <= 0: return True
        else:return False


    ###########################################################################################


    def hp_zero(self):
        if self.game_state == self.GAME_DEFENCE:
            if self.hp <= 0: return True
        elif self.game_state == self.GAME_SHOOTING:
            if self.shild < 0: return True
        else: return False


    ###########################################################################################


    def hit(self):
        if self.game_state == self.GAME_DEFENCE:
            self.hp -= self.hit_point
        elif self.game_state == self.GAME_SHOOTING:
            if self.shild > 0:
                self.shild /= 2
                if self.shild <= 0.125:
                    self.shild = 0
            else:
                self.shild -= 1


    ###########################################################################################


    def in_go_defence(self):
        if self.game_state != self.GAME_SHOOTING: return False
        if self.x > (self.home_x + 50): return False
        if self.x < (self.home_x - 50): return False
        if self.y > (self.home_y + 50): return False
        if self.y < (self.home_y - 50): return False

        return True


    ###########################################################################################


    def in_home(self):
        if self.game_state != self.GAME_DEFENCE: return False
        if self.x > (self.home_x + 30): return False
        if self.x < (self.home_x - 30): return False
        if self.y > (self.home_y + 60): return False
        if self.y < (self.home_y - 60): return False

        return True


    ###########################################################################################


    def get_space(self, space):
        self.space = space
        self.home_draw_y = self.home_y - self.space.frame


    ###########################################################################################


    def get_bb(self):
        if self.game_state == self.GAME_DEFENCE:
            return self.x - 12, self.y + 18, self.x + 12, self.y - 18
        elif self.game_state == self.GAME_SHOOTING:
            return self.x - 25, self.y + 25, self.x + 25, self.y - 25
        else:
            return -99, -99, -99, -99


    ###########################################################################################


    def it_shot(self):
        if self.bullet_state == self.SHOT:
            return True
        else:
            return False


    ###########################################################################################


    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                if self.state == self.STAND:
                    self.state = self.UP
                elif self.state == self.LEFT:
                    self.state = self.UP_LEFT
                elif self.state == self.RIGHT:
                    self.state = self.UP_RIGHT
                elif self.state == self.LEFT_RIGHT:
                    self.state = self.LEFT_UP_RIGHT
                self.frame_y = 3

            elif event.key == SDLK_s:
                if self.state == self.STAND:
                    self.state = self.DOWN
                elif self.state == self.LEFT:
                    self.state = self.DOWN_LEFT
                elif self.state == self.RIGHT:
                    self.state = self.DOWN_RIGHT
                elif self.state == self.LEFT_RIGHT:
                    self.state = self.LEFT_DOWN_RIGHT
                self.frame_y = 1

            elif event.key == SDLK_a:
                if self.state == self.STAND:
                    self.state = self.LEFT
                elif self.state == self.UP:
                    self.state = self.UP_LEFT
                elif self.state == self.DOWN:
                    self.state = self.DOWN_LEFT
                elif self.state == self.RIGHT:
                    self.state = self.LEFT_RIGHT
                elif self.state == self.UP_RIGHT:
                    self.state = self.LEFT_UP_RIGHT
                elif self.state == self.DOWN_RIGHT:
                    self.state = self.LEFT_DOWN_RIGHT
                self.frame_y = 0

            elif event.key == SDLK_d:
                if self.state == self.STAND:
                    self.state = self.RIGHT
                elif self.state == self.UP:
                    self.state = self.UP_RIGHT
                elif self.state == self.DOWN:
                    self.state = self.DOWN_RIGHT
                elif self.state == self.LEFT:
                    self.state = self.LEFT_RIGHT
                elif self.state == self.UP_LEFT:
                    self.state = self.LEFT_UP_RIGHT
                elif self.state == self.DOWN_LEFT:
                    self.state = self.LEFT_DOWN_RIGHT
                self.frame_y = 2

            elif event.key == SDLK_SPACE:
                pass

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                if self.state == self.UP:
                    self.state = self.STAND
                elif self.state == self.UP_LEFT:
                    self.state = self.LEFT
                    self.frame_y = 0
                elif self.state == self.UP_RIGHT:
                    self.state = self.RIGHT
                    self.frame_y = 2
                elif self.state == self.LEFT_UP_RIGHT:
                    self.state = self.LEFT_RIGHT

            elif event.key == SDLK_s:
                if self.state == self.DOWN:
                    self.state = self.STAND
                elif self.state == self.DOWN_LEFT:
                    self.state = self.LEFT
                    self.frame_y = 0
                elif self.state == self.DOWN_RIGHT:
                    self.state = self.RIGHT
                    self.frame_y = 2
                elif self.state == self.LEFT_DOWN_RIGHT:
                    self.state = self.LEFT_RIGHT

            elif event.key == SDLK_a:
                if self.state == self.LEFT:
                    self.state = self.STAND
                elif self.state == self.UP_LEFT:
                    self.state = self.UP
                    self.frame_y = 3
                elif self.state == self.DOWN_LEFT:
                    self.state = self.DOWN
                    self.frame_y = 1
                elif self.state == self.LEFT_RIGHT:
                    self.state = self.RIGHT
                    self.frame_y = 2
                elif self.state == self.LEFT_UP_RIGHT:
                    self.state = self.UP_RIGHT
                    self.frame_y = 2
                elif self.state == self.LEFT_DOWN_RIGHT:
                    self.state = self.DOWN_RIGHT
                    self.frame_y = 2

            elif event.key == SDLK_d:
                if self.state == self.RIGHT:
                    self.state = self.STAND
                elif self.state == self.UP_RIGHT:
                    self.state = self.UP
                    self.frame_y = 3
                elif self.state == self.DOWN_RIGHT:
                    self.state = self.DOWN
                    self.frame_y = 1
                elif self.state == self.LEFT_RIGHT:
                    self.state = self.LEFT
                    self.frame_y = 0
                elif self.state == self.LEFT_UP_RIGHT:
                    self.state = self.UP_LEFT
                    self.frame_y = 0
                elif self.state == self.LEFT_DOWN_RIGHT:
                    self.state = self.DOWN_LEFT
                    self.frame_y = 0

            elif event.key == SDLK_SPACE:
                pass


    ###########################################################################################


    def handle_move(self, distance, total_frame):
        if self.state != self.STAND:
            self.frame_x = int(total_frame) % 3

        if self.state in (self.UP, self.LEFT_UP_RIGHT):
            self.y += distance

        elif self.state in (self.DOWN, self.LEFT_DOWN_RIGHT):
            self.y -= distance

        elif self.state == self.LEFT:
            self.x -= distance

        elif self.state == self.RIGHT:
            self.x += distance

        elif self.state == self.UP_LEFT:
            self.x -= (distance * math.cos(math.radians(45)))
            self.y += (distance * math.sin(math.radians(45)))

        elif self.state == self.UP_RIGHT:
            self.x += (distance * math.cos(math.radians(45)))
            self.y += (distance * math.sin(math.radians(45)))

        elif self.state == self.DOWN_LEFT:
            self.x -= (distance * math.cos(math.radians(45)))
            self.y -= (distance * math.sin(math.radians(45)))

        elif self.state == self.DOWN_RIGHT:
            self.x += (distance * math.cos(math.radians(45)))
            self.y -= (distance * math.sin(math.radians(45)))

        if self.game_state == self.GAME_DEFENCE:
            if self.x < 15:
                self.x = 15

            if self.x > 785:
                self.x = 785

            if self.y > 630:
                self.y = 630

            if self.y < 20:
                self.y = 20

        elif self.game_state == self.GAME_SHOOTING:
            if self.x < 15:
                self.x = 15

            if self.x > 785:
                self.x = 785

            if self.y < 20:
                self.y = 20

            if self.y > 980:
                self.y = 980


    ###########################################################################################


    def __init__(self):
        self.x, self.y = 400, 200
        self.frame_x, self.frame_y = 0, 3
        self.total_frame = 0

        self.home_x, self.home_y = 740, 110
        self.home_draw_y = 0

        self.shild = 0.5

        self.hp_x, self.hp_y = 10, 10
        self.hp = 200
        self.hit_point = 20

        self.cos, self.sin = 0, 0

        self.space = None

        self.state = self.STAND
        self.bullet_state = self.NO_SHOT
        self.game_state = self.GAME_DEFENCE

        self.hp_font = load_font('font_file\ENCR10B.TTF', 15)
        self.go_defence_font = load_font('font_file\ENCR10B.TTF', 30)
        self.game_over_font = load_font('font_file\ENCR10B.TTF', 100)

        self.soldier_image = load_image('png_file\soldier.png')
        self.ship_image = load_image('png_file\ship.png')
        self.ship_home_image = load_image('png_file\ship_home.png')

        self.go_defence_image = load_image('png_file\go_defence.png')

        self.hp_bk_image = load_image('png_file\soldier_hp_black.png')
        self.hp_rd_image = load_image('png_file\soldier_hp_red.png')

        self.shild_image = load_image('png_file\ship_shild.png')


    ###########################################################################################


    def update(self, frame_time):
        if self.game_state == self.GAME_DEFENCE:
            distance = (frame_time * self.SOLDIER_PPS)
            self.total_frame += (frame_time * self.FRAMES_PER_ACTION * self.ACTION_PER_TIME)

        elif self.game_state == self.GAME_SHOOTING:
            distance = (frame_time * self.SHIP_PPS)

        else:
            distance = 0

        self.handle_move(distance, self.total_frame)


    ###########################################################################################


    def draw(self):
        if self.game_state == self.GAME_DEFENCE:
            self.soldier_image.clip_draw(self.frame_x * 30, self.frame_y * 40, 30, 40, self.x, self.y)

            self.hp_bk_image.draw(60, 110)
            self.hp_rd_image.clip_draw_to_origin(0, 0, 100, self.hp, self.hp_x, self.hp_y)
            self.hp_font.draw(30, 110, '%d/200' %self.hp, (255, 255, 255))

        elif self.game_state == self.GAME_SHOOTING:
            self.go_defence_image.draw(self.home_x, self.home_y)
            self.ship_image.draw(self.x, self.y)
            self.shild_image.opacify(self.shild)
            self.shild_image.rotate_draw(0, self.x, self.y, 100, 100)

            if self.in_go_defence():
                self.go_defence_font.draw(self.home_x - 50, self.home_y, 'SHIFT', (255, 0, 0))

        self.ship_home_image.draw(self.home_x, self.home_draw_y)

        if self.game_state == self.GAME_OVER:
            self.game_over_font.draw(150, 500, 'You Die!!', (255, 0, 0))