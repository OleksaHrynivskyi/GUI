import requests
from bs4 import BeautifulSoup
from collections import Counter
import FreeSimpleGUI as sg

sg.theme("DarkTeal9")


text = sg.Text("Збір даних з веб-документів",
               font = ("Comic Sans", 16))

text1 = sg.Text("Введіть покликання:",
                font = ("Comic Sans", 14))

input = sg.Input(key = "input",
                 font = ("Comic Sans", 14),
                 expand_x=True)

button = sg.Button("Збір даних",
                   key = "button",
                   font = ("Comic Sans", 14))

output = sg.Output(size = (50, 10),
                   key = "output",
                   font = ("Comic Sans", 14))

exit = sg.Button("Вихід",
                 key = "exit",
                 font = ("Comic Sans", 14),
                 button_color = ("white", "red"))

layout = [
    [text],
    [text1],
    [input],
    [button],
    [output],
    [exit]
]

window = sg.Window("Збір даних з веб-документів", layout)
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "exit"):
        break

    elif event == "button":
        url = values["input"]
        if not url:
            window["output"].update("Будь ласка, введіть покликання!")
            continue

        try:
            res = requests.get(url)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, "html.parser")

            text = soup.get_text().lower()

            words = Counter(text.split())

            all_tags = soup.find_all(True)

            tag_name = []

            for tag in all_tags:
                tag_name.append(tag.name)

            tag_kilkist = Counter(tag_name)

            links = len(soup.find_all('a'))
            images = len(soup.find_all('img'))

            window["output"].update("") 
            print("Частота слів (найбільш популярні):")
            for word, count in words.most_common(10):
                print(f"  {word}: {count}")
            print("\nЧастота HTML-тегів:")
            for tag, count in tag_kilkist.items():
                print(f"  {tag}: {count}")
            print(f"\nКількість посилань: {links}")
            print(f"Кількість зображень: {images}")

        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні сторінки: {e}")


