from pico2d import *
import game_framework
import main_state

from menu import Menu

menu = None


################################################################################################


def enter():
    global menu

    menu = Menu()

    clear_canvas()


################################################################################################


def exit():
    global menu

    del(menu)


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

        elif event.type == SDL_MOUSEMOTION:
            if menu.cursor_start(event):
                menu.big_start()
            elif menu.cursor_sound(event):
                menu.big_sound()
            elif menu.cursor_exit(event):
                menu.big_exit()
            else:
                menu.all_small()

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if menu.cursor_start(event):
                game_framework.push_state(main_state)
            if menu.cursor_sound(event):
                pass
            if menu.cursor_exit(event):
                game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


################################################################################################


def update(frame_time):
    pass


################################################################################################


def draw(frame_time):
    clear_canvas()

    menu.draw()

    update_canvas()

