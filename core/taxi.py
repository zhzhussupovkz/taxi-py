# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Taxi class - main player

from car import *

class Taxi(Car):
    def __init__(self, pygame, screen, x, y):
        image = pygame.image.load("./images/cars/taxi.png")
        super(Taxi, self).__init__(screen, x, y, image)

    def draw(self):
        super(Taxi, self).draw()
