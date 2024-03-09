from tkinter import Tk, Button
from tkinter import CENTER  # CENTER를 사용하기 위해 추가

from 버튼함수 import word_section

root_first = Tk()
root_first.title("HOWTOENGLISH")
root_first.geometry("500x500+500+150")
root_first.resizable(True, True)

# 초기 화면에 있는 버튼 (단어장 선택)
make_button_word_section = Button(root_first, text="단어장 선택", relief="raised", borderwidth=5, command=word_section)
make_button_word_section.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)  # CENTER 사용
# relx, rely, relwidth, relheight는 부모에 대한 상대적인 크기와 위치를 나타내는 것이므로 어떤 값으로 설정해도 좋습니다.

root_first.mainloop()
