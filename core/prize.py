# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Prize class

import random
import time

class Prize:
    def __init__(self, world, screen):
        self.world, self.pygame = world, world.pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/env/present.png")
        self.x, self.y, self.drawing = random.randint(225, 280), random.randint(10, 150), False
        self.type = random.choice(['fuel', 'money', 'damage'])

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    # game logic
    def update(self):
        current = self.world.taxi.last_prize
        t = random.randint(current + 10, current + 30)
        if t == int(time.time()):
            self.drawing = True

    def move(self):
        if self.drawing:
            if self.world.taxi.gear == 1:
                self.y += 0.75
            elif self.world.taxi.gear == 2:
                self.y += 0.1
            elif self.world.taxi.gear == 3:
                self.y += 0.2
            elif self.world.taxi.gear == 4:
                self.y += 0.25
        if self.y >= 480:
            self.y = 0
            self.world.taxi.last_prize = int(time.time())
            self.change()
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2

    def change(self):
        self.x, self.y, self.drawing = random.randint(225, 280), random.randint(10, 150), False
        self.type = random.choice(['fuel', 'money', 'damage'])
        self.drawing = False
