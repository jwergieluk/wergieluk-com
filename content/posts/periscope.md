---
title: "Pygame dashboard for algo trading"
date: 2019-10-17
lastmod: 2019-10-22
draft: true
markup: "mmark"
---

Recently I've spent some time coding a dashboard for my algo trading system, and I am quite happy with the result: 

{{< figure src="/periscope/periscope-dashboard-0.gif" title="Dashboard" >}}

What's a bit unusual about this project is the use of pygame, a Python game development package, instead of a web-based dashboard library (like Dash or Bokeh) or a GUI framework. 

Pygame is effectively a wrapper around SDL library. It is super-simple and easy learn and fun to and work with. It doesn't offer any standard GUI elements like buttons and windows, but it is surprisingly easy to write those from scratch. 

In this post I go over some basics of pygame for non-interactive use (no user interaction) and show how to use that small subset of pygame features for develop a (static) dashboard to display some text and plots. (By static dashboard I mean that positions of all GUI elements are defined in the code and e.g. those windows on the dashboard snapshot above cannot be moved at run-time.)

# A quick pygame tutorial

Initialize pygame and get the screen surface. 

    import pygame
    pygame.init()
    screen_surface = pygame.display.set_mode((120, 80))
    pygame.display.flip()

{{< figure src="/periscope/pygame-0.png" >}}

A surface is a bitmap and it's a fundamental concept in pygame. Essentially, a pygame app defines multiple surfaces, modifies their content (pixels) and copies one surface onto another. This resembles playing with multiple post-it notes of different sizes. A screen surface is linked to the pygame window at run-time. We can update that window using the `pygame.display.flip()` method. For example, let's fill the screen surface with a color and update.

    color_fg, color_bg = pygame.Color(0xfff31bff), pygame.Color(0x1e2320ff)
    screen_surface.fill(color_bg)
    pygame.display.flip()

{{< figure src="/periscope/pygame-1.png" >}}

Creating a surface: 

    another_surface = pygame.Surface((20, 20))
    another_surface.fill(color_fg)

A surface has width and height:

    w, h = another_surface.get_width(), another_surface.get_height()

Blitting (copying) one surface onto another:

    where_x, where_y = 10, 10
    screen_surface.blit(another_surface, (where_x, where_y))

{{< figure src="/periscope/pygame-2.png" >}}

Fonts: 

    font_name, font_size = 'inconsolata', 32
    font = pygame.font.SysFont(font_name, font_size)
    text_surface = font.render('A', True, color_fg, color_bg)
    screen_surface.blit(text_surface, (65, 57))

{{< figure src="/periscope/pygame-3.png" >}}

Draw an (anti-aliased) line from the lower-left corner to the upper-right corner of the screen surface:

    x_y_tuples = [(0, 79), (119, 0)]
    pygame.draw.aalines(screen_surface, color_fg, False, x_y_tuples)

{{< figure src="/periscope/pygame-4.png" >}}

That's all we need to know about pygame to write a simple dashboard.

# Widgets

## TextField

    text_field_0 = TextField(250, 'Text field with width 250')

{{< figure src="/periscope/text-field-0.png" >}}

## LinePlot

    x = np.linspace(0.0, 2*np.pi, 100)
    line_plot_0 = LinePlot(120, 80)
    line_plot_0.set_content(x, np.sin(x))

{{< figure src="/periscope/line-plot-0.png" >}}

{{< figure src="/periscope/periscope-lineplot-0.gif" >}}

## HStack and VStack

    text_field_1 = TextField(90, 'TextField1')
    text_field_2 = TextField(90, 'TextField2')
    text_field_3 = TextField(90, 'TextField3')
    h_stack = HStack([text_field_1, text_field_2, text_field_3])
    v_stack = VStack([text_field_1, text_field_2, text_field_3])
    text_field_2.set_content('Field2')


{{< figure src="/periscope/h-stack-0.png" >}}
{{< figure src="/periscope/v-stack-0.png" >}}


# References

https://github.com/kitao/pyxel
