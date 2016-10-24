from pico2d import *

class Menu():
    def cursor(self, event):
        x, y = event.x, 600 - event.y

        if (self.st_x + 200 > x) and (self.st_x - 200 < x) and (self.st_y + 50 > y) and (self.st_y - 50 < y):
            self.st_frame_x = 420
            self.st_frame_y = 105
        else:
            self.st_frame_x = 403
            self.st_frame_y = 103

        if (self.so_x + 200 > x) and (self.so_x - 200 < x) and (self.so_y + 50 > y) and (self.so_y - 50 < y):
            self.so_frame_x = 420
            self.so_frame_y = 105
        else:
            self.so_frame_x = 403
            self.so_frame_y = 103

        if (self.ex_x + 200 > x) and (self.ex_x - 200 < x) and (self.ex_y + 50 > y) and (self.ex_y - 50 < y):
            self.ex_frame_x = 420
            self.ex_frame_y = 105
        else:
            self.ex_frame_x = 403
            self.ex_frame_y = 103

    def click_start(self, event):
        x, y = event.x, 600 - event.y

        if x >= self.st_x + 200: return False
        if x <= self.st_x - 200: return False
        if y >= self.st_y + 50: return False
        if y <= self.st_y - 50: return False

        return True

    def click_sound(self, event):
        x, y = event.x, 600 - event.y

        if x >= self.so_x + 200: return False
        if x <= self.so_x - 200: return False
        if y >= self.so_y + 50: return False
        if y <= self.so_y - 50: return False

        return True

    def click_exit(self, event):
        x, y = event.x, 600 - event.y

        if x >= self.ex_x + 200: return False
        if x <= self.ex_x - 200: return False
        if y >= self.ex_y + 50: return False
        if y <= self.ex_y - 50: return False

        return True

    def __init__(self):
        self.st_x, self.st_y = 400, 450
        self.st_frame_x, self.st_frame_y = 403, 103
        self.so_x, self.so_y = 400, 300
        self.so_frame_x, self.so_frame_y = 403, 103
        self.ex_x, self.ex_y = 400, 150
        self.ex_frame_x, self.ex_frame_y = 403, 103
        self.st_image = load_image('png_file\start_menu.png')
        self.so_image = load_image('png_file\sound_menu.png')
        self.ex_image = load_image('png_file\exit_menu.png')
        self.back_image = load_image('png_file\space.png')

    def draw(self):
        self.back_image.clip_draw(0, 500, 800, 600, 400, 300)
        self.st_image.clip_draw(0, 0, self.st_frame_x, self.st_frame_y, self.st_x, self.st_y)
        self.so_image.clip_draw(0, 0, self.so_frame_x, self.so_frame_y, self.so_x, self.so_y)
        self.ex_image.clip_draw(0, 0, self.ex_frame_x, self.ex_frame_y, self.ex_x, self.ex_y)
