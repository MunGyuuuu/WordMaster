import tkinter as tk
from buttonfunction import summit_add_button,open_file

def add_button_dialog(callback_function):
    
    root_addbuttondialog = tk.Tk()
    root_addbuttondialog.title("버튼 추가하는 창")
    root_addbuttondialog.geometry("300x200")

    textofbuttonname = tk.Label(root_addbuttondialog,text="버튼이름")
    textofbuttonname.pack()
    textboxofbuttonname = tk.Entry(root_addbuttondialog, width = 30)
    textboxofbuttonname.pack()

    buttonoffilepath = tk.Button(root_addbuttondialog,text="파일선택",command=lambda: open_file())
    buttonoffilepath.pack()

    summitbutton = tk.Button(root_addbuttondialog,text="제출",command=lambda: summit_add_button(textboxofbuttonname.get(), open_file()))
    summitbutton.pack()
    
    root_addbuttondialog.mainloop()

add_button_dialog(summit_add_button)