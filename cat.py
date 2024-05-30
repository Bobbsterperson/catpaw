import pygame

pygame.init()

SCREEN_W = 800
SCREEN_H = 800
FPS = 60
BLUE = "#65A1E0"
PURPLE = "#7865E0"

z = 0
y = 0
x = 0
direction_y = 20
direction_x = 20

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("catpaw")
clock = pygame.time.Clock()

paw_surface = pygame.image.load("catpawww.png").convert_alpha()
paw_width, paw_height = paw_surface.get_size()
rotated_image = pygame.transform.rotate(paw_surface, 270)

rectangle_surface = pygame.Surface((150, SCREEN_H))
rectangle_surface.fill(PURPLE)

run = True
while run:

    z += direction_x
    y += direction_y
    if z <= -500 or z >= SCREEN_W - 700:
        direction_x *= -1
    if y <= -500 or y >= SCREEN_H - 100:
        direction_y *= -1

    clock.tick(60)
    screen.fill((BLUE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(rotated_image, (z, y))
    screen.blit(rectangle_surface, (0, 0))

    pygame.display.flip()

pygame.quit()
