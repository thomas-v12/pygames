from random import randint
import random
import time
import pgzrun

WIDTH = 1000
HEIGHT = 800
BUITEN_BEELD = (WIDTH + 100, HEIGHT + 100)

appel = Actor('apple', pos = BUITEN_BEELD)
sinasappel = Actor('orange', pos = BUITEN_BEELD)
ananas = Actor('pineapple', pos = BUITEN_BEELD)

fruits = [appel, sinasappel, ananas]

score = 0
levens = 3
level = 1
fruit_spawned = 0
game_over = False


def draw():
    global game_over
    screen.clear()
    for fruit in fruits:
        print('teken fruit: ' + fruit.image)
        fruit.draw()
    if game_over:
        toon_game_over()
    else:
        toon_score()

def toon_score():
    screen.draw.text('LEVENS: ' + str(levens) + ' SCORE: ' + str(score) + ' LEVEL: ' + str(level), (50, 10), color='green', fontsize=60)

def toon_game_over():
    screen.clear()
    screen.draw.text('GAME OVER', (100, 100), color='red', fontsize=60)
    screen.draw.text('SCORE: ' + str(score), (100, 150), color='red', fontsize=60)
    screen.draw.text('LEVEL: ' + str(level), (100, 200), color='red', fontsize=60)

def random_fruit():
    return random.choice(fruits)

def plaats_fruit():
    global level, fruit_spawned
    if not game_over:
        fruit = random_fruit()
        print('toegevoegd: '+ fruit.image)
        fruit.x = randint(10, WIDTH)
        fruit.y = randint (10,HEIGHT)
        clock.schedule(respawn_fruit, 5 / level)
        fruit_spawned += 1

def respawn_fruit():
    if is_fruit_in_beeld():
        mis_geschoten()
    plaats_fruit()

def mis_geschoten():
    global game_over, score, levens
    print('je hebt gemist')
    verminder_punten(5)
    verminder_levens()
    
def verminder_levens():
    global levens, game_over
    levens -= 1
    if levens <= 0:
        print('je bent game over')
        game_over = True
    print('je hebt ' + str(levens)+ ' levens')

def voeg_leven_toe():
    global levens
    levens += 1

def voeg_punten_toe(punten):
    global score, levens, level
    score += punten
    if score <= 0:
        score = 0
    if score > 0 and score % 100 == 0:
        voeg_leven_toe()
    if fruit_spawned > 0 and fruit_spawned % 10 == 0:
        level += 1
    print('toegevoegd: ' + str(punten))
    print('je score is: ' + str(score))

def verminder_punten(punten):
    voeg_punten_toe(-1*punten)

def hoeveel_punten(fruit):
    if fruit == appel:
        return 10
    elif fruit == ananas:
        return 1
    elif fruit  == sinasappel:
        return 5
    else:
        return 0

def raak_geschoten(fruit):
    print('Goed schot')
    voeg_punten_toe(hoeveel_punten(fruit))
    verwijder_fruit(fruit)

def verwijder_fruit(fruit):
    # zet fruit buiten beeld
    fruit.pos = BUITEN_BEELD

def is_fruit_in_beeld():
    global fruit_in_beeld
    for fruit in fruits:
        if fruit.x <= WIDTH:
            return True
    return False

def on_mouse_down(pos):
    global score
    fruit_geraakt = False
    for fruit in fruits:
        if fruit.collidepoint(pos):
            fruit_geraakt = True
            raak_geschoten(fruit)
    
    if not fruit_geraakt:
        mis_geschoten()

plaats_fruit()
pgzrun.go()