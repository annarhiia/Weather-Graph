def display():
    import pygame
    import weather
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        MOUSEBUTTONDOWN,
    )

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    buttonX = 650
    buttonY = 50

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))

    f = open('graph.png')
    plot_img = pygame.image.load('graph.png')
    screen.blit(plot_img, (0, 0))

    b = open('Button.png')
    button_img = pygame.image.load('Button.png')
    screen.blit(button_img, (650, 50))

    pygame.display.flip()

    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            if buttonX <= mouseX <= buttonX + 81 and buttonY <= mouseY <= buttonY + 69 and event.type == pygame.MOUSEBUTTONDOWN:
                weather.graph()
                running = False
                pygame.quit()

