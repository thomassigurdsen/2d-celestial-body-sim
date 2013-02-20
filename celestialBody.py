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
    def __init__(self, radius, xpos, ypos, color):
        if DEBUG > 1:
            print("in celBody!")
        self.rad = int(radius)
        self.pos = int(xpos), int(ypos)
        self.color = color
    # init end

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
# CelBody end
