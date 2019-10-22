import pygame


def flip_and_save(surface0, i: int):
    pygame.display.flip()
    pygame.image.save(surface0, f'pygame-{i}.png')


pygame.init()
pygame.mixer.quit()

screen_surface = pygame.display.set_mode((120, 80))
flip_and_save(screen_surface, 0)

color_fg, color_bg = pygame.Color(0xfff31bff), pygame.Color(0x1e2320ff)
screen_surface.fill(color_bg)
flip_and_save(screen_surface, 1)

another_surface = pygame.Surface((20, 20))
another_surface.fill(color_fg)
where_x, where_y = 10, 10
screen_surface.blit(another_surface, (where_x, where_y))

flip_and_save(screen_surface, 2)

font_name, font_size = 'inconsolata', 32
font = pygame.font.SysFont(font_name, font_size)
text_surface = font.render('A', True, color_fg, color_bg)

screen_surface.blit(text_surface, (65, 57))
flip_and_save(screen_surface, 3)

x_y_tuples = [(0, 79), (119, 0)]
pygame.draw.aalines(screen_surface, color_fg, False, x_y_tuples)
flip_and_save(screen_surface, 4)

pygame.quit()
