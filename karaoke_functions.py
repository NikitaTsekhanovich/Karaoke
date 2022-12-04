import codecs
import time
import pygame
import sys
import pyglet
import speech_recognition
import threading


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


def play_song(song):
    mus = pyglet.resource.media(song)
    mus.play()
    pyglet.app.run()


def get_voice_reading(ai_settings):
    try:
        print("Зашел!")
        sr = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                ai_settings.sentence = query
    except speech_recognition.UnknownValueError:
        ai_settings.sentence = 'Не молчи!'


def check_line_delay(ai_settings, arr_file_text_song, line_delay, rows, score):
    if line_delay != 0:
        voice = threading.Thread(target=get_voice_reading, args=(ai_settings,))
        voice.start()
        score = get_score(ai_settings, arr_file_text_song, rows, score)
    return score


def get_score(ai_settings, arr_file_text_song, rows, score):
    voice_text = ai_settings.sentence.replace(" ", "")
    lyrics = arr_file_text_song[rows - 1].lower().replace(",", "").replace(" ", "")
    if len(voice_text) == len(lyrics) - 1:
        score += 1
    return score


def get_time_code_lyrics(name_song):
    file_line_delay = open(f"breakpoint_for_songs/{name_song}_time_code.txt", "r")
    arr_file_line_delay = file_line_delay.read().split("\n")
    count_rows = len(arr_file_line_delay)
    file_line_delay.close()
    return arr_file_line_delay, count_rows


def get_lyrics(name_song):
    file_text_song = codecs.open(f"lyrics/{name_song}_text.txt", "r", "utf_8_sig")
    arr_file_text_song = file_text_song.read().split("\n")
    file_text_song.close()
    return arr_file_text_song


def get_text_to_draw(ai_settings, arr_file_text_song, rows, score):
    text_score = pygame.font.Font(None, 20) \
        .render(str(score), True, (200, 200, 200))
    text_voice = pygame.font.Font(None, 20) \
        .render(ai_settings.sentence, True, (200, 200, 200))
    text_song = pygame.font.Font(None, 20) \
        .render(arr_file_text_song[rows], True, (255, 255, 255))
    return text_score, text_song, text_voice


def update_screen(screen, text_song, text_x, text_y, background,
                  text_voice, text_voice_x, text_voice_y, is_text_voice,
                  text_score, text_score_x, text_score_y):
    background.draw()

    if text_song is not None and is_text_voice:
        screen.blit(text_song, (text_x, text_y))
    if is_text_voice:
        screen.blit(text_voice, (text_voice_x, text_voice_y))
        screen.blit(text_score, (text_score_x, text_score_y))

    pygame.display.flip()
