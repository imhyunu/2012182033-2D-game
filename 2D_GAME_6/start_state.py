import math

from pico2d import *

import game_framework
import menu_state

name = "StartState"
image = None

from kpu_logo import Kpu_logo

kpu_logo = None


# ////////////////////////////// def enter /////////////////////////////////////


def enter():
    global image, kpu_logo

    open_canvas(800, 1000)
    kpu_logo = Kpu_logo()
    image = load_image('png_file\whiteboard.png')


# ////////////////////////////// def exit //////////////////////////////////////


def exit():
    global image, kpu_logo

    del(image)
    del(kpu_logo)

    clear_canvas()


# ////////////////////////////// def pause /////////////////////////////////////


def pause():
    pass


# ////////////////////////////// def resume ////////////////////////////////////


def resume():
    pass


# ////////////////////////////// def handle_events /////////////////////////////


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(menu_state)


# ////////////////////////////// def update ////////////////////////////////////


def update(frame_time):
    global kpu_logo

    kpu_logo.update(frame_time)


# ////////////////////////////// def draw //////////////////////////////////////


def draw(frame_time):
    global image, kpu_logo

    clear_canvas()
    image.draw(400,500)
    kpu_logo.draw()
    update_canvas()

