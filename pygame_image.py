import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_image = pg.image.load("fig/3.png")
    kk_image = pg.transform.flip(kk_image, True, False)
    kk_rect = kk_image.get_rect()
    kk_rect.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed()
        
        dx, dy = -1, 0
        if key_list[pg.K_UP]:
            dy -= 1
        if key_list[pg.K_DOWN]:
            dy += 1
        if key_list[pg.K_RIGHT]:
            dx += 1
        if key_list[pg.K_LEFT]:
            dx -= 1
        kk_rect.move_ip(dx, dy)

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])

        screen.blit(kk_image, kk_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()