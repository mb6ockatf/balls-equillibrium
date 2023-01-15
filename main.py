#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


pygame.init()
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
try:
    width = int(input("width: "))
    height = int(input("height: "))
    speed = int(input("FPS: "))
except ValueError:
    print("size and FPS values must be integers")
    pygame.quit()
    exit(1)
if width > screen_width or height > screen_height:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width = screen_width
    height = screen_height
else:
    screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
is_running = True
cur_circle_rad = 10
cords = None
balls = []
screen.fill(black)
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = event.pos
            _cords = {"width": cords[0], "height": cords[1]}
            _direction = {"left": True, "top": True}
            ball = {"cords": _cords, "direction": _direction}
            balls += [ball]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
    screen.fill(black)
    for j in balls:
        direction = j["direction"]
        if j["cords"]["width"] <= 10 or width - 10 <= j["cords"]["width"]:
            value = j["direction"]["left"]
            j["direction"]["left"] = not value
        elif j["cords"]["height"] <= 10 or height - 10 <= j["cords"]["height"]:
            value = j["direction"]["top"]
            j["direction"]["top"] = not value
        if j["direction"]["left"]:
            j["cords"]["width"] -= 10
            if j["direction"]["top"]:
                j["cords"]["height"] -= 10
            else:
                j["cords"]["height"] += 10
        else:
            j["cords"]["width"] += 10
            if j["direction"]["top"]:
                j["cords"]["height"] -= 10
            else:
                j["cords"]["height"] += 10
    for j in balls:
        cords = (j["cords"]["width"], j["cords"]["height"])
        pygame.draw.circle(screen, white, cords, cur_circle_rad)
    clock.tick(speed)
    pygame.display.update()
pygame.quit()

