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
direction_y = 10
direction_x = 40
rot_values = list(range(290, 240, -1))
rot_index = 0
forward_rotation = True
rotation_speed = 6

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("catpaw")
clock = pygame.time.Clock()

paw_surface = pygame.image.load("catpawww.png").convert_alpha()
paw_width, paw_height = paw_surface.get_size()
mouse = pygame.image.load("mouse.png").convert_alpha()
mouse_width = 100
mouse_height = 100
mouse = pygame.transform.scale(mouse, (mouse_width, mouse_height))

rectangle_surface = pygame.Surface((180, SCREEN_H))
rectangle_surface.fill(PURPLE)
rectangle_rect = rectangle_surface.get_rect(topleft=(0, 0))

run = True
while run:
    clock.tick(60)
    screen.fill((BLUE))

    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos:
        mouse_rect = mouse.get_rect(center=mouse_pos)
        screen.blit(mouse, mouse_rect.topleft)
        if rectangle_rect.collidepoint(mouse_pos):
            rot_val = rot_values[rot_index]
            z += direction_x
            y += direction_y
            if z <= -400 or z >= SCREEN_W - 700:
                direction_x *= -1
            if y <= -1 or y >= SCREEN_H - 500:
                direction_y *= -1
            rotated_image = pygame.transform.rotate(paw_surface, rot_val)
            screen.blit(rotated_image, (z, y))
            screen.blit(rectangle_surface, (0, 0))
            pygame.display.flip()
            if forward_rotation:
                rot_index += rotation_speed
                if rot_index >= len(rot_values):
                    rot_index = len(rot_values) - 2
                    forward_rotation = False
            else:
                rot_index -= rotation_speed
                if rot_index < 0:
                    rot_index = 1
                    forward_rotation = True
        else:
            print("ass")


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

pygame.quit()
