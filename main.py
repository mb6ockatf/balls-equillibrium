#!/usr/bin/env python3
import pygame


pygame.init()
width = int(input("width: "))
height = int(input("height: "))
screen = pygame.display.set_mode((width, height))
cur_circle_rad = 10
breaker = 1
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
speed = 10
runner = True
cords = None
balls = []


def reverse(bool_arg):
    return False if bool_arg is True else True


screen.fill(black)
while runner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breaker = 0
            runner = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = event.pos
            _cords = {"width": cords[0], "height": cords[1]}
            _direction = {"left": True, "top": True}
            ball = {"cords": _cords, "direction": _direction}
            balls += [ball]
            breaker = 0
    screen.fill(black)
    for j in balls:
        direction = j["direction"]
        if j["cords"]["width"] <= 10 or width - 10 <= j["cords"]["width"]:
            value = j["direction"]["left"]
            j["direction"]["left"] = reverse(value)
        elif j["cords"]["height"] <= 10 or height - 10 <= j["cords"]["height"]:
            value = j["direction"]["top"]
            j["direction"]["top"] = reverse(value)
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
    clock.tick(10)
    pygame.display.update()
pygame.quit()
