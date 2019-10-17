---
title: "Dashboard for an automated trading system with pygame"
date: 2019-10-17
lastmod: 2019-10-17
draft: true
markup: "mmark"
---

Pygame is super-simple and easy to use. 

# Fastest pygame tutorial on earth

* Covers non-interactive use.

Initialize pygame and get the screen surface. 

    import pygame
    pygame.init()
    pygame.mixer.quit()
    surface = pygame.display.set_mode((320, 240))

{{< figure src="/periscope/pygame-0.png" >}}

Fill the screen with a color and update screen.

    COLOR_BACKGROUND_0 = pygame.Color(0x1e2320ff)
    screen.fill(COLOR_BACKGROUND_0)
    pygame.display.flip()

Create a free surface: 

    another_surface = pygame.Surface((100, 100))

Blitting (copy one surface onto another)

    surface.blit(another_surface, (where_x, where_y))

Surface width and height

    w, h = surface.get_width(), surface.get_height()
    
Text

{{< figure src="/periscope/periscope-dashboard-0.gif" title="Dashboard" >}}

{{< figure src="/periscope/periscope-lineplot-0.gif" title="Line plot" >}}






https://github.com/kitao/pyxel
