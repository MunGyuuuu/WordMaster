import tkinter as tk

def update_password():
    global current_password
    new_password = entry.get()  # 입력된 새 비밀번호 가져오기
    current_password.set(new_password)  # 현재 비밀번호 업데이트

root = tk.Tk()
root.title("비밀번호 업데이트")

current_password = tk.StringVar()
current_password.set("현재 비밀번호: 1234")  # 초기 비밀번호 설정

label = tk.Label(root, textvariable=current_password)
label.pack(pady=10)

entry = tk.Entry(root, show="*")  # 입력 내용을 '*'로 숨김
entry.pack(pady=5)

button = tk.Button(root, text="비밀번호 변경", command=update_password)
button.pack(pady=5)

root.mainloop()
