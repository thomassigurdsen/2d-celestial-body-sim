#! /usr/bin/python

#  vector2.py
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


class Vector2():
    def __init__(self, xCo, yCo):
        pygame.sprite.Sprite.__init__(self)
        if DEBUG > 3:
            print("in Vector2!")
    # init end

# Vector2 end
