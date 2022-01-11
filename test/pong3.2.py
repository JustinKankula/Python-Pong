import pygame

import random



SCR_WID, SCR_HEI = 640, 480
class Player():

        def __init__(self):
                self.x, self.y = 16, SCR_HEI/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (32, 16))
                if self.score == 10:
                        print ("player 1 wins!")
                        exit()
                
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

 
class Enemy():
        
        
        def __init__(self):
                self.x, self.y = SCR_WID-16, SCR_HEI/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                screen.blit(scoreBlit, (SCR_HEI+92, 16))
                if self.score == 10:
                        print ("Player 2 wins!")
                        exit()
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                        self.y -= self.speed
                elif keys[pygame.K_DOWN]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Ball():
        def __init__(self):
                self.x = random.randint(250, 450)
                self.y = random.randint(250, 450)
                self.speed_x = random.choice([-3, 3])
                self.speed_y = random.choice([-3, 3])
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
                if self.y <= 0:
                        self.speed_y *= -1
                if self.y >= SCR_HEI:
                        self.speed_y *= -1
 
                
                        
                
                       
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score += 1
                        if player.score < 9:
                                score_sound = pygame.mixer.Sound('sounds\score.wav')
                                score_sound.play()
                        elif player.score == 9:
                                score_sound = pygame.mixer.Sound('sounds\matchpoint.wav')
                                score_sound.play()
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x = 3
                        player.score += 1
                        if player.score < 9:
                                score_sound = pygame.mixer.Sound('sounds\score.wav')
                                score_sound.play()
                        elif player.score == 9:
                                score_sound = pygame.mixer.Sound('sounds\matchpoint.wav')
                                score_sound.play()
                                
                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1.1
                                        score_sound = pygame.mixer.Sound('sounds\hit.wav')
                                        score_sound.play()
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                        self.speed_x *= -1.1
                                        score_sound = pygame.mixer.Sound('sounds\hit.wav')
                                        score_sound.play()
                                        break
                        n += 1
               
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))

SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.font.init()
player = Player() 
enemy = Enemy()
##Continue = int(input('Enter 1 for New Game or 2 to Continue Last Game:'))
##if Continue == 2:
##        from SaveFile import *
##        player.score = s_player
##        enemy.score = s_enemy
ball = Ball()
ball2 = Ball()
ball3 = Ball()
clock = pygame.time.Clock()
FPS = 60
pygame.mixer.init()

def main():
        BG_Image = pygame.image.load("images\BG.jpg")
        pygame.display.set_caption("Pong")
        
        while True:
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        exit()
                ##process
                #logic
                if player.score > 4:
                        ball2.movement()
                if enemy.score > 4:
                        ball3.movement()
                ball.movement()
                player.movement()
                enemy.movement()
                
                ##logic
                #draw
                screen.fill((0, 0, 0))
                screen.blit(BG_Image, (0, 0))
                
                ball.draw()
                player.draw()
                player.scoring()
                if player.score == 5:
                        BG_Image = pygame.image.load("images\BG2.jpg")
                enemy.draw()
                enemy.scoring()
                if enemy.score == 5:
                        BG_Image = pygame.image.load("images\BG2.jpg")
##                SF = open("SaveFile.py", "w")
##                SF.write("s_player = " + str(player.score) + "\n")
##                SF.write("s_enemy = " + str(enemy.score) + "\n")
##                SF.close()
                ##draw
                #_______
                pygame.display.flip()
                clock.tick(FPS)
main()
