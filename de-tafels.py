from random import randint
import time
import pgzrun
from dataclasses import dataclass

@dataclass
class Stip:
    actor: Actor
    waarde: int

WIDTH = 1900
HEIGHT = 1000
AANTAL_STIPPEN = 10

stippen = []
foute_stippen = []
lijnen = []

volgende_stip = 0
tafel = 2

for s in range(0, AANTAL_STIPPEN):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint (20, HEIGHT - 20 )
    stip = Stip(actor, 0)
    stippen.append(stip)

for s in range(0, AANTAL_STIPPEN // 2):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint (20, HEIGHT - 20 )
    foute_stip = Stip(actor, 0)
    foute_stippen.append(foute_stip)

def plaats_stippen():
    waarde = tafel
    for stip in stippen:
        stip.actor.pos = randint(20, WIDTH - 20), randint (20, HEIGHT - 20 )
        stip.waarde = waarde
        waarde = waarde + tafel
    
    if tafel == 1:
        for foute_stip in foute_stippen:
            foute_stip.actor.pos = (-1000, -1000)
    else:
        for foute_stip in foute_stippen:
            foute_stip.actor.pos = randint(20, WIDTH - 20), randint (20, HEIGHT - 20 )
            positie = randint(1, AANTAL_STIPPEN-1)
            fout_getal = randint(positie*tafel + 1, (positie+1) * tafel - 1)
            foute_stip.waarde = fout_getal

def toon_tafel():
    screen.draw.text('Tafel van: ' + str(tafel), color='red', topleft=(10,10))
    screen.draw.text('Volgende som: ' + str(volgende_stip+1) + ' * ' + str(tafel), color='red', topleft=(10,50))


def draw_stip(stip):
    screen.draw.text(str(stip.waarde), (stip.actor.pos[0], stip.actor.pos[1]+12), color = 'red')
    stip.actor.draw()

def draw():
    screen.fill('yellow')
    
    for stip in stippen:
        draw_stip(stip)
        
    for foute_stip in foute_stippen:
        draw_stip(foute_stip)

    for lijn in lijnen:
        screen.draw.line(lijn[0], lijn[1], (0,0,0))

    toon_tafel()


def on_mouse_down(pos):
    global volgende_stip
    global lijnen
    global tafel

    if stippen[volgende_stip].actor.collidepoint(pos):
        if volgende_stip:
            lijnen.append((stippen[volgende_stip - 1].actor.pos, stippen[volgende_stip].actor.pos))
        volgende_stip = volgende_stip + 1
        if volgende_stip >= len(stippen):
            tafel = tafel + 1
            lijnen = []
            volgende_stip = 0
            plaats_stippen()
    else:
        lijnen = []
        volgende_stip = 0

plaats_stippen()
pgzrun.go()