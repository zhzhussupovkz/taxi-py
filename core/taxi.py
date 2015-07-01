# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Taxi class - main player

from car import *

class Taxi(Car):
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        image = self.pygame.image.load("./images/cars/taxi.png")
        super(Taxi, self).__init__(screen, x, y, image)

    def draw(self):
        super(Taxi, self).draw()

    def driving(self):
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.go()
        elif key[self.pygame.K_DOWN]:
            self.brake()
        if key[self.pygame.K_RIGHT]:
            self.move_right()
        elif key[self.pygame.K_LEFT]:
            self.move_left()