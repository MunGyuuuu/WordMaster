import tkinter as tk

password = '0000'
recentpassword = ''

# 비밀번호 라벨과 메시지 라벨을 전역 변수로 선언
password_label = None
message_label = None

def update_password():
    # password_label이 전역 변수로 선언되었는지 확인
    global password_label
    if password_label:
        password_label.config(text="현재 비밀번호는 " + recentpassword)
    check_password_length()

def remove_password():
    global recentpassword
    recentpassword = recentpassword[:-1]
    update_password()

def add_password(value):
    global recentpassword
    if len(recentpassword) < 4:  # 4자리를 넘어가지 않도록 제한
        recentpassword += value
        update_password()
    else:
        # 4자리를 넘어가면 오류 메시지를 표시
        if message_label:
            message_label.config(text="비밀번호는 4자리로 제한됩니다.")

def summit_check():
    if recentpassword == password:
        if message_label:
            message_label.config(text="비밀번호가 일치합니다.")
            return True
    else:
        if message_label:
            message_label.config(text="비밀번호가 일치하지 않습니다.")
            return False

def input_password():
    global password_label, message_label  # 전역 변수로 선언
    password_tk = tk.Tk()
    password_tk.title("비밀번호 4자리를 입력해주세요")
    password_tk.geometry("170x270")
    password_tk.resizable(False, False)

    password_label = tk.Label(password_tk, text="")
    password_label.grid(row=0, column=0, columnspan=3)

    buttons = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '←', '0', '확인'
    ]

    row_val = 1
    col_val = 0
    for button_text in buttons:
        if button_text == '확인':
            button = tk.Button(password_tk, text=button_text, command=summit_check, width=5, height=2)
        elif button_text == '←':
            button = tk.Button(password_tk, text=button_text, command=remove_password, width=5, height=2)
        else:
            button = tk.Button(password_tk, text=button_text, command=lambda text=button_text: add_password(text), width=5, height=2)

        button.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    # 메시지를 표시할 라벨 추가
    message_label = tk.Label(password_tk, text="")
    message_label.grid(row=row_val, column=0, columnspan=3)

    password_tk.mainloop()

def check_password_length():
    global message_label
    if len(recentpassword) > 4:
        if message_label:
            message_label.config(text="비밀번호는 4자리로 제한됩니다.")

input_password()
