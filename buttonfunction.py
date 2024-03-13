from tkinter import filedialog, simpledialog, messagebox
from openpyxl import load_workbook
import tkinter as tk

def load_button_data():
    try:
        button_data = []
        wb = load_workbook("savebuttondata.xlsx")
        sheet = wb.active
        for row in sheet.iter_rows(values_only=True):
            button_data.append(row)
        return button_data
    except FileNotFoundError:
        return []

def add_button():
    file_path = filedialog.askopenfilename(title="파일 선택", filetypes=(("Excel files", "*.xlsx"), ("모든 파일", "*.*")))
    if file_path:
        wb = load_workbook("savebuttondata.xlsx")
        sheet = wb.active
        button_name = simpledialog.askstring("버튼 이름 입력", "추가할 버튼의 이름을 입력하세요:")
        if button_name:
            sheet.append([button_name, file_path])
            wb.save("savebuttondata.xlsx")
            messagebox.showinfo("성공", "버튼 추가가 완료되었습니다.")
        else:
            messagebox.showwarning("경고", "버튼 이름을 입력하세요.")
    else:
        messagebox.showwarning("경고", "파일을 선택하세요.")

def delete_button():
    file_path = filedialog.askopenfilename(title="파일 선택", filetypes=(("Excel files", "*.xlsx"), ("모든 파일", "*.*")))
    if file_path:
        wb = load_workbook("savebuttondata.xlsx")
        sheet = wb.active
        button_names = [row[0].value for row in sheet.iter_rows(values_only=True)]
        selected_buttons = simpledialog.askstring("버튼 선택", "삭제할 버튼을 선택하세요:", initialvalue=", ".join(button_names))
        if selected_buttons:
            selected_buttons = [button.strip() for button in selected_buttons.split(",")]
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if row[0] in selected_buttons:
                    sheet.delete_rows(row[0].row)
            wb.save("savebuttondata.xlsx")
            messagebox.showinfo("성공", "선택한 버튼이 삭제되었습니다.")
        else:
            messagebox.showwarning("경고", "삭제할 버튼을 선택하세요.")
    else:
        messagebox.showwarning("경고", "파일을 선택하세요.")

def update_window(window):
    button_data = load_button_data()
    if not button_data:
        return
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()
    for button_name, file_path in button_data:
        button = tk.Button(window, text=button_name, command=lambda path=file_path: open_file(path))
        button.pack(pady=5)

# open_file 함수는 삭제됨
