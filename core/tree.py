# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Tree class

import random

class Tree:
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        self.screen = screen
        model = random.choice(['tree.png', 'tree_1.png'])
        self.image = self.pygame.image.load("./images/houses/" + model)
        self.x, self.y = x, y

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move(self):
        if self.y >= 480:
            self.change()
            self.y = 0
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2

    def change(self):
        model = random.choice(['tree.png', 'tree_1.png'])
        self.image = self.pygame.image.load("./images/houses/" + model)
