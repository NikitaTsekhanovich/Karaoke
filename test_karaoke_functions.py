import unittest
import pygame
import karaoke_functions as kf
from settings import Settings
import codecs


class TestKaraokeFunctions(unittest.TestCase):
    def test_get_score_correct_input(self):
        ai_settings = Settings()
        name_song = "test"
        file_text_song = codecs.open(f"test_song/{name_song}_text.txt", "r", "utf_8_sig")
        arr_file_text_song = file_text_song.read().split("\n")
        file_text_song.close()
        ai_settings.sentence = "test тест"
        score = 1
        row = 2
        score_new = kf.get_score(ai_settings, arr_file_text_song, row, score)
        self.assertEqual(score_new, score + 1)

    def test_get_score_incorrect_input(self):
        ai_settings = Settings()
        name_song = "test"
        file_text_song = codecs.open(f"test_song/{name_song}_text.txt", "r", "utf_8_sig")
        arr_file_text_song = file_text_song.read().split("\n")
        file_text_song.close()
        ai_settings.sentence = "aaa"
        score = 1
        row = 2
        score_new = kf.get_score(ai_settings, arr_file_text_song, row, score)
        self.assertEqual(score_new, score)

    def test_get_time_code_lyrics(self):
        name_song = "ДайМне"
        self.assertEqual(kf.get_time_code_lyrics(name_song), (['0.00000000000001',
                                                               '0.00000000000001',
                                                               '4.792797803878784',
                                                               '4.985811233520508',
                                                               '10.001412153244019',
                                                               '4.37142539024353',
                                                               '4.497427701950073',
                                                               '10.572131633758545',
                                                               ''],
                                                              9))

    def test_check_line_delay(self):
        ai_settings = Settings()
        rows = 2
        score = 0
        line_delay = 0
        arr_file_text_song = "file"
        new_score = kf.check_line_delay(ai_settings, arr_file_text_song, line_delay, rows, score)
        self.assertEqual(new_score, score)
        line_delay = 1
        new_score = kf.check_line_delay(ai_settings, arr_file_text_song, line_delay, rows, score)
        self.assertEqual(new_score, score + 1)


if __name__ == '__main__':
    unittest.main()
