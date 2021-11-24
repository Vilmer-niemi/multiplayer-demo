import pygame
from netClient import *
pygame.display.set_caption("Client")
#variables
token = 0
players = []
window = pygame.display.set_mode((200,500))

#classes
class Player():
    def __init__(self, cordinate:tuple, width:int, height:int, color:tuple):
        self.x = cordinate[0] 
        self.y = cordinate[1]
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
    def draw(self, window):
        print(window, self.color,(self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, self.color,(self.x, self.y, self.width, self.height))        

    def input(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_w]:
            self.y -= 5
        if pressedKeys[pygame.K_s]:
            self.y += 5
        if pressedKeys[pygame.K_a]:
            self.x -= 5
        if pressedKeys[pygame.K_d]:
            self.x += 5
            
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def drawWindow(window, players):
    window.fill((255,255,255))
    for player in players:
        player.drawWindow(window)
    pygame.display.update()

def main():
    run = True
    
    net = Network()
    x, y = dataHandling.ServerReceive(net.getPosition())
    player = Player((x,y),100,100,(0,255,0))

    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        data = net.send(player.x,player.y)
        for i in len(data):
            players.append(data[i])
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.input()
        drawWindow(window, players)
                
main()  