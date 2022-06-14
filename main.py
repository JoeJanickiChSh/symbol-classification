from weightmap import WeightMap
import pygame as pg
import image

model_dict = {
    'A': 'letter_A.json',
    'B': 'letter_B.json',
    'C': 'letter_C.json',
    'D': 'letter_D.json',
    'E': 'letter_E.json',
}

for key in model_dict:
    with open(model_dict[key], 'r') as fp:
        model_dict[key] = WeightMap.from_json(fp.read())


def main():
    pg.display.set_caption('Symbol Classification')
    d = pg.display.set_mode((512, 512))

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
                    max_conf = 0
                    guess = 'None'
                    for wm in model_dict:
                        conf = model_dict[wm].get_confidence(new_wm)
                        if conf > max_conf:
                            max_conf = conf
                            guess = wm

                    print(guess)

        mousex, mousey = pg.mouse.get_pos()
        mouse_down = pg.mouse.get_pressed()[0]

        if mouse_down:
            pg.draw.line(d, (0, 0, 0), (mousex, mousey),
                         (p_mousex, p_mousey), 4)

        p_mousex, p_mousey = mousex, mousey
        pg.display.update()


if __name__ == '__main__':
    main()
