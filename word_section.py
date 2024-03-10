from tkinter import Tk, Button, messagebox
from password_dialog import show_password_dialog
from add_button import open_button_add_window
from delete_button import delete_button_root, delete_selected_buttons
from button_functions import button_data, open_excel_file

def word_section():
    global root_word
    root_word = Tk()
    root_word.title("단어장 선택하는 창")
    root_word.geometry("200x300")
    
    label_word = Label(root_word, text="원하시는 단어장을 선택해주세요")
    label_word.pack(fill="x", padx=10, pady=3)
    
    add_button = Button(root_word, text="버튼 추가하기", command=add_button_root)
    add_button.pack()

    delete_button = Button(root_word, text="버튼 삭제하기", command=delete_button_root)
    delete_button.pack()

    for name, filepath in button_data:
        button = Button(root_word, text=name, command=lambda path=filepath: open_excel_file(path))
        button.pack(fill="x", padx=10, pady=3)

    root_word.mainloop()
