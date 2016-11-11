from pico2d import *
import game_framework

from soldier import Soldier
from space import Space
from tutorial import Tutorial

soldier = None
space = None
tutorial = None


################################################################################################


def enter():
    clear_canvas()
    global soldier, space, tutorial

    soldier = Soldier()
    space = Space()
    tutorial = Tutorial()


################################################################################################


def exit():
    global soldier, space, tutorial

    del(soldier)
    del(space)
    del(tutorial)


################################################################################################


def pause():
    pass

def resume():
    pass


################################################################################################


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()

        if event.type == SDL_MOUSEMOTION:
            if tutorial.handle_event(event):
                tutorial.big_next()
            else:
                tutorial.small_next()

        if event.type == SDL_MOUSEBUTTONDOWN:
            if tutorial.handle_event(event):
                tutorial.next_tutorial()

        else:
            soldier.handle_events(event)


################################################################################################


def update(frame_time):
    soldier.update(frame_time)


################################################################################################


def draw(frame_time):
    global tutorial_state

    clear_canvas()

    space.draw()

    tutorial.draw()

    soldier.draw()

    update_canvas()

