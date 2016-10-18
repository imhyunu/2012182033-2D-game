from pico2d import *

class Ship():
    PIXEL_PER_METER = (10.0 / 0.5)
    SPACESHIP_KPH = 30
    SPACESHIP_MPM = (SPACESHIP_KPH * 1000 / 60)
    SPACESHIP_MPS = (SPACESHIP_MPM / 60)
    SPACESHIP_PPS = (SPACESHIP_MPS * PIXEL_PER_METER)

    UP_MOVE, DOWN_MOVE, RIGHT_MOVE, LEFT_MOVE, STOP = 0, 1, 2, 3, 4
    UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT = 5, 6, 7, 8
    LEFT_UP_RIGHT, LEFT_DOWN_RIGHT = 9, 10
    LEFT_RIGHT = 11
    OUT_HOME = 12

    GAME_STATE_DEFENCE, GAME_STATE_SHOOTING, GAME_OVER = 0, 1, 2

    def ship_die(self):
        if self.game_state == self.GAME_OVER:
            return True
        else: return False

    def bump(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if self.hp_frame > 30:
                self.hp_frame = self.hp_frame / 2
            if self.hp_frame < 30:
                self.hp_frame = 0
                self.game_state = self.GAME_OVER

    def in_soldier(self):
        if self.game_state == self.GAME_STATE_DEFENCE:
            self.state = self.OUT_HOME

    def get_bb(self):
        if self.game_state == self.GAME_STATE_DEFENCE:
            return self.home_x - 50, self.home_y + 100, self.home_x + 50, self.home_y - 100

        elif self.game_state == self.GAME_STATE_SHOOTING:
            return self.x - 10, self.y + 10, self.x + 10, self.y - 10

        elif self.game_state == self.GAME_OVER:
            return 0, 0, 0, 0

    def up(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if (self.state == self.STOP) or (self.state == self.DOWN_MOVE):
                self.state = self.UP_MOVE
            elif self.state == self.RIGHT_MOVE:
                self.state = self.UP_RIGHT
            elif self.state == self.LEFT_MOVE:
                self.state = self.UP_LEFT

    def down(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if (self.state == self.STOP) or (self.state == self.UP_MOVE):
                self.state = self.DOWN_MOVE
            elif self.state == self.RIGHT_MOVE:
                self.state = self.DOWN_RIGHT
            elif self.state == self.LEFT_MOVE:
                self.state = self.DOWN_LEFT

    def right(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if (self.state == self.STOP) or (self.state == self.LEFT_MOVE):
                self.state = self.RIGHT_MOVE
            elif self.state == self.DOWN_MOVE:
                self.state = self.DOWN_RIGHT
            elif self.state == self.UP_MOVE:
                self.state = self.UP_RIGHT
            elif self.state == self.UP_LEFT:
                self.state = self.LEFT_UP_RIGHT
            elif self.state == self.DOWN_LEFT:
                self.state = self.LEFT_DOWN_RIGHT

    def left(self):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if (self.state == self.STOP) or (self.state == self.RIGHT_MOVE):
                self.state = self.LEFT_MOVE
            elif self.state == self.UP_MOVE:
                self.state = self.UP_LEFT
            elif self.state == self.DOWN_MOVE:
                self.state = self.DOWN_LEFT
            elif self.state == self.UP_RIGHT:
                self.state = self.LEFT_UP_RIGHT
            elif self.state == self.DOWN_RIGHT:
                self.state = self.LEFT_DOWN_RIGHT

    def stop(self, event):
        if self.game_state == self.GAME_STATE_SHOOTING:
            if (self.state, event.key) == (self.UP_MOVE, SDLK_w):
                self.state = self.STOP
            elif (self.state, event.key) == (self.DOWN_MOVE, SDLK_s):
                self.state = self.STOP
            elif (self.state, event.key) == (self.RIGHT_MOVE, SDLK_d):
                self.state = self.STOP
            elif (self.state, event.key) == (self.LEFT_MOVE, SDLK_a):
                self.state = self.STOP

            elif self.state == self.UP_RIGHT:
                if event.key == SDLK_d:
                    self.state = self.UP_MOVE
                elif event.key == SDLK_w:
                    self.state = self.RIGHT_MOVE

            elif self.state == self.UP_LEFT:
                if event.key == SDLK_a:
                    self.state = self.UP_MOVE
                elif event.key == SDLK_w:
                    self.state = self.LEFT_MOVE

            elif self.state == self.DOWN_RIGHT:
                if event.key == SDLK_d:
                    self.state = self.DOWN_MOVE
                elif event.key == SDLK_s:
                    self.state = self.RIGHT_MOVE

            elif self.state == self.DOWN_LEFT:
                if event.key == SDLK_a:
                    self.state = self.DOWN_MOVE
                elif event.key == SDLK_s:
                    self.state = self.LEFT_MOVE

            elif self.state == self.LEFT_UP_RIGHT:
                if event.key == SDLK_d:
                    self.state = self.UP_LEFT
                elif event.key == SDLK_a:
                    self.state = self.UP_RIGHT
                elif event.key == SDLK_w:
                    self.state = self.LEFT_RIGHT

            elif self.state == self.LEFT_DOWN_RIGHT:
                if event.key == SDLK_d:
                    self.state = self.DOWN_LEFT
                elif event.key == SDLK_a:
                    self.state = self.DOWN_RIGHT
                elif event.key == SDLK_s:
                    self.state = self.LEFT_RIGHT

            elif self.state == self.LEFT_RIGHT:
                if event.key == SDLK_a:
                    self.state = self.RIGHT_MOVE
                elif event.key == SDLK_d:
                    self.state = self.LEFT_MOVE

    def soldier_in(self):
        self.game_state = self.GAME_STATE_SHOOTING


    ################################################################################################


    def __init__(self):
        self.x, self.y = 740, 100
        self.hp_x, self.hp_y = 60, 110
        self.hp_frame = 200
        self.home_x, self.home_y = 740, 100
        self.state = self.STOP
        self.game_state = self.GAME_STATE_DEFENCE
        self.image = load_image('ship.png')
        self.ship_home_image = load_image('ship_home.png')
        self.hp_image = load_image('ship_shild.png')
        self.font = load_font('ENCR10B.TTF', 100)


    ################################################################################################


    def update(self, frame_time):
        if self.game_state == self.GAME_STATE_DEFENCE:
            if self.state == self.OUT_HOME:
                self.home_y -= 10
                if self.home_y < -1000:
                    self.home_y = -1000
                    self.state = self.STOP
                    self.game_state = self.GAME_STATE_SHOOTING

        elif self.game_state == self.GAME_STATE_SHOOTING:
            distance = (self.SPACESHIP_PPS * frame_time)

            if self.state == self.UP_MOVE:
                self.y += distance

            elif self.state == self.DOWN_MOVE:
                self.y -= distance

            elif self.state == self.RIGHT_MOVE:
                self.x += distance

            elif self.state == self.LEFT_MOVE:
                self.x -= distance

            elif self.state == self.UP_RIGHT:
                self.x += (distance * math.cos(math.radians(45)))
                self.y += (distance * math.sin(math.radians(45)))

            elif self.state == self.UP_LEFT:
               self.x -= (distance * math.cos(math.radians(45)))
               self.y += (distance * math.sin(math.radians(45)))

            elif self.state == self.DOWN_RIGHT:
                self.x += (distance * math.cos(math.radians(45)))
                self.y -= (distance * math.sin(math.radians(45)))

            elif self.state == self.DOWN_LEFT:
                self.x -= (distance * math.cos(math.radians(45)))
                self.y -= (distance * math.sin(math.radians(45)))

            elif self.state == self.LEFT_UP_RIGHT:
                self.y += distance

            elif self.state == self.LEFT_DOWN_RIGHT:
                self.y -= distance


    ################################################################################################


    def draw(self):
        self.image.draw(self.x, self.y)
        self.ship_home_image.draw(self.home_x, self.home_y)
        if self.game_state == self.GAME_STATE_SHOOTING:
            self.hp_image.rotate_draw(0, self.hp_x, self.hp_y, (self.hp_frame / 2), self.hp_frame)
        if self.game_state == self.GAME_OVER:
            self.font.draw(150, 300, 'You Die!!', (255, 0, 0))