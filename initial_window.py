import tkinter as tk
from wordsection import create_word_selection_window

def create_initial_window():
    root = tk.Tk()
    root.title("초기 창")
    root.geometry("300x200")

    btn_select_word = tk.Button(root, text="단어장 선택", command=create_word_selection_window)
    btn_select_word.pack(pady=10)

    root.mainloop()

create_initial_window()
