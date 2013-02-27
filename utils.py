#! /usr/bin/python

#  utils.py
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
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import sys
pygame.init()
DEBUG = int(1)
VERBOSE = int(2)


def handleEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        # Keyboard input:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit(0)

# handleEvents end
