import pygame
import os
import random

# 게임 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEGIHT = 600

# 색상 지정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (250, 170, 70)

# FPS 설정 (프레임 설정)
FPS = 60

# 초기화 
pygame.init()
pygame.font.init()
pygame.mixer.init()

# 파일 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

bounce_sound = pygame.mixer.Sound(os.path.join(assets_path, 'bgm.mp3'))
ping_sound = pygame.mixer.Sound(os.path.join(assets_path, 'ping.mp3'))
pong_sound = pygame.mixer.Sound(os.path.join(assets_path, 'pong.mp3'))

font = pygame.font.Font(os.path.join(assets_path, 'Pretendard-Medium.otf'))

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEGIHT))
pygame.display.set_caption("ping pong game")
pygame.display.set_icon()
clock = pygame.time.Clock()

# 기타 변수 설정
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEGIHT // 2, 12, 12)
ball_dx = random.choice([-3, 3])
ball_dy = 5

player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEGIHT - 40, 50, 15)
player_dx = 0

computer = pygame.Rect(SCREEN_WIDTH // 2,  40, 50, 15)

player_score = 0
computer_score = 0
