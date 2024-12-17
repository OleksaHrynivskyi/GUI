import FreeSimpleGUI as sg
import function as f


sg.theme("DarkTeal9")

menu = sg.Text("Меню управління студентами",
               font = ("Comic Sans", 16))

students = sg.Text("Група (наприклад 11-КІ)",
                   font = ("Comic Sans", 14))

students_input = sg.Input(key = "group",
                          font = ("Comic Sans", 14),
                          expand_x=True)


surname_text = sg.Text("Прізвище студента:",
                       font = ("Comic Sans", 14))

surname_input = sg.Input(key = "surname", 
                          font = ("Comic Sans", 14),
                          expand_x=True)

avg_bal_text = sg.Text("Середній бал студента:",
                       font = ("Comic Sans", 14))

avg_bal_input = sg.Input(key = "avg_bal", 
                         font = ("Comic Sans", 14),
                          expand_x=True)


delete_index_text = sg.Text("Номер студента для видалення:",
                            font = ("Comic Sans", 14))

delete_index_input = sg.Input(key = "delete_index", 
                              font = ("Comic Sans", 14),
                              expand_x=True)


student_add = sg.Button("Додати студента",
                        key = "add",
                        font = ("Comic Sans", 14))

sutdent_show = sg.Button("Відобразити студентів",
                         key = "show",
                         font = ("Comic Sans", 14))

student_find = sg.Button("Знайти студента",
                         key = "find",
                         font = ("Comic Sans", 14))

student_sort = sg.Button("Сортувати студентів",
                         key = "sort",
                         font = ("Comic Sans", 14))

student_delete = sg.Button("Видалити студента",
                           key = "delete",
                           font = ("Comic Sans", 14))

opys_box = sg.Multiline("",
                        size = (60, 10),
                        key = "result",
                        font = ("Comic Sans", 14),
                        disabled = True)

exit = sg.Button("Вийти з програми",
                 key = "exit",
                 font = ("Comic Sans", 14),
                 button_color = ("white", "red"))



layout = [
    [menu],
    [students, students_input],

    [surname_text, surname_input],
    [avg_bal_text, avg_bal_input],
    [delete_index_text, delete_index_input],

    [student_add, 
     sutdent_show, 
     student_find, 
     student_sort, 
     student_delete],

    [opys_box, sg.Push(), exit, sg.Push()]
]



window = sg.Window("Управління студентами", layout)


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "exit"):
        break


    group = values["group"]
    if not group:
        window["result"].update("Будь ласка, введіть групу!")
        continue
    group = group + ".txt" 
    group = "labs/lab3/" + group


    if event == "add":
        surname = values["surname"]
        avg_bal = values["avg_bal"]
        try:
            avg_bal = float(avg_bal)
            if surname and avg_bal:
                result = f.add_student(group, surname, avg_bal)
            else:
                result = "Будь ласка, введіть всі дані!"
            window["result"].update(result)
        except ValueError:
            window["result"].update("Середній бал повинен бути числом!")
        
    elif event == "show":
        result = f.show_students(group)
        window["result"].update(result)

    elif event == "find":
        student_name = values["surname"]
        if student_name:
            result = f.find_student(group, student_name)
        else:
            result = "Будь ласка, введіть прізвище студента для пошуку!"
        window["result"].update(result)

    elif event == "sort":
        result = f.sort_students(group)
        window["result"].update(result)

    elif event == "delete":
        try:
            delete_index = int(values["delete_index"])
            result = f.delete_student(group, delete_index)
        except ValueError:
            result = "Невірний номер студента для видалення!"
        window["result"].update(result)

window.close()
