import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Devakshi.mp3')
pygame.mixer.music.play()
sleep(5)
image = pygame.image.load('krpkab.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab1.jpg')
window.blit(image, (50,50))
pygame.display.update()
sleep(3)
image = pygame.image.load('krpkab2.jpg')
window.blit(image, (100,100))
pygame.display.update()
sleep(3)


image = pygame.image.load('krpkab3.jpg')
window.blit(image, (150,150))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab4.jpg')
window.blit(image, (150,150))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab5.jpg')
window.blit(image, (200,200))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab6.jpg')
window.blit(image, (250,250))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab7.jpg')
window.blit(image, (300,300))
pygame.display.update()
sleep(3)

image = pygame.image.load('krpkab8.jpg')
window.blit(image, (350,350))
pygame.display.update()
sleep(3)