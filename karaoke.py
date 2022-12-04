import pygame
import time
import karaoke_functions as kf
from settings import Settings
from background import Background
import codecs
import threading


def main(program, name_song, extension):
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    background = Background(screen)
    pygame.display.set_caption("Karaoke")

    if program == "Create song":
        create_song(ai_settings, background, screen)
    else:
        karaoke(ai_settings, background, extension, name_song, screen)


def karaoke(ai_settings, background, extension, name_song, screen):
    while True:
        rows = 0
        len_song = 0
        score = 0

        arr_file_line_delay, count_rows = kf.get_time_code_lyrics(name_song)
        arr_file_text_song = kf.get_lyrics(name_song)
        play_music = threading.Thread(target=kf.play_song, args=(f"songs/{name_song}{extension}",))
        play_music.start()
        kf.update_screen(screen, None, 10, 100, background, None, None, None, False,
                         None, None, None)

        for line_delay in range(0, count_rows - 1):
            time.sleep(float(arr_file_line_delay[line_delay]))
            score = kf.check_line_delay(ai_settings, arr_file_text_song, line_delay, rows, score)
            len_song += float(arr_file_line_delay[line_delay])
            text_score, text_song, text_voice = kf.get_text_to_draw(ai_settings, arr_file_text_song, rows, score)
            kf.update_screen(pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)),
                             text_song, 60, 355, background, text_voice, 60, 380, True,
                             text_score, 60, 330)
            rows += 1
        print(len_song)
        print("End")
        break


def create_song(ai_settings, background, screen):
    while True:
        kf.update_screen(screen, None, 10, 100, background, None, None, None, False,
                         None, None, None)
        kf.check_events(ai_settings, "Create song")
