from weightmap import WeightMap
import pygame as pg
import image
from glob import glob


def main():
    model_name = input('Model Name? ')

    pg.display.set_caption(f'Model Trainer - {model_name}')
    d = pg.display.set_mode((512, 512))

    if f'{model_name}.json' in glob('*.json'):
        with open(f'{model_name}.json') as fp:
            wm = WeightMap.from_json(fp.read())
    else:
        wm = WeightMap(32, 32)
    d.fill((255, 255, 255))
    p_mousex, p_mousey = 0, 0
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()

            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_c:
                    d.fill((255, 255, 255))
                elif e.key == pg.K_SPACE:
                    cropped = image.scale(d, 32, 32)
                    new_wm = WeightMap.from_pg_surface(cropped)
                    wm.train(new_wm)
                    with open(f'{model_name}.json', 'w') as fp:
                        fp.write(wm.to_json())
                    d.fill((255, 255, 255))

        mousex, mousey = pg.mouse.get_pos()
        mouse_down = pg.mouse.get_pressed()[0]

        if mouse_down:
            pg.draw.line(d, (0, 0, 0), (mousex, mousey),
                         (p_mousex, p_mousey), 4)

        p_mousex, p_mousey = mousex, mousey
        pg.display.update()


if __name__ == '__main__':
    main()
