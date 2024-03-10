from tkinter import Tk, Entry, Label, Button, messagebox
import tkinter as tk

check_password = '0000'

# 비밀번호 확인하는 함수
def verify_password(password):
    return password == check_password

# 비밀번호 창 보여주기
def show_password_dialog(callback_function):
    password_check_window = tk.Tk()
    password_check_window.title("비밀번호 확인")
    password_check_window.geometry("200x100")

    label_password = tk.Label(password_check_window, text="비밀번호를 입력하세요:")
    label_password.pack()

    entry_password = tk.Entry(password_check_window, show="*")  # 입력 내용 감춤
    entry_password.pack()

    # 확인 버튼
    confirm_button = tk.Button(password_check_window, text="확인", command=lambda: verify_and_continue(entry_password.get(), password_check_window, callback_function))
    confirm_button.pack()

    password_check_window.mainloop()

# 비밀번호 확인 후 작업 수행
def verify_and_continue(password, window, callback_function):
    if verify_password(password):
        window.destroy()  # 비밀번호 확인 창 닫기
        callback_function()  # 콜백 함수 호출
    else:
        # 잘못된 비밀번호를 입력한 경우 메시지 출력
        messagebox.showerror("오류", "잘못된 비밀번호입니다.")
