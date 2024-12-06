import pygame
import time
# Inicializa o pygame
pygame.mixer.init()
# Carrega o arquivo mp3
pygame.mixer.music.load('ScarTissue.mp3')
# Reproduz arquivo mp3
pygame.mixer.music.play()
# Espera a música acabar para finalizar o script
while pygame.mixer.music.get_busy():
        time.sleep(1)
        