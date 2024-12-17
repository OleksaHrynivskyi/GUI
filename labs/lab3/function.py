import FreeSimpleGUI as sg


def read_file(file_name):
    try: 
        with open(file_name, 'r', encoding = "utf-8") as file_local:
            datas = file_local.readlines()
            return datas
    except FileNotFoundError:
        sg.popup(f"Файл {file_name} не знайдено. Відбулося автоматичне створення файлу {file_name}",
                 font = ("Comic Sans", 14))
        return []


def write_file(file_name, data):
        with open(file_name, 'w', encoding = "utf-8") as file_local:
            file_local.writelines(data)



def add_student(group, surname, avg_bal):
    data = read_file(group)
    data.append(f"{surname} {avg_bal}\n")
    write_file(group, data)
    return "Дані успішно додані."


def show_students(group):
    data = read_file(group)
    if not data:
        return "Список студентів порожній."
    list = ""
    for i, entry in enumerate(data):
        list += (f"{i + 1}. {entry.strip()}\n")
    return list


def find_student(group, surname):
    data = read_file(group)
    found = False
    for i in data:
        if i.startswith(surname):
            surname, avg_bal = i.strip().split(" ")
            found = True
            return f"Студент {surname} знайдений у списку з середнім балом - {avg_bal}"
    if not found:
        return "Студента не знайдено."
    

def sort_students(group):
    data = read_file(group)
    sorted_data = sorted(data, reverse=True)
    if not sorted_data:
        return "Список порожній"
    sorted_list = "\n".join([entry.strip() for entry in sorted_data])
    return f"Список студентів відсортований за середнім балом:\n{sorted_list}"

def delete_student(group, index):
    data = read_file(group)
    if index < 1 or index > len(data):
        return "Номер студента повинен бути в межах списку."
    student_to_delete = data[index - 1].strip()
    data.pop(index - 1)
    write_file(group, data)
    return f"Студента {student_to_delete} успішно видалено."


