#버튼 추가하는 창
import tkinter as tk
from buttonfunction import add_button

def add_button_dialog(callback_function):
    root_addbuttondialog = tk.Tk()
    root_addbuttondialog.title("버튼 추가하는 창")
    root_addbuttondialog.geometry("300X400")

    textfobuttonname = tk.Label(root_addbuttondialog,text="버튼이름")
    textfobuttonname.pack()

add_button_dialog(add_button)
