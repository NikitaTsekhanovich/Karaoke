import codecs
import time
import pygame
import sys
import pyglet


def check_events(ai_settings, program):
    if program == "Create song":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ai_settings.file.close()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    if ai_settings.count_space % 2 == 0:
                        ai_settings.count_space += 1
                        ai_settings.start = time.time()
                        print("start")
                    else:
                        ai_settings.count_space += 1
                        end = time.time()
                        ai_settings.file.write(f"{end - ai_settings.start}\n")
                        print("end")
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ai_settings.file.close()
                    sys.exit()


def play_song(song):
    mus = pyglet.resource.media(song)
    mus.play()
    pyglet.app.run()


def update_screen(screen, text, x, y):
    screen.blit(text, (x, y))
    pygame.display.flip()
