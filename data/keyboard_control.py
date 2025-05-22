# 4월 16일 / 5월 7일
import pygame 
import os 

# 게임 스크린 크기 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# RGB 값 색상 지정
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Pink = (255, 192, 203)
Gray = (200, 200, 200)

# 초기화 
pygame.init()

# Window Name 설정
pygame.display.set_caption("Keyboard")

# Window 크기 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Screen Update
clock = pygame.time.Clock()

# 원 크기 및 색상 설정
circle_radius = 30
circle_color = Red

key_x = int(SCREEN_WIDTH / 2)
key_y = int(SCREEN_HEIGHT / 2)
key_dx = 0
key_dy = 0

# 게임 반복 구간
done = False

while not done:
    # Event 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # 키를 눌렀을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_dx = -3
            if event.key == pygame.K_RIGHT:
                key_dx = 3
            if event.key == pygame.K_UP:
                key_dy = -3
            if event.key == pygame.K_DOWN:
                key_dy = 3

        # 키를 뗐을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_dx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                key_dy = 0

    # 게임 로직 구간
    key_x += key_dx
    key_y += key_dy

    # 화면 삭제 및 채우기
    screen.fill(Black)

    # 원 그리기
    pygame.draw.circle(screen, circle_color, (key_x, key_y), circle_radius)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수
    clock.tick(60)

# 게임 종료
pygame.quit()
