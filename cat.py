import pygame

pygame.init()

SCREEN_W = 800
SCREEN_H = 800
FPS = 140
BLUE = "#65A1E0"
PURPLE = "#7865E0"

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("catpaw")
clock = pygame.time.Clock()
paw_surface = pygame.image.load("catpawww.png").convert_alpha()
paw_width, paw_height = paw_surface.get_size()
rectangle_surface = pygame.Surface((180, SCREEN_H))
rectangle_surface.fill(PURPLE)
rectangle_hid = pygame.Surface((180, SCREEN_H))
rectangle_hid.fill(BLUE)
rectangle_rect = rectangle_surface.get_rect(topleft=(0, 0)),
rectangle_rect = rectangle_hid.get_rect(topleft=(180, 0))

z = 0
y = 0
x = 0
direction_y = 20
direction_x = 40
rot_values = list(range(290, 240, -1))
rot_index = 2
forward_rotation = True
rotation_speed = 4

is_mouse_colliding = False

run = True
while run:
    clock.tick(60)
    screen.fill((BLUE))
    screen.blit(rectangle_surface, (0, 0))
    pygame.display.flip()

    mouse_pos = pygame.mouse.get_pos()
    
    if rectangle_rect.collidepoint(mouse_pos):
        is_mouse_colliding = True
        rot_val = rot_values[rot_index]
        z += direction_x
        y += direction_y
        if z <= -500 or z >= SCREEN_W - 700:
            direction_x *= -1
        if y <= -1 or y >= SCREEN_H - 500:
            direction_y *= -1
        rotated_image = pygame.transform.rotate(paw_surface, rot_val)
        screen.blit(rectangle_hid, (180, 0))
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
        if is_mouse_colliding:
            is_mouse_colliding = False
            # Reset position and rotation
            x = 0
            y = 0
            rot_index = 2


    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
