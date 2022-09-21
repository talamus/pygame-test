#!/usr/bin/env python
""" pygame.examples.setmodescale

On high resolution displays(4k, 1080p) and tiny graphics games (640x480)
show up very small so that they are unplayable. SCALED scales up the window
for you. The game thinks it's a 640x480 window, but really it can be bigger.
Mouse events are scaled for you, so your game doesn't need to do it.

Passing SCALED to pygame.display.set_mode means the resolution depends
on desktop size and the graphics are scaled.
"""

import pygame as pg
from color import Color

pg.init()

RES = (160, 120)
FPS = 24
clock = pg.time.Clock()

print("desktops", pg.display.get_desktop_sizes())
screen = pg.display.set_mode(RES, pg.SCALED | pg.RESIZABLE)

# MAIN LOOP

done = False

i = 0
j = 0

r_name, r_flags = pg.display._get_renderer_info()
print("renderer:", r_name, "flags:", bin(r_flags))
for flag, name in [
    (1, "software"),
    (2, "accelerated"),
    (4, "VSync"),
    (8, "render to texture")]:
    if flag & r_flags:
        print(name)

while not done:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            done = True
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN and event.key == pg.K_f:
            pg.display.toggle_fullscreen()
        if event.type == pg.VIDEORESIZE:
            pg.display._resize_event(event)

    i, j = pg.mouse.get_pos()

    screen.fill(Color.tan)
    pg.draw.circle(screen, Color.yellowgreen, (i, j), 5)
    pg.draw.circle(screen, (0, 0, 0), (100, 100), 20)
    pg.draw.circle(screen, (0, 0, 200), (0, 0), 10)
    pg.draw.circle(screen, (200, 0, 0), (160, 120), 30)
    pg.draw.line(screen, (250, 250, 0), (0, 120), (160, 0))
    for i in range(16):
        pg.draw.rect(screen, Color.palette[i], (8*i + 1, 1, 7, 16), 0, 3)

    pg.display.flip()
    clock.tick(FPS)
pg.quit()
