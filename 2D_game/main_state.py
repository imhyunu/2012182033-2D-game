from pico2d import *

from space_world import Space_World
from soldier import Soldier
from soldier_bullet import Soldier_Bullet
from tower import Tower
from ship_bullet import Ship_Bullet
from alien import Alien

import game_framework

space_world = None
soldier = None
soldier_bullet_team = None
tower = None
ship_bullet_team = None
alien_team = None

################################################################################################


def enter():
    global soldier, space_world, soldier_bullet_team, tower, ship_bullet_team, alien_team

    space_world = Space_World()
    soldier = Soldier()
    tower = Tower()
    soldier_bullet_team = [Soldier_Bullet() for i in range(10)]
    ship_bullet_team = [Ship_Bullet() for i in range(30)]
    alien_team = [Alien() for i in range(30)]

    soldier.get_space(space_world)
    tower.get_space(space_world)

    for alien in alien_team:
        alien.get_tower(tower)

################################################################################################


def exit():
    global soldier, space_world, soldier_bullet_team, tower, ship_bullet_team, alien_team

    del(soldier)
    del(space_world)
    del(soldier_bullet_team)
    del(tower)
    del(ship_bullet_team)
    del(alien_team)

    clear_canvas()


################################################################################################


def pause():
    pass

def resume():
    pass


################################################################################################


def handle_key(event):
    pass


################################################################################################


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RCTRL):
            for bullet in ship_bullet_team:
                if bullet.what_state():
                    bullet.shot(soldier)
                    return

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if soldier.out_ship(event.x, 600 - event.y):
                soldier.game_defence()
                space_world.game_defence()
                tower.game_defence()
                for bullet in soldier_bullet_team:
                    bullet.game_defence()

            for bullet in soldier_bullet_team:
                if bullet.what_state():
                    bullet.shot(soldier, event.x, 600 - event.y)
                    return

        else:
            soldier.handle_events(event)


################################################################################################


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
    ############## get_parent ###################

    soldier.get_space(space_world)
    tower.get_space(space_world)
    for alien in alien_team:
        alien.get_tower(tower)

    ############# update ##########################

    space_world.update(frame_time)

    soldier.update(frame_time)

    for bullet in soldier_bullet_team:
        bullet.update(frame_time)

    for bullet in ship_bullet_team:
        bullet.update(frame_time)

    for alien in alien_team:
        alien.update(frame_time)

    ############ game_change #####################

    if soldier.in_home():
        soldier.soldier_in_ship()
        space_world.soldier_in_ship()
        tower.soldier_in_ship()
        for bullet in soldier_bullet_team:
            bullet.soldier_in_ship()
        for bullet in ship_bullet_team:
            bullet.soldier_in_ship()

    if space_world.what_frame():
        space_world.game_shooting()
        soldier.game_shooting()
        tower.game_shooting()
        for bullet in soldier_bullet_team:
            bullet.game_shooting()
        for bullet in ship_bullet_team:
            bullet.game_shooting()

    ########### soldier die #########################

    if soldier.what_hp():
        soldier.game_over()
        space_world.game_over()
        tower.game_over()
        for bullet in soldier_bullet_team:
            bullet.game_over()
        for bullet in ship_bullet_team:
            bullet.game_over()

    ########### collide #############################

    for bullet in soldier_bullet_team:
        for alien in alien_team:
            if collide(alien, bullet):
                alien.hit()
                bullet.hit()

    for alien in alien_team:
        if collide(alien, soldier):
            alien.bump_soldier()
            soldier.hit()

    for alien in alien_team:
        if collide(alien, tower):
            alien.bump_soldier()
            tower.hit()


################################################################################################


def draw(frame_time):
    clear_canvas()

    space_world.draw()

    soldier.draw()

    tower.draw()

    for bullet in soldier_bullet_team:
        bullet.draw()

    for bullet in ship_bullet_team:
        bullet.draw()

    for alien in alien_team:
        alien.draw()

    update_canvas()