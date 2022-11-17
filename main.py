# import speech_recognition
#
# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5
#
# with speech_recognition.Microphone() as mic:
#     sr.adjust_for_ambient_noise(source=mic, duration=0.5)
#     audio = sr.listen(source=mic)
#     query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
#     print(query)
from datetime import datetime
import time
import pygame

pygame.init()
# screen = pygame.display.set_mode(200, 200)
while True:
    for event in pygame.event.get():
        print("A")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")

# start_time = datetime.now()
# time.sleep(5)
# print(datetime.now() - start_time)
