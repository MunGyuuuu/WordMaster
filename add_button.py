import tkinter as tk
from tkinter import filedialog
from button_functions import show_password_dialog, add_word_list, get_file_path

# 버튼 추가 창 열기
def open_button_add_window():
    root_addbutton = tk.Tk()
    root_addbutton.geometry("300x150")
    root_addbutton.title("버튼 추가하는 창")

    # Entry 위젯 생성
    label_addbutton_name = tk.Label(root_addbutton, text="파일 이름")
    label_addbutton_name.pack()

    textbox_addbutton_name = tk.Entry(root_addbutton)
    textbox_addbutton_name.pack()

    label_addbutton_filepath = tk.Label(root_addbutton, text="파일 경로")
    label_addbutton_filepath.pack()

    textbox_addbutton_filepath = tk.Entry(root_addbutton)
    textbox_addbutton_filepath.pack()

    # 파일 선택 버튼
    select_file_button = tk.Button(root_addbutton, text="파일 선택", command=lambda: get_file_path(textbox_addbutton_filepath, textbox_addbutton_name))
    select_file_button.pack()

    summit_button = tk.Button(root_addbutton, text="제출", command=lambda: add_word_list(textbox_addbutton_name.get(), textbox_addbutton_filepath.get(), root_addbutton))
    summit_button.pack()
