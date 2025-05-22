import pygame
from time import sleep
import random

# 화면 크기 정의
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임 화면 분할
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 방향 변수
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

# 색상
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
GREEN = (0, 255, 0)

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("snake_game")
clock = pygame.time.Clock()

# 전역 변수
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
direction = random.choice([UP, DOWN, RIGHT, LEFT])
length = 2
feed_pos = (0, 0)
speed = 60

def handle():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
    return False

def move():
    global snake, length
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

    if (new_head in snake[2:] or
        new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
        sleep(1)
        reset_game()
    else:
        snake.insert(0, new_head)
        if len(snake) > length:
            snake.pop()

def check():
    global length, feed_pos
    if snake[0] == feed_pos:
        length += 1
        return True
    return False

def draw_info():
    info = f"Length : {length}      Speed : {round(speed, 2)}"
    font = pygame.font.SysFont('FixedSys', 30)
    text = font.render(info, True, GRAY)
    screen.blit(text, (10, 10))

def draw_snake():
    red, green, blue = 50 / max(length - 1, 1), 50, 150 / max(length - 1, 1)
    for i, p in enumerate(snake):
        color = (min(255, 100 + red * i), green, blue * i)
        rect = pygame.Rect(p, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, color, rect)

def draw_feed():
    rect = pygame.Rect(feed_pos, (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, GREEN, rect)

def create_feed():
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        pos = (x * GRID_SIZE, y * GRID_SIZE)
        if pos not in snake:
            return pos

def draw_screen():
    screen.fill(WHITE)
    draw_info()
    draw_feed()
    draw_snake()
    pygame.display.flip()

def reset_game():
    global snake, length, direction, feed_pos
    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    direction = random.choice([UP, DOWN, RIGHT, LEFT])
    length = 2
    feed_pos = create_feed()

def main():
    global speed, feed_pos
    feed_pos = create_feed()
    running = True

    while running:
        running = not handle()
        move()
        if check():
            feed_pos = create_feed()
        speed = min(30, (10 + length) / 2)
        draw_screen()
        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    main()
