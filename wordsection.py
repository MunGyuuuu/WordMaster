import tkinter as tk
from buttonfunction import add_button, delete_button, update_window

def create_word_selection_window():
    root = tk.Tk()
    root.title("단어장 선택")
    root.geometry("400x300")

    btn_add = tk.Button(root, text="버튼 추가하기", command=add_button)
    btn_add.pack(pady=20)

    btn_delete = tk.Button(root, text="버튼 삭제하기", command=delete_button)
    btn_delete.pack(pady=10)

    update_window(root)

    root.mainloop()

if __name__ == "__main__":
    create_word_selection_window()
