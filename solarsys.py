#! /usr/bin/python

#  solarsys.py
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
from utils import handleEvents, DEBUG, VERBOSE
from celestialBody import CelestialBody
pygame.init()


def main():
    print("Welcome to The 2D Solar System experience!")
    width = 1024
    height = 768
    size = width, height

    # The screen is a pygame surface object.
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption('Solar System 2D')
    clock = pygame.time.Clock()

    sun = CelestialBody(60, (width / 2), (height / 2), (240, 15, 15), screen)
    planets = []
    for pCnt in range(10):
        planets.append(CelestialBody(
            20, (pCnt),  # * 8) % width,
                (pCnt),  # * 8) % height,
                (15, 120, (15 + pCnt * 2) % 255), screen))
        if DEBUG > 2:
            print("pCnt: ", pCnt)

    running = True
    while running:
        handleEvents()
        screen.fill((15, 15, 15))
        sun.draw(screen)
        if DEBUG > 2:
            print("get_ticks: ", pygame.time.get_ticks())
        pygame.display.flip()
        clock.tick(120)
        if VERBOSE > 2:
            print("get_time: ", clock.get_time())

# Main end


# This calls the 'main' function when this script is excecuted:
if __name__ == '__main__':
    main()
