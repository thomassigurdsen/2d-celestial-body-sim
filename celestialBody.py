#! /usr/bin/python

#  celestialBody.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
import pygame
from utils import DEBUG
pygame.init()


class CelestialBody:
    def __init__(self, radius, xpos, ypos, color, screen):
        if DEBUG > 2:
            print("in celBody!")
        self.rad = int(radius)
        self.rect = pygame.Rect((xpos, ypos), (self.rad, self.rad))
        self.color = color
        if DEBUG > 0:
            print("size: ", self.rect.size)
            print("typeof w: ", type(self.rect.width))
            print("typeof h: ", type(self.rect.height))
        self.surface = pygame.Surface(screen.subsurface(self.rect))
    # init end

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.rad)

    def update(self):
        pass

# CelBody end
