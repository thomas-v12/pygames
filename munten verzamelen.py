from random import randint
import time
import pgzrun

WIDTH = 1900
HEIGHT = 900
STAP = 10
TIJD = 120.
PUNT_PER_MUNT = 1


score = 0
game_over = False
vos = Actor('fox')
vos.pos = 100, 100
munt = Actor('coin')
munt.pos = 200, 200

def draw():
    screen.fill('green')
    vos.draw()
    munt.draw()
    screen.draw.text('scor: ' + str(score), color='red', topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text('eind score: ' + str(score), topleft = (10, 10), fontsize = 60)


def plaats_munt():
    munt.x = randint(20, WIDTH - 20)
    munt.y = randint(20, HEIGHT - 20)

def tijd_om():    
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        vos.x = vos.x - STAP
    elif keyboard.right:
        vos.x = vos.x + STAP
    elif keyboard.up:
        vos.y = vos.y - STAP
    elif keyboard.down:
        vos.y = vos.y + STAP

    if vos.x < 0:
        vos.x = WIDTH + vos.x
    elif vos.x > WIDTH:
        vos.x = vos.x - WIDTH
    elif vos.y < 0:
        vos.y = HEIGHT + vos.y
    elif vos.y > HEIGHT:
        vos.y = vos.y - HEIGHT
        
                 
    munt_verzameld = vos.colliderect(munt)

    if munt_verzameld:
        score = score + PUNT_PER_MUNT
        plaats_munt()

clock.schedule(tijd_om, TIJD)
plaats_munt()
pgzrun.go()