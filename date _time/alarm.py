import time
import datetime
# import pygane

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    sound_file = "my_music.mp3"  # Replace with your sound file path

if __name__ == "__main__":
    alarm_time = input("Enter alarm time in HH:MM format: ")
    set_alarm(alarm_time)
    print(f"Alarm set for {alarm_time}. Waiting...")
