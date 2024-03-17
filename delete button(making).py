import tkinter as tk
from wordsection import read_csv, write_csv

def delete_csv(name):
    data = read_csv()
    new_data = [line for line in data if line[0] != name]
    return new_data

def summit_delete_button(check_list, button_list):
    for i, check in enumerate(check_list):
        if check.get():
            checked_button_name = button_list[i][0]
            data = delete_csv(checked_button_name)
            write_csv(data)

def delete_button_dialog_function():
    root_deletebuttondialog = tk.Tk()
    root_deletebuttondialog.title("버튼삭제하는 창")
    root_deletebuttondialog.geometry("300x500")

    labeldeletebutton = tk.Label(root_deletebuttondialog, text="버튼을 삭제하시면 체크박스에 체크해주세요")
    labeldeletebutton.grid(row=0)

    button_list = read_csv()
    check_list = []

    for i, button_data in enumerate(button_list):
        name = button_data[0]
        check = tk.BooleanVar()
        check_list.append(check)
        button_checkbox = tk.Checkbutton(root_deletebuttondialog, text=name, variable=check)
        button_checkbox.grid(row=i+1)

    summit_button = tk.Button(root_deletebuttondialog, text="제출", command=lambda: summit_delete_button(check_list, button_list))
    summit_button.grid(row=len(button_list) + 1)
    root_deletebuttondialog.mainloop()

delete_button_dialog_function()
