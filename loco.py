import pgzrun
def draw():
    aantal_even = 0
    aantal_oneven = 0
    screen.draw.text('even', topleft=(10,0), color='green')
    screen.draw.text('oneven', topleft=(100,0), color='red')
    for teller in range(1000,1,-1):
        if((teller % 2)==0):
            aantal_even += 1
            screen.draw.text(str(teller), topleft=(10,20*aantal_even), color='green')
        else:
            aantal_oneven += 1
            screen.draw.text(str(teller), topleft=(100,20*aantal_oneven), color='red')
import pgzrun
    