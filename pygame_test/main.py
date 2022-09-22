import pygame as pg
from color import Color

pg.init()
RES = (160, 120)
FPS = 24
clock = pg.time.Clock()
screen = pg.display.set_mode(RES, pg.SCALED | pg.RESIZABLE)

# CO2
CO2_RES = (RES[0]//4, RES[1]//4)
co2 = pg.Surface(CO2_RES, pg.SRCALPHA)
co2_color = Color.blue
co2.fill(co2_color + (0,))
def emit_and_average_co2(x, y):
    global co2
    tmp = pg.transform.smoothscale(co2, RES)
    pg.draw.circle(tmp, co2_color, (x, y), 4)
    pg.draw.rect(tmp, co2_color + (0,), (0, 0) + RES, 4)
    co2 = pg.transform.smoothscale(tmp, CO2_RES)

# Hytty
hytty = (RES[0]//2, RES[1]-12)
import functools
def navigate_hytty():
    global hytty
    pos = (hytty[0]//4, hytty[1]//4)
    dirs = ((-1, -1), (1, 1), (1, -1), (-1, 1),)
    dir, max = 0, 0
    try:
        max = co2.get_at((pos[0]+dirs[0][0], pos[1]+dirs[0][1]))[3]
    except IndexError: pass
    try:
        if (m := co2.get_at((pos[0]+dirs[1][0], pos[1]+dirs[1][1]))[3]) > max: dir, max = 1, m
    except IndexError: pass
    try:
        if (m := co2.get_at((pos[0]+dirs[2][0], pos[1]+dirs[2][1]))[3]) > max: dir, max = 2, m
    except IndexError: pass
    try:
        if (m := co2.get_at((pos[0]+dirs[3][0], pos[1]+dirs[3][1]))[3]) > max: dir, max = 3, m
    except IndexError: pass
    hytty = (hytty[0]+dirs[dir][0], hytty[1]+dirs[dir][1])

# Main loop
i = 0
j = 0
done = False
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

    # Draw and update CO2
    i, j = pg.mouse.get_pos()
    emit_and_average_co2(i, j)
    screen.fill(Color.tan)
    s = pg.transform.smoothscale(co2, RES)
    screen.blit(s, (0, 0))

    # Draw and update hytty
    pg.draw.circle(screen, Color.lightblue, hytty, 1)
    navigate_hytty()

    pg.display.flip()
    clock.tick(FPS)
pg.quit()
