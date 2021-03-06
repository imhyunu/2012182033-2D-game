from pico2d import *

import game_framework
import json

from space import Space
from soldier import Soldier
from soldier_bullet import Soldier_Bullet
from tower import Tower
from ship_bullet import Ship_Bullet
from alien import Alien

space = None
soldier = None
tower = None
soldier_bullet_team = None
ship_bullet_team = None
alien_team = None

font = None

point = 0

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

tower_data_file = open('text_file\defence_tower.txt', 'r')
tower_data = json.load(tower_data_file)
tower_data_file.close()

alien_data_file = open('text_file\_alien_1.txt', 'r')
alien_data = json.load(alien_data_file)
alien_data_file.close()


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

def creat_alien_team():
    team = []

    for name in alien_data:
        alien = Alien()
        alien.hit_point = alien_data[name]['hit_point']
        team.append(alien)

    return team


#################################################################################################


def enter():
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team, alien_team
    global font

    space = Space()

    soldier = creat_soldier()

    soldier_bullet_team = creat_soldier_bullet_team()
    ship_bullet_team = creat_ship_bullet_team()
    alien_team = creat_alien_team()

    tower = creat_tower()

    soldier.get_space(space)
    tower.get_space(space)
    for alien in alien_team:
        alien.get_space(space)

    font = load_font('font_file\ENCR10B.TTF', 30)


#################################################################################################


def exit():
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team, alien_team
    global font

    del(space)
    del(soldier)
    del(soldier_bullet_team)
    del(tower)
    del(ship_bullet_team)
    del(alien_team)
    del(font)

    clear_canvas()


#################################################################################################


def pause():
    pass


def resume():
    pass


#################################################################################################


def handle_events(frame_time):
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team, alien_team

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()

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
                    tower.game_defence()
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


def point_up():
    global point

    point += 10


#################################################################################################


def update(frame_time):
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team, alien_team

    ############# get_data ######################

    soldier.get_space(space)
    tower.get_space(space)
    for alien in alien_team:
        alien.get_space(space)

    for alien in alien_team:
        if alien.go_tower():
            alien.get_tower(tower)
            alien.game_defence()

    ############# update #########################

    soldier.update(frame_time)
    for bullet in soldier_bullet_team:
        bullet.update(frame_time)
    for bullet in ship_bullet_team:
        bullet.update(frame_time)
    for alien in alien_team:
        alien.update(frame_time)

    ############# state_change ####################

    if soldier.in_home():
        soldier.game_shooting()
        for bullet in soldier_bullet_team:
            bullet.game_shooting()
        for bullet in ship_bullet_team:
            bullet.game_shooting()
        space.game_shooting()
        tower.game_shooting()

    ############# colldie ##########################

    for alien in alien_team:
        if collide(alien, soldier):
            alien.dump()
            soldier.hit()

    for alien in alien_team:
        for bullet in soldier_bullet_team:
            if collide(alien, bullet):
                alien.hit()
                bullet.hit()

    for alien in alien_team:
        for bullet in ship_bullet_team:
            if collide(alien, bullet):
                alien.hit()
                bullet.hit()

    for alien in alien_team:
        if collide(alien, tower):
            alien.dump()
            tower.dump()

    ############# hp_zero ##########################

    for alien in alien_team:
        if alien.hp_zero():
            alien.his_die()

    if soldier.hp_zero():
        soldier.game_over()
        for alien in alien_team:
            alien.game_over()
        for bullet in ship_bullet_team:
            bullet.game_over()
        for bullet in soldier_bullet_team:
            bullet.game_over()

    if tower.hp_zero():
        soldier.game_over()
        for alien in alien_team:
            alien.game_over()
        for bullet in ship_bullet_team:
            bullet.game_over()
        for bullet in soldier_bullet_team:
            bullet.game_over()


#################################################################################################


def draw(frame_time):
    global space, soldier, soldier_bullet_team, tower, ship_bullet_team, alien_team
    global font, point

    clear_canvas()

    space.draw()

    for alien in alien_team:
        alien.draw()

    soldier.draw()

    for bullet in soldier_bullet_team:
        bullet.draw()
    for bullet in ship_bullet_team:
        bullet.draw()


    tower.draw()

    font.draw(600, 900, '%d' %point, (255, 255, 255))

    update_canvas()