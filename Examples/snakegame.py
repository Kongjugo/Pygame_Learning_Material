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
        if event.type == pygame.quit():
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

    # 벽을 만났을때와 몸에 부딪혔을떄 -> 게임 리셋
    if new_head in snake[2:] or new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
        sleep(1)
        reset_game()
    else:
        snake.insert(0, new_head)
        # length보다 snake 길이가 긴 경우 -> 제거
        if len(snake) > length:
            snake.pop()

# 뱀이 먹이를 먹었을 때
    # 뱀이 먹이와 충돌한 경우
def check():
    global length, feed_pos
    if snake[0] == feed_pos:
        length += 1
        return True
    return False

# 게임 정보 표시 
def draw_info():
    info = "Length : " + str(length) + "      " + "Speed : " + str(round(speed, 2)) # round 메소드 : 소수점 자리에 맞춰 반올림 (반올림할 숫자, 표시할 자리의 순서)
    font = pygame.font.SysFont('FixedSys', 30, False, False)
    text = font.render(info, True, GRAY)
    screen.blit(text, (10, 10)) # blit(문자열, (위치))

# 뱀 그리기 
def draw_snake():
    red, green, blue = 50 / max(length-1, 1), 50, 150 / max(length-1, 1) # 길이 증가 -> 몸통 색상 변화

    # enmerate(리스트트) : 리스트의 인덱스와 값을 동시에 가져오는 메소드 
    for i, p in enumerate(snake):
        color = (min(255, 100 + red * i), green, blue * i) 
        rect = pygame.Rect(p, (GRIZ_SIZE, GRIZ_SIZE))
        pygame.draw.rect(screen, color, rect)

# 먹이 그리기 
def draw_feed():
    rect = pygame.Rect(feed_pos, (GRIZ_SIZE, GRIZ_SIZE))
    pygame.draw.rect(screen, GREEN, rect)

# 먹이 위치 생성 
def create_feed():
    x = random.randint(0, GRID_WIDTH-1)
    y = random.randint(0, GRID_HEIGHT-1)
    return (x * GRIZ_SIZE, y * GRIZ_SIZE)

# 화면 업데이트
def draw_screen():
    screen.fill(WHITE)
    draw_info()
    draw_feed()
    draw_snake()
    pygame.display.flip()

# 게임 리셋
def reset_game():
    global snake, length, direction, feed_pos
    snake = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    direction = random.choice([UP, DOWN, RIGHT, LEFT])
    length = 2
    feed_pos = create_feed()

# 실행 로직
def main():
    # 전역 변수
    global speed, feed_pos
    feed_pos = create_feed()
    running = True

    # 반복문 
    while running:
        running = not handle() 
        move()
        if check():
            feed_pos = create_feed()
        speed = (10 + length) / 2
        draw_screen()
        clock.tick(speed)

    pygame.quit()

# 프로그램 시작 함수 설정
if __name__ == "__main__":
    main()
        
