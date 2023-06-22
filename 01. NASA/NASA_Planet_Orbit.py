"""
Created by Sk. Salahuddin
This is copyright project
"""
import math
import pygame
from pygame.locals import *

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1800

SUN_RADIUS = 50

# Planet data: name, radius, orbit radius, orbit speed, color
PLANETS = [
    ("Mercury", 10, 100, 0.02, pygame.Color("#A9A9A9")),  # Gray
    ("Venus", 15, 150, 0.015, pygame.Color("#FFA500")),  # Orange
    ("Earth", 20, 200, 0.01, pygame.Color("#0000FF")),  # Blue
    ("Mars", 17, 250, 0.008, pygame.Color("#FF0000")),  # Red
    ("Jupiter", 40, 350, 0.005, pygame.Color("#FFD700")),  # Gold
    ("Saturn", 35, 450, 0.004, pygame.Color("#D2B48C")),  # Tan
    ("Uranus", 30, 550, 0.003, pygame.Color("#00FFFF")),  # Cyan
    ("Neptune", 30, 650, 0.002, pygame.Color("#00008B")),  # Dark Blue
    ("Pluto", 8, 750, 0.001, pygame.Color("#A0522D"))  # Brown
]

class CelestialBody:
    def __init__(self, name, radius, orbit_radius, orbit_speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.color = color
        self.angle = 0

    def update(self, dt):
        self.angle += self.orbit_speed * dt

    def get_position(self):
        x = SCREEN_WIDTH // 2 + math.cos(self.angle) * self.orbit_radius
        y = SCREEN_HEIGHT // 2 + math.sin(self.angle) * self.orbit_radius
        return x, y

    def draw(self, surface):
        x, y = self.get_position()
        pygame.draw.circle(surface, self.color, (int(x), int(y)), self.radius)

        # Draw planet name
        font = pygame.font.Font(None, 20)
        text = font.render(self.name, True, (255, 255, 255))
        text_rect = text.get_rect(center=(int(x), int(y)))
        surface.blit(text, text_rect)

        # Draw orbit circle
        pygame.draw.circle(surface, self.color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.orbit_radius, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Solar System Simulator")

    sun = CelestialBody("Sun", SUN_RADIUS, 0, 0, pygame.Color("yellow"))
    planets = []

    for planet_data in PLANETS:
        name, radius, orbit_radius, orbit_speed, color = planet_data
        planet = CelestialBody(name, radius, orbit_radius, orbit_speed, color)
        planets.append(planet)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False

        screen.fill((0, 0, 0))  # Clear the screen

        for planet in planets:
            planet.update(dt)
            planet.draw(screen)
        sun.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
