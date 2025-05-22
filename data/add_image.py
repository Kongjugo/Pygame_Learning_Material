# 4월 16일 (이미지 첨부)

import pygame 
import os 

# 게임 스크린 크기 
SCREEN_WIDTH = 630
SCREEN_HEIGHT = 600

# RGB 값 색상 지정
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Pink = (255, 192, 203)
Gray = (200, 200, 200)

LAND = (160, 120, 40)

# 초기화 
pygame.init()

# Window Name 설정
pygame.display.set_caption("Image")

# Window 크기 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Screen Update
clock = pygame.time.Clock()

# Setting a path
current_path = os.path.dirname(__file__)
asset_path = os.path.join(current_path, 'assets')

# background image
backgroun_image = pygame.image.load(os.path.join(asset_path, 'dfaf.png'))

# image load
image1 = pygame.image.load(os.path.join(asset_path, 'dd.png'))


# 게임 반복 구간
done = False

while not done: # While True
    # Event 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    # 게임 로직 구간

    # 화면 삭제 구간

    # 스크린 채우기 
    screen.blit(backgroun_image, backgroun_image.get_rect()) # get_rect() 메소드 함수는 이미지 채우기
    screen.blit(image1, [0, 420])

    # 화면 그리기

    # 화면 업데이트
    pygame.display.flip()

    # 초당 업데이트 횟수
    clock.tick(60)

# 게임 종료
pygame.quit()
