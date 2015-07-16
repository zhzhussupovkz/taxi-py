# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Taxi class - main player

from car import *

class Taxi(Car):
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        self.acc = pygame.mixer.Sound("./sounds/acc.ogg")
        self.beep_sound = pygame.mixer.Sound("./sounds/beep.ogg")
        self.acc.set_volume(0.01)
        self.beep_sound.set_volume(0.01)
        self.gear = 1
        self.fuel, self.damage, self.money, self.lives, self.score, self.distance = 100, 100, 200, 3, 0, 0
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
