# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Road class

class Road:
    def __init__(self, pygame, screen):
        self.road = pygame.image.load("./images/env/asphalt.png").convert()
        self.line = pygame.image.load("./images/env/line.png").convert()
        self.screen = screen

    def draw(self):
        self.screen.blit(self.road, [120, 0])
        i = 10
        while i <= 450:
            self.screen.blit(self.line, [215, i])
            i += 40
