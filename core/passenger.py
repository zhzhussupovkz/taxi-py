# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Passenger class

import random

class Passenger:
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        self.screen = screen
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/passengers/" + model)
        self.x, self.y, self.distance = x, y, random.randint(5000, 10000)
        self.drawing, self.ride = False, False
        self.ui = self.pygame.font.SysFont("monaco", 25)

    def draw(self):
        if drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def move(self):
        if self.y >= 480:
            self.change()
            self.y = 0
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2

    def change(self):
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/passengers/" + model)
