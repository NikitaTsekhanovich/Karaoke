import codecs
import time
import pygame
import sys
import pyglet
import speech_recognition


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


def get_voice_reading(ai_settings):
    try:
        print("Зашел!")
        sr = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                ai_settings.sentence = query
                return ai_settings.sentence
    except speech_recognition.UnknownValueError:
        ai_settings.sentence = 'Не молчи!'
        return


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
