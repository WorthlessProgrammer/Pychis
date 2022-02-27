import sys
import pygame

BOARD_FILE = "Tablero_parchis_2.png"
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SCREEN_OFFSET = 100

if __name__=="__main__":

    #inicialització del joc
    pygame.init()

    #càrrega de pantalla
    size = [SCREEN_WIDTH + SCREEN_OFFSET, SCREEN_HEIGHT + SCREEN_OFFSET]
    screen = pygame.display.set_mode(size)
    
    #càrrega del tauler
    board = pygame.image.load(BOARD_FILE).convert()

    #nom de la finestra
    pygame.display.set_caption("Parchis")

    while True:

        # completely fill the surface object
        # with white colour
        #screen.fill((255, 255, 255))

        # copiem la imatge a la pantalla
        screen.blit(board, (SCREEN_OFFSET // 2, SCREEN_OFFSET // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Dibuixa l'objecte screen a la pantalla.
            pygame.display.update()





