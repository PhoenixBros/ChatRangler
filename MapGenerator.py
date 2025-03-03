import pygame as pg

pg.init()

joyce = None
joysticks = []
for event in pg.event.get():
    if event.type == pg.JOYDEVICEADDED:
        joy = pg.joystick.Joystick(event.device_index)
        joysticks.append(joy)