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
import math
from utils import DEBUG
pygame.init()


class Vector2():
    def __init__(self, xCo, yCo):
        if DEBUG > 3:
            print("in Vector2!")
        pygame.sprite.Sprite.__init__(self)
        self.xCo = xCo
        self.yCo = yCo
    # init end

    def printCo(self):
        print("X,Y: ", self.xCo, ",", self.yCo)

    def add(self, rhs):
        return Vector2((self.xCo + rhs.xCo), (self.yCo + rhs.yCo))

    def diff(self, rhs):
        return Vector2((self.xCo - rhs.xCo), (self.yCo - rhs.yCo))

    def times(self, rhs):
        if isinstance(rhs, Vector2):
            ret = Vector2((self.xCo * rhs.xCo), (self.yCo * rhs.yCo))
        else:
            ret = Vector2((self.xCo * rhs), (self.yCo * rhs))
        return ret

    def divide(self, rhs):
        if isinstance(rhs, Vector2):
            ret = Vector2((self.xCo / rhs.xCo), (self.yCo / rhs.yCo))
        else:
            ret = Vector2((self.xCo / rhs), (self.yCo / rhs))
        return ret

    def dot(self, rhs):
        return (self.xCo * rhs.xCo) + (self.yCo * rhs.yCo)

    def cross(self, rhs):
        return (self.xCo * rhs.yCo) - (self.yCo * rhs.xCo)

    def length(self):
        return math.sqrt((self.xCo * self.xCo) + (self.yCo * self.yCo))

    def sqlength(self):
        return (self.xCo * self.xCo) + (self.yCo * self.yCo)

    def unit(self):
        return self / self.length()

    def turn(self, angle):
        return Vector2((self.xCo * math.cos(angle) - self.yCo *
                        math.sin(angle)), (self.xCo * math.sin(angle) +
                                           self.yCo * math.cos(angle)))

    def angle(self):
        return math.atan2(self.yCo, self.xCo)

# Vector2 end
