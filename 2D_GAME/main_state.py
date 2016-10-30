from pico2d import *

import game_framework
import json

from space import Space
from soldier import Soldier
from soldier_bullet import Soldier_Bullet
from tower import Tower
from ship_bullet import Ship_Bullet

space = None
soldier = None
soldier_bullet_team = None
tower = None
ship_bullet = None


#################################################################################################


soldier_data_file = open('text_file\soldier.txt', 'r')
soldier_data = json.load(soldier_data_file)
soldier_data_file.close()

soldier_bullet_data_file = open('text_file\soldier_bullet.txt', 'r')
soldier_bullet_data = json.load(soldier_bullet_data_file)
soldier_bullet_data_file.close()

ship_bullet_data_file = open('text_file\ship_bullet.txt', 'r')
ship_bullet_data = json.load(ship_bullet_data_file)
ship_bullet_data_file.close()

tower_data_file = open('text_file\defence_tower.txt')
tower_data = json.load(tower_data_file)
tower_data_file.close()

#################################################################################################


def creat_soldier_bullet_team():
    bullet_team = []

    for name in soldier_bullet_data:
        bullet = Soldier_Bullet()
        bullet.range = soldier_bullet_data[name]['range']
        bullet_team.append(bullet)

    return bullet_team

def creat_ship_bullet_team():
    bullet_team = []

    for name in ship_bullet_data:
        bullet = Ship_Bullet()
        bullet.range = ship_bullet_data[name]['range']
        bullet_team.append(bullet)

    return bullet_team

def creat_soldier():
    data = Soldier()

    data.x = soldier_data['x']
    data.y = soldier_data['y']
    data.hit_point = soldier_data['hit_point']

    return data

def creat_tower():
    data = Tower()

    data.hit_point = tower_data['hit_point']

    return data

#################################################################################################


def enter():
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team

    space = Space()

    soldier = creat_soldier()

    soldier_bullet_team = creat_soldier_bullet_team()
    ship_bullet_team = creat_ship_bullet_team()

    tower = creat_tower()

    soldier.get_space(space)
    tower.get_space(space)

#################################################################################################


def exit():
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team

    del(space)
    del(soldier)
    del(soldier_bullet_team)
    del(tower)
    del(ship_bullet_team)

    clear_canvas()


#################################################################################################


def pause():
    pass


def resume():
    pass


#################################################################################################


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

        else:
            soldier.handle_events(event)

        if event.type == SDL_MOUSEBUTTONDOWN:
            for bullet in soldier_bullet_team:
                if bullet.what_state():
                    bullet.shot(soldier, event.x, 1000 - event.y)
                    break

        if event.type == SDL_KEYDOWN:
            if event.key in (SDLK_LSHIFT, SDLK_RSHIFT):
                if soldier.in_go_defence():
                    soldier.game_defence()
                    for bullet in soldier_bullet_team:
                        bullet.game_defence()
                    for bullet in ship_bullet_team:
                        bullet.game_defence()
                    space.game_defence()
            elif event.key == SDLK_RCTRL:
                for bullet in ship_bullet_team:
                    if bullet.what_state():
                        bullet.shot(soldier)
                        break


#################################################################################################


def collide(a, b):

    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


#################################################################################################


def update(frame_time):
    soldier.get_space(space)
    tower.get_space(space)

    soldier.update(frame_time)
    for bullet in soldier_bullet_team:
        bullet.update(frame_time)
    for bullet in ship_bullet_team:
        bullet.update(frame_time)

    if soldier.in_home():
        soldier.game_shooting()
        for bullet in soldier_bullet_team:
            bullet.game_shooting()
        for bullet in ship_bullet_team:
            bullet.game_shooting()
        space.game_shooting()


#################################################################################################


def draw(frame_time):
    clear_canvas()

    space.draw()

    soldier.draw()

    for bullet in soldier_bullet_team:
        bullet.draw()
    for bullet in ship_bullet_team:
        bullet.draw()

    tower.draw()

    update_canvas()