import os
import FreeSimpleGUI as sg

def labs():

    papka = os.listdir("labs/")
    labs = []
    for i in papka:
        if i.startswith("lab"):
            number = i[3:]  
            labs.append(i + " - Лабораторна робота №" + number)
    return labs


def opys(lab_name):

    readme_path = f"labs/{lab_name}/README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Опис для цієї лабораторної роботи відсутній."


def run(lab_name):
    
    lab_name = lab_name.split(" - ")[0]
    lab_path = f"labs/{lab_name}/{lab_name}.py"
    if os.path.exists(lab_path):
        try:
            os.system(f"python {lab_path}")
        except Exception as e: 
            sg.popup(f"Помилка під час виконання {lab_name}: {e}", font=("Times New Roman", 14))
    else:
        sg.popup(f"Файл labX.py для {lab_name} не знайдено!", font=("Times New Roman", 14))