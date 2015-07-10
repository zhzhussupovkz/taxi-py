# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Prize class

import random

class Prize:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/env/present.png")
        self.x, self.y, self.drawing = random.randint(225, 280), random.randint(10, 150), False
        self.type = random.choice(['fuel', 'money', 'damage'])

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def move(self):
        if self.y >= 480:
            self.change()
            self.y = 0
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2

    def change(self):
        self.x, self.y, self.drawing = random.randint(225, 280), random.randint(10, 150), False
        self.type = random.choice(['fuel', 'money', 'damage'])
