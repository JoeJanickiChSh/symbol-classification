import pygame as pg


def find_y(surf, direction):
    val = 0
    scanning = True
    y = 0
    if direction == -1:
        y = surf.get_height()-1

    while scanning:
        for x in range(surf.get_width()):
            if surf.get_at((x, y))[0] < 127:
                scanning = False
                val = y
                break
        y += direction
        if y not in range(surf.get_height()):
            return 0

    return val


def find_x(surf, direction):
    val = 0
    scanning = True
    x = 0
    if direction == -1:
        x = surf.get_width()-1

    while scanning:
        for y in range(surf.get_height()):
            if surf.get_at((x, y))[0] < 127:
                scanning = False
                val = x
                break
        x += direction
        if x not in range(surf.get_width()):
            return 0

    return val


def crop(surf):
    top = find_y(surf, 1)
    bottom = find_y(surf, -1)
    left = find_x(surf, 1)
    right = find_x(surf, -1)

    out = pg.Surface((right-left, bottom-top))
    out.blit(surf, (-left, -top))

    return out


def scale(surf, width, height):
    return pg.transform.smoothscale(crop(surf), (width, height))
