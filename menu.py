import pygame
import pygame_menu
import karaoke


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
    menu.add.button('song: 7Б', start_karaoke_7B)
    menu.add.button('song: Mnogoznaal', start_karaoke_Mnogoznaal)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


def start_karaoke_7B():
    karaoke.main(True, "Karaoke", "7Б", ".mp3")


def start_karaoke_Mnogoznaal():
    karaoke.main(True, "Karaoke", "Mnogoznaal", ".mp3")


def start_create_song():
    karaoke.main(True, "Create song", None, None)


if __name__ == "__main__":
    Menu()
