# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Road class

from line import *

class Road:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.road = pygame.image.load("./images/env/asphalt.png").convert()
        self.lines = []
        i = 10
        while i <= 450:
            self.lines.append(Line(self.pygame, self.screen, 215, i))
            i += 40

    def draw(self):
        self.screen.blit(self.road, [120, 0])
        for l in self.lines:
            l.draw()

    def move(self):
        for l in self.lines:
            l.move()
