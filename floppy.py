import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 150
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

bird_image = pygame.Surface((34, 24)) 
bird_image.fill((255, 255, 0))
pipe_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_image.fill(GREEN)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 400)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self):
        screen.blit(pipe_image, (self.x, self.height - PIPE_HEIGHT))
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

def main():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        screen.fill(WHITE)
        bird.update()
        bird.draw()

        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()
            pipe.draw()

            if pipe.x < bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + 24 > pipe.height + PIPE_GAP:
                    running = False

            if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
                score += 1
                pipe.passed = True

        if bird.y > SCREEN_HEIGHT or bird.y < 0:
            running = False

        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()