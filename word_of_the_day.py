from winotify import Notification, audio
import json
import random
import time
from datetime import datetime

cheatsheet = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p',
    17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
    24: 'x', 25: 'y', 26: 'z', 27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e'
}

with open("C:\\Users\\Medha Trust\\OneDrive\\Desktop\\python\\project\\dict.json", "r") as fin:
    cont = json.load(fin)

now = datetime.now()
day = now.day
month = now.month
year = now.year

letter = cheatsheet.get(day, None)
if not letter:
    print("Invalid day for cheatsheet.")
    exit()


letter_list = [(word, meaning) for word, meaning in cont.items() if word.lower().startswith(letter)]


def send_notification():
    if not letter_list:
        print(f"No words found for letter '{letter}'.")
        return
    word, meaning = random.choice(letter_list)
    toast = Notification(
        app_id="WORD OF THE DAY",
        title=f"Date: {day}/{month}/{year} | Letter: '{letter.upper()}'",
        msg=f"{word.capitalize()}: {meaning}\n\n***** Enjoy Learning *****",
        icon=r"C:\Users\Medha Trust\OneDrive\Desktop\python\project\wod.png",  
        duration="long"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def main():
    while True:
        send_notification()
        time.sleep(24*3600)  # Run once every 24 hours

if __name__ == "__main__":
    main()
