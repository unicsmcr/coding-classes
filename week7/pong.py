import pygame
import sys
import math
# Pong game made by lewis from https://codereview.stackexchange.com/questions/33289/basic-pong-game-in-pygame

class Ball(object):
    def __init__(self, x, y, width, height, vx, vy, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.colour = colour

    def render(self, screen):
        pygame.draw.ellipse(screen, self.colour, self.rect)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Paddle(object):
    def __init__(self, x, y, width, height, speed, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.speed = speed
        self.colour = colour

    def render(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def update(self):
        self.x += self.vx

    def key_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vx = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.vx = self.speed
        elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.vx = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)   


class Pong(object):
    COLOURS = {"BLACK": (  0,   0,   0),
               "WHITE": (255, 255, 255),
               "RED"  : (255,   0,   0)}
    def __init__(self):
        pygame.init()
        (WIDTH, HEIGHT) = (640, 480)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Lewis' Pong")
        self.ball = Ball(5, 5, 50, 50, 5, 5, Pong.COLOURS["BLACK"])
        self.paddle = Paddle(WIDTH / 2, HEIGHT - 50, 100,
                             10, 3, Pong.COLOURS["BLACK"])
        self.score = 0

    def play(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    self.paddle.key_handler(event)

            self.collision_handler()
            self.draw()

    def collision_handler(self):
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.vy = -self.ball.vy
            self.score += 1

        if self.ball.x + self.ball.width >= self.screen.get_width():
            self.ball.vx = -(math.fabs(self.ball.vx))
        elif self.ball.x <= 0:
            self.ball.vx = math.fabs(self.ball.vx)

        if self.ball.y + self.ball.height >= self.screen.get_height():
            pygame.quit()
            sys.exit()
        elif self.ball.y <= 0:
            self.ball.vy = math.fabs(self.ball.vy)

        if self.paddle.x + self.paddle.width >= self.screen.get_width():
            self.paddle.x = self.screen.get_width() - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0

    def draw(self):
        self.screen.fill(Pong.COLOURS["WHITE"])

        font = pygame.font.Font(None, 48)
        score_text = font.render("Score: " + str(self.score), True,
                                 Pong.COLOURS["RED"])
        self.screen.blit(score_text, (0, 0))

        self.ball.update()
        self.ball.render(self.screen)
        self.paddle.update()
        self.paddle.render(self.screen)

        pygame.display.update()

if __name__ == "__main__":
    Pong().play()
