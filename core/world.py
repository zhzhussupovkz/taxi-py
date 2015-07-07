# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# World class

import pygame, sys
import random
from road import *
from taxi import *
from driver import *

class World:
    SIZE = (640, 480)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Taxi')
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/env/green.png").convert()
        self.road = Road(pygame, self.screen)
        self.taxi = Taxi(pygame, self.screen, 256, 432)
        self.drivers = []
        self.gen_drivers()

    def gen_drivers(self):
        i = 10
        while i <= 600:
            coord = random.randint(135, 185)
            self.drivers.append(Driver(pygame, self.screen, coord, i))
            i += 150

    def draw(self):
        self.road.draw()
        self.taxi.draw()
        for driver in self.drivers:
            driver.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.taxi.driving()
            for driver in self.drivers:
                driver.driving()
            self.road.move()
            pygame.display.flip()
        pygame.quit()
