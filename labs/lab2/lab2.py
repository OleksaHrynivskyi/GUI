import random
from function import find_element
import FreeSimpleGUI as sg

sg.theme("DarkTeal9")

text = sg.Text("Введіть кількість елементів списку: ",
                font = ("Comic Sans", 16))
input = sg.Input(key = "input",
                    font = ("Comic Sans", 16))
button = sg.Button("Згенерувати список",
                    key = "button",
                    font = ("Comic Sans", 16))
text2 = sg.Text("Згенерований список:",
                font = ("Comic Sans", 16))
box = sg.Multiline(size = (30, 3),
                    key = "box",
                    font = ("Comic Sans", 16),
                    disabled = True)
text3 = sg.Text("Введіть число, яке треба знайти:",
                font = ("Comic Sans", 16))
input2 = sg.Input(key = "input2",
                    font = ("Comic Sans", 16))
button2 = sg.Button("Знайти елемент",
                    key = "button2",
                    font = ("Comic Sans", 16))
text4 = sg.Text(key = "result",
                font = ("Comic Sans", 16),
                size = (30, 1),
                text_color = "yellow")
exit = sg.Button("Вихід",
                    key = "exit",
                    font = ("Comic Sans", 16),
                    button_color = ("white", "red"))


layout = [[text],
            [input],
            [button],
            [text2],
            [box],
            [text3],
            [input2],
            [button2],
            [text4],
            [exit]
            ]

window = sg.Window("Пошук елемента у списку", layout)

spysok_random = [] 

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "exit"):
        break
    elif event == "button":
        try:
            n = int(values["input"])
            if n <= 0:
                sg.popup("Ви ввели не додатнє число або нуль!",
                            font=("Comic Sans", 14))
                continue 
            spysok_random = [random.randint(-10, 10) for _ in range(n)]
            window["box"].update(f"{spysok_random}")

        except ValueError:
            sg.popup("Ви ввели не ціле число або поле пусте!", 
                        font=("Comic Sans", 14))
    elif event == "button2":
        try:
            if not spysok_random:
                sg.popup("Спершу згенеруйте список",
                            font = ("Comic Sans", 14))
                continue
            else:
                shchyslo = int(values["input2"])
                res = find_element(spysok_random, shchyslo)

                if res != -200:
                    window["result"].update(f"Елемент {shchyslo} знайдено на індексі - {res}")
                else:
                    window["result"].update("Елемент не знайдено у списку.")
        except ValueError:
            sg.popup("Ви ввели не ціле число або поле пусте!", 
                     font=("Comic Sans", 14))
        except Exception as e:
            sg.popup(f"Сталася помилка: {e}", 
                     font=("Comic Sans", 14))

window.close()