import pygame
import time
import karaoke_functions as kf
from settings import Settings
import codecs
import threading


def main(run, program, name_song, extension):
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Karaoke")
    text = pygame.font.Font(None, 36)\
        .render('Караоке у Никиты', False, (255, 255, 255))

    if program == "Create song":
        while run:
            kf.update_screen(screen, text, 10, 100)
            kf.check_events(ai_settings, "Create song")
    else:
        while run:
            file_line_delay = open(f"breakpoint_for_songs/{name_song}_time_code.txt", "r")
            arr_file_line_delay = file_line_delay.read().split("\n")
            count_rows = len(arr_file_line_delay)
            file_line_delay.close()
            file_text_song = codecs.open(f"lyrics/{name_song}_text.txt", "r", "utf_8_sig")
            arr_file_text_song = file_text_song.read().split("\n")
            rows = 0
            len_song = 0
            play_music = threading.Thread(target=kf.play_song, args=(f"songs/{name_song}{extension}",))
            play_music.start()
            kf.update_screen(screen, text, 10, 100)
            for line_delay in range(0, count_rows - 1):
                time.sleep(float(arr_file_line_delay[line_delay]))
                len_song += float(arr_file_line_delay[line_delay])
                print(arr_file_text_song[rows])
                text_song = pygame.font.Font(None, 24) \
                    .render(arr_file_text_song[rows], True, (255, 255, 255))
                kf.update_screen(pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)),
                                 text_song, 10, 200)
                rows += 1
            print(len_song)
            print("End")
            break
