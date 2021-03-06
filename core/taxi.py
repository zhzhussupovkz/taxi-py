# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Taxi class - main player

from car import *
import time

class Taxi(Car):
    def __init__(self, world, screen, x, y):
        self.pygame, self.world = world.pygame, world
        self.acc = self.pygame.mixer.Sound("./sounds/acc.ogg")
        self.beep_sound = self.pygame.mixer.Sound("./sounds/beep.ogg")
        self.door_sound = self.pygame.mixer.Sound("./sounds/door.ogg")
        self.crash_sound = self.pygame.mixer.Sound("./sounds/crash.ogg")
        self.collect_sound = self.pygame.mixer.Sound("./sounds/collect.ogg")
        self.acc.set_volume(0.01)
        self.beep_sound.set_volume(0.01)
        self.door_sound.set_volume(0.1)
        self.crash_sound.set_volume(0.01)
        self.collect_sound.set_volume(0.01)
        self.gear = 1
        self.passenger, self.dead, self.g = False, False, True
        self.fuel, self.damage, self.money, self.lives, self.score, self.distance = 100, 100, 200, 3, 0, 0
        self.last_trip = self.last_prize = self.last_gear = int(time.time())
        self.ui = self.pygame.font.SysFont("monaco", 25)
        image = self.pygame.image.load("./images/cars/taxi.png")
        super(Taxi, self).__init__(screen, x, y, image)

    def draw(self):
        super(Taxi, self).draw()
        self.draw_score()

    def draw_score(self):
        i = 0
        for j in range(0, self.lives):
            self.screen.blit(self.image, [485 + i, 190])
            i += 34
        ui_sc = self.ui.render("Score: %s" % self.score, 1, (255, 255, 255))
        ui_money = self.ui.render("%s" % self.money, 1, (255, 255, 255))
        ui_damage = self.ui.render("%s" % self.damage, 1, (255, 255, 255))
        ui_fuel = self.ui.render("%s" % self.fuel, 1, (255, 255, 255))
        ui_gear = self.ui.render("%s" % self.gear, 1, (255, 255, 255))
        self.screen.blit(ui_sc, (485, 20))
        self.screen.blit(ui_money, (525, 82))
        self.screen.blit(ui_damage, (525, 107))
        self.screen.blit(ui_fuel, (525, 132))
        self.screen.blit(ui_gear, (525, 157))

    def beep(self):
        self.acc.stop()
        self.beep_sound.play()

    def go(self):
        if self.y >= 200:
            self.y -= 0.5
        self.distance += 10
        if self.distance % 1000 == 0:
            self.fuel -= (0.5 * self.gear)
            if self.fuel <= 0:
                self.fuel = 0
            if self.passenger:
                self.money += (10 * self.gear)
                self.score += (100 * self.gear)
                self.world.passenger.cab_ride()
        if self.world.passenger.distance == 0:
            self.del_passenger()
            self.world.passenger.update_dist()

    def driving(self):
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.go()
            self.acc.play()
        elif key[self.pygame.K_DOWN]:
            self.brake()
            self.acc.stop()
        if key[self.pygame.K_RIGHT]:
            self.move_right()
        elif key[self.pygame.K_LEFT]:
            self.move_left()
        if key[self.pygame.K_SPACE]:
            self.beep()
        self.transmission()

    # transmission logic
    def transmission(self):
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_LSHIFT] and self.g:
            self.gear += 1
            self.g = False
        elif key[self.pygame.K_LCTRL] and self.g:
            self.gear -= 1
            self.g = False
        if self.gear >= 4:
            self.gear = 4
        if self.gear <= 1:
            self.gear = 1
        if (int(time.time()) - self.last_gear) == 10:
            self.g = True
            self.last_gear = int(time.time())

    # add passenger
    def add_passenger(self):
        self.acc.stop()
        self.passenger = True
        self.door_sound.play()

    # delete passenger
    def del_passenger(self):
        self.acc.stop()
        time.sleep(2)
        self.passenger = False
        self.door_sound.play()
        self.world.passenger.drawing = True

    #add fuel
    def refuel(self):
        self.fuel += 10
        if self.fuel >= 100:
            self.fuel = 100
        self.score += (3 * self.gear)

    #repair auto
    def repair(self):
        self.damage += 10
        if self.damage >= 100:
            self.damage = 100
        self.score += (5 * self.gear)

    # add money
    def coin(self):
        self.money += 5
        self.score += (10 * self.gear)

    # add injury
    def add_injury(self):
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.damage -= (2 * self.gear)
        else:
            self.damage -= 2
        self.x += 15
        self.y += 15
        if self.damage <= 0:
            self.damage = 0
            self.acc.stop()
            self.crash_sound.play()
            self.reboot()

    # reboot player
    def reboot(self):
        self.x, self.y = 250, 425
        time.sleep(2)
        self.lives -= 1
        self.damage = 100

    # game over
    def game_over(self):
        self.dead = True
