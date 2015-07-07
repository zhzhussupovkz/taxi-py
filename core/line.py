# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Line class

class Line:
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        self.screen = screen
        self.x, self.y = x, y
        self.img = pygame.image.load("./images/env/line.png").convert()

    def draw(self):
        self.screen.blit(self.img, [self.x, self.y])

    def move(self):
        if self.y >= 480:
            self.y = 0
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2
