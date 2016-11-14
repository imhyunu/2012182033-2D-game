from pico2d import *
import game_framework

from soldier import Soldier
from space import Space
from tutorial import Tutorial
from soldier_bullet import Soldier_Bullet
from alien import Alien

soldier = None
space = None
tutorial = None
soldier_bullet_team = None
alien_team = None

soldier_bullet_data_file = open('text_file\soldier_bullet.txt', 'r')
soldier_bullet_data = json.load(soldier_bullet_data_file)
soldier_bullet_data_file.close()

alien_data_file = open('text_file\_tutorial_alien.txt', 'r')
alien_data = json.load(alien_data_file)
alien_data_file.close()

def creat_soldier_bullet_team():
    bullet_team = []

    for name in soldier_bullet_data:
        bullet = Soldier_Bullet()
        bullet.range = soldier_bullet_data[name]['range']
        bullet_team.append(bullet)

    return bullet_team

def creat_alien_team():
    team = []

    for name in alien_data:
        alien = Alien()
        alien.hit_point = alien_data[name]['hit_point']
        alien.x = alien_data[name]['x']
        alien.y = alien_data[name]['y']
        team.append(alien)

    return team

################################################################################################


def enter():
    clear_canvas()
    global soldier, space, tutorial, soldier_bullet_team, alien_team

    soldier = Soldier()
    space = Space()
    tutorial = Tutorial()
    soldier_bullet_team = creat_soldier_bullet_team()
    alien_team = creat_alien_team()


################################################################################################


def exit():
    global soldier, space, tutorial, soldier_bullet_team


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
            if tutorial.bullet_tutorial():
                for bullet in soldier_bullet_team:
                    if bullet.what_state():
                        bullet.shot(soldier, event.x, 1000 - event.y)
                        break

        if event.type == SDL_MOUSEBUTTONDOWN:
            if tutorial.handle_event(event):
                tutorial.next_tutorial()

        else:
            soldier.handle_events(event)



def collide(a, b):

    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


################################################################################################


def update(frame_time):
    soldier.update(frame_time)
    for alien in alien_team:
        alien.get_space(space)

    if tutorial.bullet_tutorial():
        for bullet in soldier_bullet_team:
            bullet.update(frame_time)

        for alien in alien_team:
            alien.update(frame_time)

    for alien in alien_team:
        for bullet in soldier_bullet_team:
            if collide(bullet, alien):
                alien.hit()
                bullet.hit()

    for alien in alien_team:
        if alien.hp_zero():
            alien.his_die()

################################################################################################


def draw(frame_time):
    global tutorial_state

    clear_canvas()

    space.draw()

    tutorial.draw()

    soldier.draw()

    if tutorial.bullet_tutorial():
        for bullet in soldier_bullet_team:
            bullet.draw()

        for alien in alien_team:
            alien.draw()

    update_canvas()

