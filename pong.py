import pygame as pg
from pygame.locals import (K_UP, K_DOWN)
import random as rd
import math as m

VINDU_BREDDE = 720
VINDU_HOYDE  = 480
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

clock = pg.time.Clock()

l1 = []
for i in range(-3500,-4000):
    l1.append(i)

for i in range(3500,4000):
    l1.append(i)    

tilfeldig_tall = rd.randint(0,500)
tilfeldig_tall2= rd.randint(0,500)

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

class Hinder(Ball):
    def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart = xFart
        self.yFart = yFart
    
    #resetter ballen tilbake til midten
    def reset_ball(self):
        self.x = VINDU_BREDDE // 2
        self.y = VINDU_HOYDE // 2
        self.xFart = l1[rd.randint(0,500)]/1000
        self.yFart = l1[rd.randint(0,500)]/1000

    def flytt(self,rectangle1,rectangle2):
        """Metode for å flytte hinderet"""
       
        # Sjekker om hinderet er utenfor øvre/nedre kant
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart
        #sjekker om hinderet kolliderer med rektanglene
        if ((self.x - self.radius <= 21) and (rectangle1.ypos1 <= self.y <= rectangle1.ypos1 + 120)) or \
            ((self.x + self.radius >= 699) and (rectangle2.ypos2 <= self.y <= rectangle2.ypos2 + 120)):
             self.xFart = -self.xFart
    
        #spretter ballen av høyre og venstre kant, oppdaterer score etter hvert sprett
        #og setter ballen tilbake på midten når spillet er ferdig
        if ((self.x + self.radius)>=VINDU_BREDDE):
             self.xFart = -self.xFart
             rectangle1.increase_score()
             self.reset_ball()
        if ((self.x - self.radius) <= 0):
            self.xFart = -self.xFart
            rectangle2.increase_score()
            self.reset_ball()

    

        # Flytter hinderet
        self.x += self.xFart
        self.y += self.yFart
        return True


class Rectangle:
    def __init__(self,høyde,bredde,farge,vindu,fart):
        self.høyde = høyde
        self.bredde = bredde
        self.farge = farge
        self.vindu = vindu
        self.fart = fart
        self.ypos1 = 180
        self.ypos2 = 180
        self.score = 0
    
    #oppdaterer score til spillerene
    def increase_score(self):
        self.score += 1       
        print(self, self.score)

    def tegn(self):
         """Metode for å tegne rektangelet"""
         pg.draw.rect(vindu,(255,255,255),(1,self.ypos1,20,120))
         pg.draw.rect(vindu,(255,255,255),(699,self.ypos2,20,120))

    #gir metode for å flytte rektanglene
    def flytt(self, taster):
        """Metode for å flytte spilleren"""
        if taster[pg.K_w]:
         self.ypos1 -= self.fart
        if taster[pg.K_s]:
            self.ypos1 += self.fart
        if taster[K_UP]:
         self.ypos2 -= self.fart
        if taster[K_DOWN]:
            self.ypos2 += self.fart

#gir dimensjoner til objektene
rektangel1 = Rectangle(25,10,(255,255,255),vindu,5)
rektangel2 = Rectangle(25,10,(255,255,255),vindu,5)
hinder = Hinder(360, 240, 10, (255, 255, 255), vindu, l1[tilfeldig_tall]/1000, l1[tilfeldig_tall2]/1000)

fortsett = True
kjører = True

while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    #grenser framerate
    clock.tick(60)
    #oppdaterer spillet
    trykkede_taster = pg.key.get_pressed()
    vindu.fill((110, 110, 110))
    rektangel1.tegn()
    rektangel2.tegn()
    hinder.tegn()
    hinder.flytt(rektangel1,rektangel2)
    rektangel1.flytt(trykkede_taster)
    rektangel2.flytt(trykkede_taster)

    bilde1 = pg.image.load(str(rektangel1.score) + ".png")
    bilde2 = pg.image.load(str(rektangel2.score) + ".png")
   
    score_display1 = vindu.blit(bilde1,(140,70))
    score_display2 = vindu.blit(bilde2,(520,70))

    if rektangel2.score == 10:
        print("Spiller 1 vant")
        pg.quit()
    if rektangel1.score == 10:
        print("spiller 2 vant")
        pg.quit()

    pg.display.flip()

pg.quit()