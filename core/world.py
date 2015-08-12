# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# World class

import pygame, sys
import random
import math
from road import *
from taxi import *
from driver import *
from passenger import *
from prize import *
from tree import *
from house import *
from board import *

class World:
    SIZE = (640, 480)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Taxi')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/env/green.png").convert()
        self.road = Road(self, self.screen)
        self.taxi = Taxi(self, self.screen, 256, 432)
        self.passenger = Passenger(self, self.screen, 347.5, 25)
        self.prize = Prize(self, self.screen)
        self.drivers, self.trees, self.houses = [], [], []
        self.gen_drivers()
        self.gen_trees()
        self.gen_houses()
        self.board = Board(pygame, self.screen)

    def gen_drivers(self):
        i = 10
        while i <= 600:
            coord = random.randint(135, 185)
            self.drivers.append(Driver(pygame, self.screen, coord, i))
            i += 150

    def gen_trees(self):
        i = 10
        while i <= 500:
            self.trees.append(Tree(self, self.screen, 80, i))
            self.trees.append(Tree(self, self.screen, 325, i))
            i += 100

    def gen_houses(self):
        i = 20
        while i <= 500:
            self.houses.append(House(self, self.screen, 25, i))
            self.houses.append(House(self, self.screen, 370, i))
            i += 100

    def draw(self):
        self.board.draw()
        self.road.draw()
        self.taxi.draw()
        self.passenger.draw()
        self.prize.draw()
        for driver in self.drivers:
            driver.draw()
        for tree in self.trees:
            tree.draw()
        for house in self.houses:
            house.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.taxi.driving()
            self.passenger.update()
            self.passenger.move()
            self.prize.update()
            self.prize.move()
            for driver in self.drivers:
                driver.driving()
                if math.fabs(driver.x - self.taxi.x) <= 15 and math.fabs(driver.y - self.taxi.y) <= 15:
                    self.taxi.add_injury()
            for tree in self.trees:
                tree.move()
            for house in self.houses:
                house.move()
            self.road.move()
            pygame.display.flip()
        pygame.quit()
