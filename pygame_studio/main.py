import pygame


def main_init():
    pygame.init()

def main():
    main_init()
    running = True
    screen = pygame.display.set_mode(size=(500, 500))
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()