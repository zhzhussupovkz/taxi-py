# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# World class

import pygame, sys
import random
from road import *
from taxi import *
from driver import *
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
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/env/green.png").convert()
        self.road = Road(pygame, self.screen)
        self.taxi = Taxi(pygame, self.screen, 256, 432)
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
            self.trees.append(Tree(pygame, self.screen, 80, i))
            self.trees.append(Tree(pygame, self.screen, 325, i))
            i += 100

    def gen_houses(self):
        i = 20
        while i <= 500:
            self.houses.append(House(pygame, self.screen, 25, i))
            self.houses.append(House(pygame, self.screen, 370, i))
            i += 100

    def draw(self):
        self.board.draw()
        self.road.draw()
        self.taxi.draw()
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

            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.taxi.driving()
            for driver in self.drivers:
                driver.driving()
            for tree in self.trees:
                tree.move()
            for house in self.houses:
                house.move()
            self.road.move()
            pygame.display.flip()
        pygame.quit()
