import FreeSimpleGUI as sg
import random
from collections import Counter

sg.theme("DarkTeal9")


def zavd_1():
    spys1 = ["Красивий", "Щасливий", "Злий", "Швидкий", "Терплячий"]
    spys2 = ["какаду", "собака", "тигр", "страус", "кит"]
    spys3 = ["стрибає", "плаває", "бігає", "говорить", "їсть"]

    text = sg.Text("Генератор випадкових фраз:",
                    font=("Comic Sans", 16))
    
    button = sg.Button("Згенерувати", 
                       key="button",
                       expand_x=True,
                       font=("Comic Sans", 16))
    
    output = sg.Text("",
                     size=(50, 1), 
                     font=("Comic Sans", 14), 
                     key='output',
                     justification="center")
    
    exit = sg.Button("Назад",
                     key = "exit",
                     font = ("Comic Sans", 14),
                     button_color = ("white", "red"),
                     expand_x=True)
    
    layout = [
        [text],
        [button],
        [output],
        [exit]
    ]

    window = sg.Window("Завдання 1", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "exit"):
            break

        elif event == "button":
            phrase = f"{random.choice(spys1)} {random.choice(spys2)} {random.choice(spys3)}"
            window['output'].update(phrase)

    window.close()            


def zavd_2():
    text = sg.Text("Оберіть файл:", 
                   font=("Comic Sans", 18))

    input2 = sg.Input(key = "input",
                     enable_events = True,
                     font=("Comic Sans", 14))
    
    browse = sg.FileBrowse(font=("Comic Sans", 14),
                           button_text = "Огляд",
                           file_types = (("Text Files", "*.txt"),))

    button = sg.Button("Аналізувати",
                       key = "analyze",
                       font=("Comic Sans", 14),
                       expand_x=True)

    output = sg.Output(size = (50, 10),
                       font=("Comic Sans", 14),
                       key = "output")
    
    exit = sg.Button("Назад",
                     key = "exit",
                     button_color= ("white", "red"),
                     font = ("Comic Sans", 14),
                     expand_x=True)
    
    layout = [
        [text], 
        [input2, browse],
        [button],
        [output],
        [exit]
    ]

    window = sg.Window('Завдання 2', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "exit"):
            break

        elif event == "analyze":
            filepath = values["input"]
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()
                withspaces = len(text)
                withoutspaces = len(text.replace(" ", ""))
                words = text.split()
                allwords = len(words)
                uniquewords = len(set(words))
                wordsCount = Counter(words)
                totalwords = []
                for word, count in wordsCount.items():
                    if count == 1:
                        totalwords.append(word)
                totalwords1 = len(totalwords)

                window['output'].update(
                    f"Кількість слів, які зустрічаються один раз: {totalwords1}\n"
                    f"Кількість унікальних слів у тексті: {uniquewords}\n"
                    f"Кількість слів у тексті: {allwords}\n"
                    f"Кількість символів з пробілами: {withspaces}\n"
                    f"Кількість символів без пробілів: {withoutspaces}"
                )
            except FileNotFoundError:
                window['output'].update("Файл не знайдено.")
            except Exception as e:
                window['output'].update(f"Помилка: {e}")

    window.close()            


def zavd_3():

    text = sg.Text("Оберіть файл:", 
                   font=("Comic Sans", 14))

    input = sg.Input(key = "input",
                     enable_events = True,
                     font=("Comic Sans", 14))
    
    browse = sg.FileBrowse(font=("Comic Sans", 14),
                           button_text = "Огляд",
                           file_types = (("Text Files", "*.txt"),))
    
    text_N = sg.Text("Введіть N:", 
                     font=("Comic Sans", 14))
    
    Input_N = sg.Input(key = "N",
                       size = (5, 1),
                       font=("Comic Sans", 14))

    button = sg.Button("Аналізувати",
                       key = "analyze",
                       expand_x=True,
                       font=("Comic Sans", 14))

    output = sg.Output(size = (50, 10),
                       font=("Comic Sans", 14),
                       expand_x=True,
                       key = "output")
    
    exit = sg.Button("Назад",
                     key = "exit",
                     button_color= ("white", "red"),
                     font = ("Comic Sans", 14),
                     expand_x=True)
    

    layout = [
        [text], 
        [input, browse],
        [text_N, Input_N],
        [button],
        [output],
        [exit]
    ]

    window = sg.Window('Завдання 3', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "exit"):
            break

        elif event == "analyze":
            filepath = values["input"]
            try:
                N = int(values["N"])
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()                
                words = text.split()
                spys = []

                words_all = len(words) - N + 1

                for i in range(words_all):
                    aboba = ""
                    for j in range(N):
                        aboba = aboba + words[i + j] + " "
                    aboba = aboba.strip()
                    spys.append(aboba)

                rah = Counter(spys)
                window["output"].update(
                    f"Топ-10 найчастіше зустрічаємих послідовностей з {N} слів:\n{rah.most_common(10)}"
                )
            except FileNotFoundError:
                window['output'].update("Файл не знайдено.")
            except ValueError:
                window['output'].update("Невірний формат N. Введіть ціле число.")
            except Exception as e:
                window['output'].update(f"Помилка: {e}")

    window.close()


text = sg.Text("Виберіть завдання:", 
               justification='center', 
               size=(20, 1),
               font = ("Comic Sans", 16))

button_1 = sg.Button("Генератор випадкових фраз",
                     key = "button_1",
                     font = ("Comic Sans", 14),
                     expand_x=True)

button_2 = sg.Button("Аналіз файлу",
                     key = "button_2",
                     font = ("Comic Sans", 14),
                     expand_x=True)

button_3 = sg.Button("Пошук найчастіших послідовностей",
                     key = "button_3",
                     font = ("Comic Sans", 14),
                     expand_x=True)

exit = sg.Button("Вийти",
                 key = "exit",
                 button_color=("white", "red"),
                 expand_x=True,
                 font = ("Comic Sans", 14))

layout = [
    [text],
    [button_1],
    [button_2],
    [button_3],
    [exit]
]

window = sg.Window("Меню завдань", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "exit"):
        break
    if event == "button_1":
        zavd_1()
    elif event == "button_2":
        zavd_2()
    elif event == "button_3":
        zavd_3()

window.close()  