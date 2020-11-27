import os, sys
from math import sin, cos
import random
import pygame


dirparth = os.getcwd()
sys.path.append(dirparth)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
velocity = 0
aceleration = 1
max_speed = 25
music = 1
rend_red = 60
n_red = 5
velocity_red = 1
speedrate = 1
sizerate = 60
ballsrate = 1
print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[1] PLAY
[2] Blueball settings
[3] Redball settings
[4] Change to default settings
[5] Music
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")

while True:
    try:
        r = int(input('Select an option:'))
        if r == 2:
            while True:
                try:
                    velocity = int(input('Blueball velocity:'))
                    aceleration = int(input('Blueball aceleration:'))
                    max_speed = int(input(' Blueball max speed:'))
                except(ValueError, TypeError):
                    print('Invalid settings...')
                else:
                    break
        if r == 3:
            while True:
                try:
                    rend_red = int(input('Redballs size:'))
                    n_red = int(input('Number of Redballs:'))
                    velocity_red = int(input('Redballs velocity: '))
                    speedrate = int(input('Speed Rate:'))
                    sizerate = int(input('Size Rate:'))
                    ballsrate = int(input('Balls Rate:'))
                except(ValueError, TypeError):
                    print('Invalid settings...')
                else:
                    break
        if r == 4:
            velocity = 0
            aceleration = 2
            max_speed = 25

            rend_red = 60
            n_red = 10
            velocity_red = 4
            speedrate = 3
            sizerate = 30
            ballsrate = 1
            print('established default settings...')
        if r == 5:
            pass
            print("""Select an music:
            [1] Master of Puppets
            [2] Duality
            [3] Psychosocial
            [4] Painkiller
            [5] The Trooper
            [6] Run to the Hills
            [7] Hardwired
            [8] Symphony of destruction
            [9] Ride the Lightning
            [10] One
            [11] Hallowed be Thy Name""")
            while True:
                try:
                    music = int(input('Choose a song:'))
                except(ValueError, TypeError):
                    print('Invalid Option...')
                else:
                    break
        if r == 1:
            print('Loading...')
            break
    except(ValueError, TypeError):
        print('Invalid option...')
pygame.init()


masterOfPuppets = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\masterofpuppets.mp3")
duality = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\duality.mp3")
psychosocial = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\pyschosocial.mp3")
pain = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\painkiller.mp3")
trooper = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\trooper.mp3")
run = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\Run.mp3")
hard = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\hardwired.mp3")
sym = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\symphony.mp3")
ride = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\ride.mp3")
one = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\one.mp3")
hallowed = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\hallowed.mp3")
playlist = [masterOfPuppets, duality, psychosocial, pain, trooper, run,
            hard, sym, ride, one,
            hallowed]
playlist[music-1].play(-1)
display = pygame.display.set_mode((1920, 1018), pygame.RESIZABLE)
pygame.display.set_caption('Red_Ball Game')
#Draw
y = random.randint(25, 965)
x = random.randint(25, 965)
DrawGroup = pygame.sprite.Group()

#Greenrect
Greenrect = pygame.sprite.Sprite(DrawGroup)
Greenrect.image = pygame.image.load(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\greendrect.png")
Greenrect.rect = pygame.Rect(0, 0, 200, 100)
Greenrect.rect.center = (1920, x)
Greenrect.image = pygame.transform.scale(Greenrect.image, [100, 100])

#Whiterect:
Whiterect = pygame.sprite.Sprite(DrawGroup)
Whiterect.image = pygame.image.load(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\whiterect.png")
Whiterect.rect = pygame.Rect(0, 0, 200, 100)
Whiterect.rect.center = (100, y)
Whiterect.image = pygame.transform.scale(Whiterect.image, [50, 100])

#BlueBall
blueball = pygame.sprite.Sprite(DrawGroup)
blueball.image = pygame.image.load(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\blueball2.png")
blueball.rect = pygame.Rect(0, 0, 50, 50)
blueball.image = pygame.transform.scale(blueball.image, [40, 40])
blueball.rect.center = (1890, x+10)
#REDBALL


class Redball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\redball.png")
        self.rect = pygame.Rect(500, 500, 50, 50)
        self.image = pygame.transform.scale(self.image, [rend_red, rend_red])


red_list = []


def add_ball(n):
    for c in range(0, n):
        red_list.append(f'rb{c}')


add_ball(n_red)
red_list2 = []
red_list3 = []
v_list = []
v_list2 = []


def create_red():
    for e in red_list:
        if e not in red_list2:
            red_list2.append(e)
            y = random.randint(50, 968)
            e = Redball(DrawGroup)
            red_list3.append(e)
            e.rect.center = [50, y]
            v = random.randint(-velocity_red, velocity_red)
            v2 = random.randint(-velocity_red, velocity_red)
            v_list.append(v)
            v_list2.append(v2)
        else:
            pass


#pygame.mouse.set_visible(0)
crash = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\crash.flac")
levelup = pygame.mixer.Sound(r"C:\Users\PICHAU\PycharmProjects\Blueball_game\data\levelup.mp3")
#clock = pygame.time.Clock()
angle_vector = 22.5
open_display = True
while open_display:
    #clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_display = False
        elif event.type == pygame.KEYUP:
            pass
        if keys[pygame.K_w]:
            blueball.rect.y -= velocity
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        elif keys[pygame.K_s]:
            blueball.rect.y += velocity
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        elif keys[pygame.K_d]:
            blueball.rect.x += velocity
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        elif keys[pygame.K_a]:
            blueball.rect.x -= velocity
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        if keys[pygame.K_a] and keys[pygame.K_w]:
            blueball.rect.x += velocity * cos(angle_vector)
            blueball.rect.y -= velocity * sin(angle_vector)
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            blueball.rect.x -= velocity * cos(angle_vector)
            blueball.rect.y -= velocity * sin(angle_vector)
            velocity += aceleration
            if velocity >= max_speed:
                    velocity = max_speed
        if keys[pygame.K_s] and keys[pygame.K_a]:
            blueball.rect.x += velocity * cos(angle_vector)
            blueball.rect.y += velocity * sin(angle_vector)
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            blueball.rect.x -= velocity * cos(angle_vector)
            blueball.rect.y += velocity * sin(angle_vector)
            velocity += aceleration
            if velocity >= max_speed:
                velocity = max_speed

    display.fill([0, 0, 0])
    #mx, my = pygame.mouse.get_pos
    create_red()
    for e in red_list3:
        e.rect.x += v_list[red_list3.index(e)]
        e.rect.y += v_list2[red_list3.index(e)]
        if pygame.sprite.collide_mask(blueball, e):
            crash.play()
            blueball.rect.center = Greenrect.rect.center
            #mx, my = Greenrect.rect.center
        #Colisão com a parede:
        if e.rect.x >= 1870 or e.rect.x <= 0:
            v_list[red_list3.index(e)] *= -1
        if e.rect.y + e.rect.w >= 1018 or e.rect.y <= -2*e.rect.w:
            v_list2[red_list3.index(e)] *= -1
        #Colisão Greenrect:
        if pygame.sprite.collide_mask(e, Greenrect):
            v_list[red_list3.index(e)] *= -1
            v_list2[red_list3.index(e)] *= -1
        if pygame.sprite.collide_mask(e, Whiterect):
            v_list[red_list3.index(e)] *= -1
            v_list2[red_list3.index(e)] *= -1
        if pygame.sprite.collide_mask(blueball, Whiterect):
            levelup.play()
            red_list.clear()
            red_list2.clear()
            velocity_red += speedrate
            n = ballsrate
            rend_red += sizerate
            e.image = pygame.transform.scale(e.image, [rend_red, rend_red])
            add_ball(n)
            x2 = 0
            x1 = random.choice([100, 1900])
            y = random.randint(25, 965)
            y2 = random.randint(25, 965)
            if x1 == 100:
                x2 = 1900
            else:
                x2 = 100
            Whiterect.rect.center = x1, y
            Greenrect.rect.center = x2, y2
            blueball.rect.center = Greenrect.rect.center
            #pygame.mouse.get_pos = Greenrect.rect.center
    DrawGroup.draw(display)
    pygame.display.flip()
pygame.quit()