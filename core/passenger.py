# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Passenger class

import random
import time

class Passenger:
    def __init__(self, world, screen, x, y):
        self.pygame = world.pygame
        self.screen, self.world = screen, world
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/passengers/" + model)
        self.x, self.y, self.distance = x, y, random.randint(5000, 10000)
        self.drawing, self.ride = False, False
        self.ui = self.pygame.font.SysFont("monaco", 25)

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])
        if self.world.taxi.passenger:
            ui_distance = self.ui.render("Distance: %s" % self.distance, 1, (255, 255, 255))
            self.screen.blit(ui_distance, (475, 50))
        else:
            ui_distance = self.ui.render("Distance: 0", 1, (255, 255, 255))
            self.screen.blit(ui_distance, (475, 50))

    # move passenger
    def move(self):
        if self.y >= 480:
            self.change()
            self.y = 0
            self.drawing = False
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_UP]:
            self.y += 0.2

    # passenger game logic
    def update(self):
        if not self.world.taxi.passenger:
            current = self.world.taxi.last_trip
            t = random.randint(current + 5, current + 30)
            if t == int(time.time()):
                self.drawing = True
            key = self.pygame.key.get_pressed()
            if key[self.pygame.K_z] and (self.ride == False):
                self.drawing = False
                self.world.taxi.add_passenger()

    # change pass
    def change(self):
        model = random.choice(["boy.png", "girl.png"])
        self.image = self.pygame.image.load("./images/passengers/" + model)

    # cab ride
    def cab_ride(self):
        self.distance -= 1000
        if self.distance <= 0:
            self.distance = 0

    # update distance
    def update_dist(self):
        self.distance = random.randint(5000, 10000)
