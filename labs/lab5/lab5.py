import FreeSimpleGUI as sg

class Povtory(str):
    def povtory_sliv(self, s):
        
        words = s.lower().split()
        symv3 = []
        
        
        for i in words:
            if len(i) > 3:
                symv3.append(i) 
        
        
        for word in symv3:
            if symv3.count(word) > 1:
                return True
            return False
       


    def palindrome(self):
        ryadok = self.lower()
        return ryadok == ryadok[::-1]



sg.theme("DarkTeal9")

text = sg.Text("Перевірка рядку на повтори і паліндром",
               font = ("Comic Sans", 16))
text1 = sg.Text("Введіть рядок:",
                font = ("Comic Sans", 14))

input = sg.Input(key = "input",
                 font = ("Comic Sans", 16))

button = sg.Button("Перевірити",
                   key = "button",
                   font = ("Comic Sans", 14))

result = sg.Text("",
                 key = "result",
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
    [result],
    [exit]
]

window = sg.Window("Перевірка рядка", layout)
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "exit"):
        break

    elif event == "button":
        input = values["input"]
        if not input:
            window["result"].update("Будь ласка, введіть рядок!")
            continue

        input = Povtory(input)        
    
        palindrom = input.palindrome()
        repeat = input.povtory_sliv(input)

        final = f"Паліндром: {'Так' if palindrom else 'Ні'}\n"
        final += f"Повтори слів > 3 символів: {'Так' if repeat else 'Ні'}"

        window["result"].update(final)


window.close()

