from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shots_grp):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
        self.shots_group = shots_grp
        self.reload_time = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: ## left
            self.rotate(-dt) 
        if keys[pygame.K_RIGHT]: ## right
            self.rotate(dt) 

        if keys[pygame.K_UP]: ## forward
            self.move(dt)  
        if keys[pygame.K_DOWN]: ## back
            self.move(-dt) 

        self.reload_time -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if (self.reload_time > 0):
            pass
        else:
            shot = Shot(self.position.x, self.position.y)
            self.shots_group.add(shot)
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity += shot_velocity * PLAYER_SHOOT_SPEED
            self.reload_time += PLAYER_SHOOT_COOLDOWN
