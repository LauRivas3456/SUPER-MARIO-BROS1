import pygame
import os

pygame.init()
pygame.mixer.init()
ruta_musica = os.path.join("MarioBros", "Archivos", "Super Mario Bros. Theme Song - ultragamemusic.mp3")
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)
ruta_moneda_sonido = os.path.join("MarioBros", "Archivos", "super-mario-bros-coin.mp3")
sonido_moneda = pygame.mixer.Sound(ruta_moneda_sonido)