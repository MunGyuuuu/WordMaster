import tkinter as tk
import os
from tkinter import filedialog, messagebox
import csv
from password_dialog import show_password_dialog

def create_word_selection_window():
    root = tk.Tk()
    root.title("단어장 선택")
    root.geometry("400x300")

    btn_add = tk.Button(root, text="버튼 추가하기", command=lambda: show_password_dialog(lambda: add_button_dialog_function(root)))
    btn_add.pack(pady=20)

    btn_delete = tk.Button(root, text="버튼 삭제하기", command=lambda: show_password_dialog(lambda: delete_button_dialog_function(root)))
    btn_delete.pack(pady=10)

    update_window(root)

    root.mainloop()

def update_window(root):
    data = read_csv()
    for line in data:
        button_name = line[0]
        file_path = line[1]
        button = tk.Button(root, text=button_name)
        button.pack()

    
def add_textbox(filepath_textbox,buttonname_textbox):
    path = filedialog.askopenfilename()
    buttonname = buttonname_textbox.get()
    if buttonname == "":
        buttonname=os.path.splitext(os.path.basename(path))[0]
        buttonname_textbox.insert(0,buttonname)
    filepath_textbox.insert(0,path)

def write_csv(data_list):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    csv_data = os.path.join(script_dir, 'database.csv')
    path = script_dir + '\\' + 'database.csv'
    try:
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            for data in data_list:
                writer.writerow(data)
        return 1 
    except Exception as e:
        return 0
    

def read_csv():
    data = []
    script_dir = os.path.dirname(os.path.realpath(__file__))
    csv_data = os.path.join(script_dir, 'database.csv')
    path = script_dir + '\\' + 'database.csv'
    try:
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # 빈 줄 건너뛰기
                    data.append(row)
        return data
    except Exception as e:
        messagebox.showinfo("오류", "파일을 읽어오는 도중 오류가 발생했습니다.")
        return None
    
    


def summit_add_button(file_path, button_name, root_addbuttondialog, root):
    data = [button_name, file_path]
    if write_csv(data):
        messagebox.showinfo("성공", "저장되었습니다.")
        root_addbuttondialog.destroy()
        root.destroy()  # root 창도 함께 닫음
        create_word_selection_window()  # 새 창 열기
    else:
        messagebox.showinfo("실패", "실패하였습니다.")


def add_button_dialog_function(root):
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


    summitbutton = tk.Button(root_addbuttondialog,text="제출",width = 20,command=lambda: summit_add_button(textboxoffilepath.get(), textboxofbuttonname.get(),root_addbuttondialog,root))
    summitbutton.grid(sticky='S', column=1,padx=5)

    root_addbuttondialog.mainloop()


def delete_button_dialog_function():
    root_deletebuttondialog = tk.Tk()
    root_deletebuttondialog.title("버튼삭제하는 창")
    root_deletebuttondialog.geometry("300x500")
    
    labeldeletebutton = tk.Label(root_deletebuttondialog,text="버튼을 삭제하시면 체크박스에 체크해주세요")
    labeldeletebutton.grid(row=0)
    
    root_deletebuttondialog.mainloop()
delete_button_dialog_function()
