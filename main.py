import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Fenster erzeugen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    running = True
    while running:
        # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Bildschirm füllen
        screen.fill("black")
        
        # Anzeige aktualisieren
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
