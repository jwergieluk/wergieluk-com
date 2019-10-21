---
title: "Dashboard for an automated trading system with pygame"
date: 2019-10-17
lastmod: 2019-10-17
draft: true
markup: "mmark"
---

Recently I've spent some time coding a dashboard for my automated trading system, and I am quite happy with the result: 

{{< figure src="/periscope/periscope-dashboard-0.gif" title="Dashboard" >}}

What's a bit unusual about this project is the use of pygame, a Python game development package, instead of a web-based dashboard library (like Dash or Bokeh) or a GUI framework. 

Pygame is effectively a wrapper around SDL library. It is super-simple and easy learn and fun to and work with. It doesn't offer any standard GUI elements like buttons and windows, but it is surprisingly easy to write those from scratch. 

I this post I go over some basics of pygame for non-interactive use (no user interaction) and show how to use that small subset of pygame features for develop a (static) dashboard to display some text and plots. (By static dashboard I mean that positions of all GUI elements are defined in the code and e.g. those windows on the dashboard snapshot above cannot be moved at run-time.)

# A quick pygame tutorial

Initialize pygame and get the screen surface. 

    import pygame
    pygame.init()
    pygame.mixer.quit()
    screen_surface = pygame.display.set_mode((120, 80))
    pygame.display.flip()

{{< figure src="/periscope/pygame-0.png" >}}

A surface is a bitmap and it's a fundamental concept in pygame. Essentially, a pygame app defines multiple surfaces, modifies their content (pixels) and copies one surface onto another. This resembles playing with multiple post-it notes of different sizes. A screen surface is linked to the pygame window at run-time. We can update that window using the `display.flip()` method. For example, let's fill the screen surface with a color and update screen.

    color_fg, color_bg = pygame.Color(0xfff31bff), pygame.Color(0x1e2320ff)
    screen_surface.fill(color_bg)
    pygame.display.flip()

Creating a surface: 

    another_surface = pygame.Surface((20, 20))
    another_surface.fill(color_fg)

A surface has width and height:

    w, h = another_surface.get_width(), another_surface.get_height()

Blitting (copying) one surface onto another:

    where_x, where_y = 10, 10
    screen_surface.blit(another_surface, (where_x, where_y))

{{< figure src="/periscope/pygame-1.png" >}}

Fonts: 

    font_name, font_size = 'inconsolata', 32
    font = pygame.font.SysFont(font_name, font_size)
    text_surface = font.render('A', True, color_fg, color_bg)
    screen_surface.blit(text_surface, (65, 57))

{{< figure src="/periscope/pygame-2.png" >}}

Draw an (anti-aliased) line from the lower-left corner to the upper-right corner of the screen surface:

    x_y_tuples = [(0, 79), (119, 0)]
    pygame.draw.aalines(screen_surface, color_fg, False, x_y_tuples)

{{< figure src="/periscope/pygame-3.png" >}}

# Widgets

## TextField

## LinePlot

{{< figure src="/periscope/periscope-lineplot-0.gif" >}}

## HStack and VStack




# References

https://github.com/kitao/pyxel
