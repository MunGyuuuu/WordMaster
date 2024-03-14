import tkinter as tk
from buttonfunction import update_window,delete_button
from password_dialog import show_password_dialog
from add_button_dialog import add_button_dialog

def create_word_selection_window():
    root = tk.Tk()
    root.title("단어장 선택")
    root.geometry("400x300")

    btn_add = tk.Button(root, text="버튼 추가하기", command=lambda: show_password_dialog(add_button_dialog))
    btn_add.pack(pady=20)

    btn_delete = tk.Button(root, text="버튼 삭제하기", command=lambda: show_password_dialog(delete_button))
    btn_delete.pack(pady=10)

    update_window(root)

    root.mainloop()
