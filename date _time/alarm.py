import time
import datetime
import pygame
import os


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    file_path = os.path.dirname(__file__)
    sound_file = os.path.join(file_path, "my_music.mp3")
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if (current_time == alarm_time):
            print("WAKE UP !! ")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            is_running = False
        time.sleep(4)


if __name__ == "__main__":
    alarm_time = input("Enter alarm time in HH:MM format: ")
    set_alarm(alarm_time)
    print(f"Alarm set for {alarm_time}. Waiting...")
