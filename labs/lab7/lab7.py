import FreeSimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import os

sg.theme("DarkTeal9")

out_folder = "labs/lab7/graphs"
if not os.path.exists(out_folder):
    os.makedirs(out_folder)


def zavd1():
    x = np.linspace(0.01, 5, 1000)
    y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

    file_path = out_folder + "/function.png"

    plt.plot(x, y, color="pink", label=r"$F(x) = \frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Графік функції F(x) = 5 * cos(10x) * sin(3x) / sqrt(x)")
    plt.legend()
    plt.savefig(file_path)
    plt.close()
    return file_path

def zavd2(input_text):

    text = input_text.lower().replace(" ", "")
    count = Counter(text)
    letters = list(count.keys())
    frequencies = list(count.values())

    file_path = out_folder + "/histograma.png"

    plt.bar(letters, frequencies, color="pink")
    plt.xlabel("Літери")
    plt.ylabel("Частота")
    plt.title("Частота літер у тексті")
    plt.savefig(file_path)    
    plt.close()
    return file_path

def zavd3(input_text):
    text = input_text.replace("...", " <<TripleDot>> ")

    prosti = []
    potal = []
    oklich = []
    trykrap = []

    words = text.split()
    for word in words:
        if "<<TripleDot>>" in word:
            trykrap.append(word)
        elif word.endswith("!"):
            oklich.append(word)
        elif word.endswith("?"):
            potal.append(word)
        elif word.endswith("."):
            prosti.append(word)

    types = ["Прості", "Питальні", "Окличні", "Три крапки"]
    frequencies = [len(prosti), len(potal), len(oklich), len(trykrap)]

    file_path = out_folder + "/histograma_2.png"

    plt.bar(types, frequencies, color=["blue", "green", "red", "orange"])
    plt.xlabel("Типи речень")
    plt.ylabel("Частота")
    plt.title("Частота появи різних типів речень у тексті")
    plt.savefig(file_path)
    plt.close()     
    return file_path


text_1 = sg.Text("Натисніть кнопку для побудови графіка функції:", 
                 font=("Comic Sans", 16))
button_1 = sg.Button("Побудувати графік", 
                     key="button1", 
                     font=("Comic Sans", 14),
                     expand_x = True,
                     expand_y= True)
image_1 = sg.Image(key="image_1")

layout_tab1 = [
    [text_1],
    [button_1],
    [image_1]
]


text_2 = sg.Text("Введіть текст для аналізу:", 
                 font=("Comic Sans", 16))
input_2 = sg.Input(key="input_2", 
                   font=("Comic Sans", 16),
                     expand_x = True)
button_2 = sg.Button("Аналізувати", 
                     key="button2", 
                     font=("Comic Sans", 14),
                     expand_x = True)
image_2 = sg.Image(key="image_2")

layout_tab2 = [
    [text_2],
    [input_2],
    [button_2],
    [image_2]
]


text_3 = sg.Text("Введіть текст для аналізу типів речень:", 
                 font=("Comic Sans", 16))
input_3 = sg.Input(key="input_3", 
                   font=("Comic Sans", 16),
                     expand_x = True)
button_3 = sg.Button("Аналізувати", 
                     key="button3", 
                     font=("Comic Sans", 14),
                     expand_x = True)
image_3 = sg.Image(key="image_3")

layout_tab3 = [
    [text_3],
    [input_3],
    [button_3],
    [image_3]
]

tab1 = sg.Tab("Графік функції", layout_tab1)
tab2 = sg.Tab("Аналіз тексту", layout_tab2)
tab3 = sg.Tab("Аналіз типів речень", layout_tab3)
exit = sg.Button("Вихід", 
                 key="exit", 
                 font=("Comic Sans", 14), 
                 button_color=("white", "red"),
                 expand_x=True)


layout = [
    [sg.TabGroup([[tab1, tab2, tab3]], font = ("Comic Sans", 10))],
     [exit]
]

window = sg.Window("Меню завдань", layout)


while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "exit"):
        break
    if event == "button1":
        graph_path = zavd1()
        window["image_1"].update(graph_path)
    elif event == "button2":
        input_text = values["input_2"]
        if input_text:
            hist_path = zavd2(input_text)
            window["image_2"].update(hist_path)
        else:
            sg.popup("Будь ласка, введіть текст для аналізу!")
    elif event == "button3":
        input_text = values["input_3"]
        if input_text:
            hist_path = zavd3(input_text)
            window["image_3"].update(hist_path)
        else:
            sg.popup("Будь ласка, введіть текст для аналізу!")



window.close()
