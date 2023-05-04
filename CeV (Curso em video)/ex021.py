import pygame
print(5*'=','Musica',5*'=')
pygame.init()
pygame.mixer.music.load('Over_the_Horizon.mp3')
pygame.mixer.music.play()
pygame.event.wait()