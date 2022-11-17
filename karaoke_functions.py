import codecs
import time
import pygame
import sys
import pyglet


# def text_output(screen):
#     file_line_delay = open("breakpoint_for_songs/7Б_time_code.txt", "r")
#     arr_file_line_delay = file_line_delay.read().split("\n")
#     count_rows = len(arr_file_line_delay)
#     file_line_delay.close()
#     file_text_song = codecs.open("lyrics/7Б_text.txt", "r", "utf_8_sig")
#     arr_file_text_song = file_text_song.read().split("\n")
#     rows = 0
#     len_song = 0
#     for line_delay in range(0, count_rows - 1):
#         time.sleep(float(arr_file_line_delay[line_delay]))
#         len_song += float(arr_file_line_delay[line_delay])
#         print(arr_file_text_song[rows])
#         text_song = pygame.font.Font(None, 20) \
#             .render(arr_file_text_song[rows], True, (255, 255, 255))
#         update_screen(screen, text_song)
#         rows += 1
#     print(len_song)
#     print("End")


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
