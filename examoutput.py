import tkinter as tk

def create_exam_output_window():
    root = tk.Tk()
    root.title("시험지 출력")
    root.geometry("400x300")

    btn_exam_output = tk.Button(root, text="시험지 출력", command=print_exam_paper)
    btn_exam_output.pack(pady=20)

    root.mainloop()

def print_exam_paper():
    pass  # 시험지 출력 기능을 여기에 추가

if __name__ == "__main__":
    create_exam_output_window()
