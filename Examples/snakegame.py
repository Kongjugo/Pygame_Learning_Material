import pygame
from time import sleep
import random

# 화면 크기 정의
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임 화면 분할
GRIZ_SIZE = 20
GRID_WIDTH = int(SCREEN_WIDTH/GRIZ_SIZE)
GRID_HEIGHT = int(SCREEN_HEIGHT/GRIZ_SIZE)

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

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 제목 정의 
pygame.display.set_caption("snake_game")

# clock 설정
clock = pygame.time.Clock()

# 전역 변수
snake = [(SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)]
direction = random.choice([UP, DOWN, RIGHT, LEFT])
length = 2
feed_pos = (0, 0)
speed = 60 

# 방향 제어 함수
def handle():
    global direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
        return False        

# 뱀 이동 함수 
def move():
    global snake, length
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx * GRIZ_SIZE, head_y + dy * GRIZ_SIZE)

    # 벽을 만났을때 -> 게임 리셋
    if new_head in snake[2:] or new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
        
