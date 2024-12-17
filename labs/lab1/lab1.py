from math import *
import random
import FreeSimpleGUI as sg

sg.theme("DarkTeal9")


def math():
    text = sg.Text("Введіть додатнє число m для обрахунку 1/(√m+√2)",
                   font=("Comic Sans", 16))    
    input = sg.Input(key="input",
                     font=("Comic Sans", 16),
                     expand_x= True)
    button = sg.Button("Розрахувати",
                       key="button",
                       font=("Comic Sans", 14),
                       expand_x=True)
    result = sg.Text("",
                     key="result",
                     font=("Comic Sans", 14))
    back = sg.Button("Назад",
                     key="back",
                     font=("Comic Sans", 16),
                     button_color=("white", "red"),
                     expand_x=True)

    layout = [
        [text],
        [input],
        [button],
        [result],
        [back]
    ]

    window = sg.Window("Математичний вираз", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "back"):
            break
        elif event == "button":
            m = values["input"]
            if not m:
                window["result"].update("Будь ласка, введіть число!")
                continue
            try:
                m = float(m)                
                if m < 0:
                    print("Ви ввели не додатнє число!")
                else:
                    z = 1/(sqrt(m)+sqrt(2))
                    window["result"].update(f"Підрахований вираз - {z}")
            except ValueError:
                window["result"].update("Ви ввели не число")

    window.close()


def proste():
    text = sg.Text("Введіть число",
                   font=("Comic Sans", 16))

    input = sg.Input(key="input",
                     font=("Comic Sans", 16))

    button = sg.Button("Перевірити",
                       key="button",
                       font=("Comic Sans", 14),
                       expand_x=True)
    
    result = sg.Text("",
                     key="result",
                     font=("Comic Sans", 14))

    back = sg.Button("Назад",
                     key="back",
                     font=("Comic Sans", 16),
                     button_color=("white", "red"),
                     expand_x=True)
    
    layout = [
        [text],
        [input],
        [button],
        [result],
        [back]
    ]

    window = sg.Window("Просте число", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "back"):
            break
        elif event == "button":
            number = values["input"]
            try:
                number = int(number)

                if number <= 1:
                    window["result"].update(f"Число {number} не є простим.")
                else:
                    is_prime = True

                    if number == 2:
                        is_prime = True
                    elif number % 2 == 0:
                        is_prime = False
                    else:
                        for i in range(3, int(sqrt(number)) + 1, 2):
                            if number % i == 0:
                                is_prime = False
                                break

                    if is_prime:
                        window["result"].update(f"Число {number} є простим.")
                    else:
                        window["result"].update(f"Число {number} не є простим.")
            except ValueError:
                window["result"].update("Ви ввели не число")

    window.close()


def spysok():
    text = sg.Text("Введіть кількість елементів списку", 
                   font=("Comic Sans", 16))
    input = sg.Input(key="input", 
                     font=("Comic Sans", 16))
    button_1 = sg.Button("Згенерувати", 
                         key="button", 
                         font=("Comic Sans", 16), 
                         expand_x=True)
    spys = sg.Text("Згенерований список: ", 
                   font=("Comic Sans", 14))
    spys_2 = sg.Text(key="result", 
                     font=("Comic Sans", 14))
    min = sg.Text("Мінімальний додатній елемент: ", 
                  font=("Comic Sans", 14))
    min_2 = sg.Text(key="min", 
                    font=("Comic Sans", 14))
    sum = sg.Text("Сума парних елементів: ", 
                  font=("Comic Sans", 14))
    sum_2 = sg.Text(key="sum", 
                    font=("Comic Sans", 14))
    zvorot = sg.Text("Зворотній список: ", 
                     font=("Comic Sans", 14))
    zvorot_2 = sg.Text(key="zvorot",                        
                       font=("Comic Sans", 14))
    back = sg.Button("Назад", 
                     key="back", 
                     font=("Comic Sans", 16), 
                     button_color=("white", "red"), 
                     expand_x=True)
  
    layout = [
        [text],
        [input],
        [button_1],
        [spys, spys_2],
        [min, min_2],
        [sum, sum_2],
        [zvorot, zvorot_2],
        [back]
    ]

    window = sg.Window("Список", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "back"):
            break
        elif event == "button":
            try:
                n = int(values["input"])
                spysok_random = [random.randint(-10, 10) for _ in range(n)]
                window["result"].update(spysok_random)
                        
                min_spys = []
                for i in spysok_random:
                    if i > 0:
                        min_spys.append(i)
                if not min_spys:
                    window["min"].update("Немає додатніх елементів")
                else:
                    min_number = min_spys[0]         # Непонятно чого не працює функція min, тому написав сам
                    for number in min_spys:
                        if number < min_number:
                            min_number = number
                    window["min"].update(min_number)

                sum_spys = []
                for i in spysok_random:
                    if i % 2 == 0:
                        sum_spys.append(i)
                if not sum_spys:
                    window["sum"].update("Немає парних елементів")
                else:
                    total = 0                         # Непонятно чого не працює функція sum, тому написав сам
                    for number in sum_spys:
                        total += number
                    window["sum"].update(total)

                zvorot = spysok_random[::-1]
                window["zvorot"].update(zvorot)
            except ValueError:
                window["result"].update("Будь ласка, введіть ціле число!")

    window.close()


text = sg.Text("Меню завдань",
               font=("Comic Sans", 16),
               justification='center', 
               size=(20, 1))

button1 = sg.Button("Математичний вираз",
                    key="button1",
                    font=("Comic Sans", 14),
                    expand_x=True)

button2 = sg.Button("Просте число",
                    key="button2",
                    font=("Comic Sans", 14),
                    expand_x=True)

button3 = sg.Button("Список",
                    key="button3",
                    font=("Comic Sans", 14),
                    expand_x=True)

exit = sg.Button("Вихід",
                 key="exit",
                 font=("Comic Sans", 14),
                 button_color=("white", "red"),
                 expand_x=True)

layout = [
    [text],
    [button1],
    [button2],
    [button3],
    [exit]
]

window = sg.Window("Меню завдань", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "exit"):
        break
    elif event == "button1":
        math()
    elif event == "button2":
        proste()
    elif event == "button3":
        spysok()

window.close()
