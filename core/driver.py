# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Driver class - other cars

from car import *
import random

class Driver(Car):
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        model = random.choice(["car_1", "car_2", "car_3", "car_4", "car_5"])
        image = self.pygame.image.load("./images/cars/" + model + ".png")
        super(Driver, self).__init__(screen, x, y, image)

    def draw(self):
        super(Driver, self).draw()

    def move_down(self):
        if self.y <= 480:
            self.y += 0.1

    def driving(self):
        self.move_down()
        if self.y >= 480:
            self.change()
            self.y = 0

    def change(self):
        model = random.choice(["car_1", "car_2", "car_3", "car_4", "car_5"])
        image = self.pygame.image.load("./images/cars/" + model + ".png")
        coord = random.randint(135, 185)
        self.x = coord
