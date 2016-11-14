from pico2d import *

class Menu():

    def big_start(self):
        self.st_frame_x = 420
        self.st_frame_y = 105

    def big_tutorial(self):
        self.so_frame_x = 420
        self.so_frame_y = 105

    def big_exit(self):
        self.ex_frame_x = 420
        self.ex_frame_y = 105

    def all_small(self):
        self.st_frame_x = 403
        self.st_frame_y = 103
        self.so_frame_x = 403
        self.so_frame_y = 103
        self.ex_frame_x = 403
        self.ex_frame_y = 103

    def cursor_start(self, event):
        x, y = event.x, 1000 - event.y

        if x >= self.start_x + 200: return False
        if x <= self.start_x - 200: return False
        if y >= self.start_y + 50: return False
        if y <= self.start_y - 50: return False

        return True

    def cursor_tutorial(self, event):
        x, y = event.x, 1000 - event.y

        if x >= self.tuto_x + 200: return False
        if x <= self.tuto_x - 200: return False
        if y >= self.tuto_y + 50: return False
        if y <= self.tuto_y - 50: return False

        return True

    def cursor_exit(self, event):
        x, y = event.x, 1000 - event.y

        if x >= self.ex_x + 200: return False
        if x <= self.ex_x - 200: return False
        if y >= self.ex_y + 50: return False
        if y <= self.ex_y - 50: return False

        return True

    def __init__(self):
        self.start_x, self.start_y = 500, 650
        self.st_frame_x, self.st_frame_y = 403, 103
        self.tuto_x, self.tuto_y = 500, 500
        self.so_frame_x, self.so_frame_y = 403, 103
        self.ex_x, self.ex_y = 500, 350
        self.ex_frame_x, self.ex_frame_y = 403, 103
        self.st_image = load_image('png_file\menu_start.png')
        self.so_image = load_image('png_file\menu_tutorial.png')
        self.ex_image = load_image('png_file\menu_exit.png')
        self.back_image = load_image('png_file\space.png')

    def draw(self):
        self.back_image.clip_draw(0, 500, 800, 1000, 400, 500)
        self.st_image.clip_draw(0, 0, self.st_frame_x, self.st_frame_y, self.start_x, self.start_y)
        self.so_image.clip_draw(0, 0, self.so_frame_x, self.so_frame_y, self.tuto_x, self.tuto_y)
        self.ex_image.clip_draw(0, 0, self.ex_frame_x, self.ex_frame_y, self.ex_x, self.ex_y)
