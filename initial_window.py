from tkinter import Tk, Button, CENTER
from password_dialog import show_password_dialog
from word_section import word_section, load_button_data

root_first = Tk()
root_first.title("HOWTOENGLISH")
root_first.geometry("500x500+500+150")
root_first.resizable(True, True)

# 초기 화면에 있는 버튼 (단어장 선택)
make_button_word_section = Button(root_first, text="단어장 선택", relief="raised", borderwidth=5, command=lambda: [load_button_data(), word_section()])
make_button_word_section.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)  # CENTER 사용

root_first.mainloop()
