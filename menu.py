import pygame
import pygame_menu
import karaoke
import os
import re


def Menu():
    pygame.init()
    screen = pygame.display.set_mode((480, 416))
    pygame.display.set_caption("Karaoke")
    main_theme = pygame_menu.themes.THEME_DARK.copy()
    main_theme.set_background_color_opacity(0.0)
    menu = pygame_menu.Menu('', 480, 416, theme=main_theme)
    menu.add.button('Karaoke', choose_song)
    menu.add.button('Create song', start_create_song)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


def choose_song():
    screen = pygame.display.set_mode((480, 416))
    pygame.display.set_caption("Songs")
    main_theme = pygame_menu.themes.THEME_DARK.copy()
    main_theme.set_background_color_opacity(0.0)
    menu = pygame_menu.Menu('', 480, 416, theme=main_theme)
    songs = os.scandir(r"C:\Users\honor\source\repos\Karaoke\songs")
    for song in songs:
        menu.add.selector('Song:', [(song.name, song.name)], onchange=start_karaoke)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


def start_karaoke(value, song_with_extension):
    song = re.search(r'.+[.]', song_with_extension).group()[:-1]
    karaoke.main("Karaoke", song, ".mp3")


def start_create_song():
    karaoke.main("Create song", None, None)


if __name__ == "__main__":
    Menu()
