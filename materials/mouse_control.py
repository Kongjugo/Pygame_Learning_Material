import pygame 
import os

# 게임 스크린 크기 
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 600

# RGB 값 색상 지정
Black = (0, 0, 0)

# 초기화 
pygame.init()

# Window Name 설정
pygame.display.set_caption("Mouse")

# Window 크기 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Screen Update
clock = pygame.time.Clock()

# 이미지 폴더 경로 설정
current_path = os.path.dirname(__file__)
asset_path = os.path.join(current_path, 'assets')

# 배경 이미지 설정
background = pygame.image.load(os.path.join(asset_path, 'music.png'))

# 음악 설정 
pygame.mixer.music.load(os.path.join(asset_path, 'edm.mp3'))
pygame.mixer.music.play(-1)

# 효과음 설정
sound = pygame.mixer.Sound(os.path.join(asset_path, 'clack.mp3'))

# 이미지 초기 설정
'''mouse_img = pygame.image.load(os.path.join(asset_path, 'hand.png'))
mouse_x = int(SCREEN_WIDTH/2)
mouse_y = int(SCREEN_HEIGHT/2)'''

# 마우스 포인터 삭제
'''pygame.mouse.set_visible(False)'''

# 게임 반복 구간
done = False
while not done: # While True
    # Event 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
        
    
    # 마우스 위치값 가져오기
    '''pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]'''

    # 스크린 채우기 
    screen.fill(Black)
    '''screen.blit(mouse_img, [mouse_x, mouse_y])''' 
    screen.blit(background, background.get_rect())

    # 화면 업데이트
    pygame.display.flip()

    # 초당 업데이트 횟수
    clock.tick(60)

# 게임 종료
pygame.quit()
