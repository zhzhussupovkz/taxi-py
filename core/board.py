# -*- coding: utf-8 -*-
# Copyright (c) 2015 Zhassulan Zhussupov
# Author zhzhussupovkz@gmail.com
# Board class

import datetime

class Board:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.image = self.pygame.image.load("./images/scboard/scboard.png")
        self.fuel = self.pygame.image.load("./images/scboard/fuel.png")
        self.money = self.pygame.image.load("./images/scboard/dollar.png")
        self.damage = self.pygame.image.load("./images/scboard/wrench.png")
        self.transmission = self.pygame.image.load("./images/scboard/transmission.png")
        self.ui = self.pygame.font.SysFont("monaco", 15)
        self.controls = self.pygame.font.SysFont("monaco", 20)

    def draw(self):
        self.screen.blit(self.image, [440, 0])
        self.screen.blit(self.money, [495, 80])
        self.screen.blit(self.damage, [495, 105])
        self.screen.blit(self.fuel, [495, 130])
        self.screen.blit(self.transmission, [495, 155])
        self.draw_controls()
        cyear = datetime.datetime.now().year
        copyright = self.ui.render("Copyright (c) %s by zhzhussupovkz" % cyear, 1, (255, 255, 255))
        self.screen.blit(copyright, (445, 450))

    def draw_controls(self):
        contr = self.controls.render("controls:", 1, (255, 255, 255))
        move = self.controls.render("move - arrows", 1, (255, 255, 255))
        beep = self.controls.render("beep - space", 1, (255, 255, 255))
        passenger = self.controls.render("passenger - alt", 1, (255, 255, 255))
        gear_up = self.controls.render("gear up - shift", 1, (255, 255, 255))
        gear_down = self.controls.render("gear down - ctrl", 1, (255, 255, 255))
        quit = self.controls.render("quit - esc", 1, (255, 255, 255))
        self.screen.blit(contr, (500, 225))
        self.screen.blit(move, (485, 255))
        self.screen.blit(beep, (485, 280))
        self.screen.blit(passenger, (485, 305))
        self.screen.blit(gear_up, (485, 330))
        self.screen.blit(gear_down, (485, 355))
        self.screen.blit(quit, (485, 380))