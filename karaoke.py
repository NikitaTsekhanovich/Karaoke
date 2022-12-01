import pygame
import time
import karaoke_functions as kf
from settings import Settings
from background import Background
import codecs
import threading


def main(run, program, name_song, extension):
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    background = Background(screen)
    pygame.display.set_caption("Karaoke")

    if program == "Create song":
        while run:
            kf.update_screen(screen, None, 10, 100, background, None, None, None, False,
                             None, None, None)
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
            score = 0
            play_music = threading.Thread(target=kf.play_song, args=(f"songs/{name_song}{extension}",))
            play_music.start()
            kf.update_screen(screen, None, 10, 100, background, None, None, None, False,
                             None, None, None)
            for line_delay in range(0, count_rows - 1):
                time.sleep(float(arr_file_line_delay[line_delay]))
                if line_delay != 0:
                    voice = threading.Thread(target=kf.get_voice_reading, args=(ai_settings,))
                    voice.start()
                    a = ai_settings.sentence.replace(" ", "")
                    b = arr_file_text_song[rows - 1].lower().replace(",", "").replace(" ", "")
                    if len(a) == len(b)-1:
                        score += 1
                len_song += float(arr_file_line_delay[line_delay])
                text_score = pygame.font.Font(None, 20) \
                    .render(str(score), True, (200, 200, 200))
                text_voice = pygame.font.Font(None, 20) \
                    .render(ai_settings.sentence, True, (200, 200, 200))
                text_song = pygame.font.Font(None, 20) \
                    .render(arr_file_text_song[rows], True, (255, 255, 255))
                kf.update_screen(pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)),
                                 text_song, 60, 355, background, text_voice, 60, 380, True,
                                 text_score, 60, 330)
                rows += 1
            print(len_song)
            print("End")
            break
