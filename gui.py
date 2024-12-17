import FreeSimpleGUI as sg
import functions as f




sg.theme("DarkTeal9")

lab_list = sg.Text("Список лабораторних робіт:", 
                   font = ("Comic Sans", 16))

lab_box = sg.Listbox(values = f.labs(), 
                     size = (50, 10), 
                     key = "lab_list", 
                     enable_events = True, 
                     font = ("Comic Sans", 14))


opys_lab = sg.Text("Опис лабораторної роботи:", 
                   font = ("Comic Sans", 16))

opys_box = sg.Multiline("Виберіть лабораторну роботу, щоб побачити її опис.", 
                        size = (50, 10), 
                        key = "opys_lab", 
                        font = ("Comic Sans", 14), 
                        disabled = True)

run = sg.Button("Запустити",
                key = "run",
                font = ("Comic Sans", 14))

cancel = sg.Button("Вихід",
                   key = "cancel",
                   font = ("Comic Sans", 14),
                   button_color = ("white", "red"))



layout = [ [lab_list],
          [lab_box],
          [opys_lab],
          [opys_box],
          [run, cancel]]
        
window = sg.Window("Лабораторні роботи", layout)


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "cancel"):
        break


    elif event == "lab_list":
        sel_lab = values["lab_list"]
        if sel_lab:
            sel_lab = sel_lab[0]
            labs = sel_lab.split(" - ")
            opys = f.opys(labs[0])
            window["opys_lab"].update(opys)

    elif event == "run":
        sel_lab = values["lab_list"]
        if sel_lab:
            f.run(sel_lab[0])
        else:
            sg.popup("Виберіть лабораторну роботу для запуску!", 
                     font = ("Comic Sans", 14))


window.close()



