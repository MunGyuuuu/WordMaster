#버튼 추가하는 창
import tkinter as tk
from buttonfunction import summit_add_button

def add_button_dialog(callback_function):
    
    button_result = tk.StringVar()
    button_name = None
    
    root_addbuttondialog = tk.Tk()
    root_addbuttondialog.title("버튼 추가하는 창")
    root_addbuttondialog.geometry("300x200")

    textofbuttonname = tk.Label(root_addbuttondialog,text="버튼이름")
    textofbuttonname.pack()
    
    
    
    
    buttonoffilepath = tk.Button(root_addbuttondialog,command=lambda: button_result.set(open_excel_file()))
    buttonoffilepath.pack()

    summitbutton = tk.Button(root_addbuttondialog,command=lambda : summit_add_button(button_result,button_name))
