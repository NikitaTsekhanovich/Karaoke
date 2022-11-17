class Settings:
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 416
        self.back_ground_color = (0, 0, 0)

        self.count_space = 0
        self.file = open("time_code.txt", "w")
        self.start = 0
