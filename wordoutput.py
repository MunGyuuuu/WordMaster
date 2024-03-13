import tkinter as tk

def create_word_output_window():
    root = tk.Tk()
    root.title("단어장 출력")
    root.geometry("400x300")

    btn_word_output = tk.Button(root, text="단어장 출력", command=print_word_list)
    btn_word_output.pack(pady=20)

    root.mainloop()

def print_word_list():
    pass  # 단어장 출력 기능을 여기에 추가

if __name__ == "__main__":
    create_word_output_window()
