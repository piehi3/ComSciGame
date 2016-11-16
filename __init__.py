import pygame, sys
import reference
import player
import objectLoader
import light
import background
import uiOverlay

pygame.init()

window = pygame.display.set_mode((reference.WIDTH,reference.HEIGHT))
lighting = pygame.Surface((reference.WIDTH,reference.HEIGHT), pygame.SRCALPHA)    
background1 = background.Background()
uiOverlay1 = uiOverlay.UIOverlay()

pygame.display.set_caption("Testing Window")
clock = pygame.time.Clock()
clock.tick(reference.FPS)

#initialize basic objects
pObjects = objectLoader.setUpObjects()
#setup object bounding box
renderBox = []
#initialize basic objects
#initialize player
player1 = player.Player(pObjects[0])
#generating stars
background1.generateBackground(player1)
uiOverlay1.generateBackground(player1)

for i in range(len(pObjects)):
    renderBox.append(pObjects[i].getRenderBoundingBox(player1))


window.fill((255,255,255))
while True:
    
    for i in range(len(renderBox)):
        renderBox[i] = pObjects[i].getRenderBoundingBox(player1)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y=event.pos
            uiOverlay1.updateButtons(x,y)
            
        if event.type == pygame.KEYUP:
            uiOverlay1.toggleOverlay(event.key)
            player1.keyUpPress(event.key,pObjects)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    window.fill((0,0,0))
    lighting.fill((0,0,0,0))
    
    keyPress = pygame.key.get_pressed()
        
    
    player1.playerInput(keyPress)
    
    #updating basic objects
    for i in range(len(pObjects)):
        pObjects[i].updateLogic(player1)
        pObjects[i].checkCollided(player1,pObjects)
        pObjects[i].updateGraphics(window,player1)
        #updatinglights 
        if isinstance(pObjects[i],light.Light):
             pObjects[i].updateGraphicLighting(lighting,player1)
    #updating player
    player1.updatePlayer()
    #adding lighting to main window
    window.blit(background1.getWindow(), (0,0))
    if(uiOverlay1.isOverlayed):
        window.blit(uiOverlay1.getWindow(), (0,0))
    #background.getWindow().blit(window,(0,0))