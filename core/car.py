# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Car class

class Car(object):
    def __init__(self, screen, x, y, image):
        self.image = image
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move_left(self):
        self.x -= 0.2
        if self.x <= 135:
            self.x = 135

    def move_right(self):
        self.x += 0.2
        if self.x >= 280:
            self.x = 280

    def go(self):
        if self.y >= 200:
            self.y -= 0.5

    def brake(self):
        if self.y <= 450:
            self.y += 0.2
