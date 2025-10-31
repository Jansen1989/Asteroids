import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # FPS Begrenzung
    clock = pygame.time.Clock()
    dt = 0

    # Fenster erzeugen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Spieler erzeugen
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Bildschirm füllen
        screen.fill("black")
        
        # Spieler anzeigen
        player.draw(screen)
        # Anzeige aktualisieren
        pygame.display.flip()

        # Begrenzen der FPS auf 60 
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()
