import tkinter as tk
from button_functions import show_password_dialog, delete_selected_buttons

# 삭제 버튼 창 열기
def delete_button_root():
    show_password_dialog(delete_selected_buttons)
