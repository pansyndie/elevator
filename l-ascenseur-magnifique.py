import pygame as pg
import text
import scenes

# main screen settings #
scrColor = (255, 255, 255)
size = width, height = 1152, 768
screen = pg.display.set_mode((size))
pg.display.set_caption("The Grand Elevator")
########################


def main():
    #setting up main loop flag and fps tick variable
    clock = pg.time.Clock()
    running = True

    #setting up scenes variable, starting with the menu
    activeScene = scenes.MainMenu(screen)
    activeScene.render()

    while running:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            else:
                activeScene.process_event(event)

        activeScene = activeScene.next

        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()