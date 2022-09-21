import pygame as pg
from color import Color

pg.init()
RES = (160, 120)
FPS = 24
clock = pg.time.Clock()
screen = pg.display.set_mode(RES, pg.SCALED | pg.RESIZABLE)

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

    i, j = pg.mouse.get_pos()
    emit_and_average_co2(i, j)

    screen.fill(Color.tan)
    s = pg.transform.smoothscale(co2, RES)
    screen.blit(s, (0, 0))

    pg.display.flip()
    clock.tick(FPS)
pg.quit()
