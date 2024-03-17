import tkinter as tk
import os
from tkinter import filedialog
import csv
from tkinter import messagebox

def add_textbox(filepath_textbox,buttonname_textbox):
    path = filedialog.askopenfilename()
    buttonname = buttonname_textbox.get()
    if buttonname == "":
        buttonname=os.path.splitext(os.path.basename(path))[0]
        buttonname_textbox.insert(0,buttonname)
    filepath_textbox.insert(0,path)

def write_csv(data):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    csv_data = os.path.join(script_dir, 'database.csv')
    path = script_dir + '\\' + 'database.csv'
    try:
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data) 
        return 1 
    except Exception as e:
        return 0
    


def summit_add_button(file_path, button_name, root):
    data = [button_name, file_path]
    if write_csv(data):
        messagebox.showinfo("성공", "저장되었습니다.")
        root.destroy()  # 현재 창 닫기
        create_word_selection_window()  # 새 창 열기
    else:
        messagebox.showinfo("실패", "실패하였습니다.")

def add_button_dialog_function():
    root_addbuttondialog = tk.Tk()
    root_addbuttondialog.title("버튼 추가하는 창")
    root_addbuttondialog.geometry("370x100")
    root_addbuttondialog.resizable(width=False, height=False)


    textofbuttonname = tk.Label(root_addbuttondialog,text="버튼이름")
    textofbuttonname.grid(row=0, column=0, padx=5, pady=5)
    textboxofbuttonname = tk.Entry(root_addbuttondialog, width = 30)
    textboxofbuttonname.grid(row=0, column=1, padx=5, pady=5)

    textoffilepath = tk.Label(root_addbuttondialog,text = "파일경로")
    textoffilepath.grid(row=1, column=0, padx=(5,5),pady=5)
    textboxoffilepath = tk.Entry(root_addbuttondialog,width=20)
    textboxoffilepath.grid(row=1,column=1, padx=(0,3),pady=5)
    buttonoffilepath = tk.Button(root_addbuttondialog,text="파일선택",command=lambda: add_textbox(textboxoffilepath,textboxofbuttonname))
    buttonoffilepath.grid(row=1,column=2,padx=(0,20),pady=5)


    summitbutton = tk.Button(root_addbuttondialog,text="제출",width = 20,command=lambda: summit_add_button(textboxoffilepath.get(), textboxofbuttonname.get(),root_addbuttondialog))
    summitbutton.grid(sticky='S', column=1,padx=5)

    root_addbuttondialog.mainloop()

add_button_dialog_function()
