import tkinter as tk
import win32com.client as win32
import subprocess

def extract_words_from_hwp_table(file_path):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

    try:
        hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")
        hwp.Open(file_path)
        hwp.InitScan(0)
        hwp.GetText()

        word_list = []

        # 표의 텍스트를 읽어옴
        table_count = hwp.GetTableCount()
        for table_index in range(table_count):
            hwp.MoveToTable(table_index)
            row_count = hwp.GetTableRowCount()
            # 각 행에 대해
            for row_index in range(row_count):
                # 한 행에 4열씩 있으므로 각 열을 읽어옴
                for col_index in range(0, hwp.GetTableColCount() - 1, 2):
                    # 영어 단어와 한글 해석을 읽어옴
                    word = hwp.GetTextFromTable(table_index, row_index, col_index)
                    translation = hwp.GetTextFromTable(table_index, row_index, col_index + 1)
                    # 영어 단어와 해당 단어의 한글 해석을 튜플로 저장
                    if word and translation:
                        word_list.append((word, translation))

        return word_list

    finally:
        hwp.Quit()

def create_exam_hwp(word_list):
    # 한컴오피스 객체 생성
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

    # 새 문서 생성
    hwp.HAction.GetDefault("DocumentNew")
    hwp.HAction.Execute()

    # 표 삽입
    table_row_count = 32  # 첫 번째 줄에 헤더가 추가되므로 행 수를 32로 설정
    table_column_count = 4
    hwp.HAction.GetDefault("TableIns")
    hwp.HParameterSet.SetItem("RowCount", table_row_count)
    hwp.HParameterSet.SetItem("ColumnCount", table_column_count)
    hwp.HParameterSet.SetItem("TableProperty", "0")
    hwp.HParameterSet.SetItem("AutoStyle", "DefaultTable")
    hwp.HAction.Execute()

    # 표 내용 채우기
    # 헤더 채우기: 이름 빈칸 빈칸 빈칸
    hwp.HAction.Run("TableCellBlock")
    hwp.HParameterSet.SetItem("BlockType", "Cell")
    hwp.HAction.Execute()
    hwp.HAction.Run("CharShapeBold")
    hwp.HParameterSet.SetItem("CharShape", 1)
    hwp.HAction.Execute()
    hwp.HAction.Run("TableCellInput")
    hwp.HParameterSet.SetItem("Text", "이름")
    hwp.HAction.Execute()

    # 나머지 헤더 채우기
    hwp.HAction.Run("TableRightCell")
    for i in range(1, table_column_count):
        hwp.HAction.Run("TableCellBlock")
        hwp.HParameterSet.SetItem("BlockType", "Cell")
        hwp.HAction.Execute()
        hwp.HAction.Run("TableCellInput")
        hwp.HParameterSet.SetItem("Text", f"단어 {i}")
        hwp.HAction.Execute()

    # 테이블 데이터 채우기
    for i, (word, translation) in enumerate(word_list, start=1):
        row = i + 1  # 첫 번째 행은 헤더이므로 인덱스를 1부터 시작
        # 단어 채우기
        hwp.HAction.Run("TableRowNext")
        hwp.HAction.Run("TableCellBlock")
        hwp.HParameterSet.SetItem("BlockType", "Cell")
        hwp.HAction.Execute()
        hwp.HAction.Run("TableCellInput")
        hwp.HParameterSet.SetItem("Text", word)
        hwp.HAction.Execute()
        # 해석 채우기
        hwp.HAction.Run("TableRightCell")
        hwp.HAction.Run("TableCellBlock")
        hwp.HParameterSet.SetItem("BlockType", "Cell")
        hwp.HAction.Execute()
        hwp.HAction.Run("TableCellInput")
        hwp.HParameterSet.SetItem("Text", translation)
        hwp.HAction.Execute()

    # 파일 저장
    hwp.HAction.GetDefault("FileSaveAs")
    hwp.HParameterSet.SetItem("FileName", "시험지.hwp")
    hwp.HAction.Execute()

    # 한컴오피스 종료
    hwp.Quit()

def create_exam_output_window(filepath):
    root = tk.Toplevel()
    root.title("시험지 출력")
    root.geometry("400x300")

    btn_exam_output = tk.Button(root, text="시험지 출력", command=makeexamfile(filepath))
    btn_exam_output.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

def print_exam_paper():
    pass  # 시험지 출력 기능을 여기에 추가

def create_word_output_window(filepath):
    root = tk.Toplevel()
    root.title("단어장 출력")
    root.geometry("400x300")

    btn_word_output = tk.Button(root, text="단어장 출력", command=print_hwp_file(filepath))
    btn_word_output.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

def print_hwp_file(filepath):
    try:
        # 한컴오피스를 사용하여 HWP 파일을 인쇄하는 명령을 실행합니다.
        # 여기서는 한컴오피스의 hwp.exe를 사용하여 파일을 인쇄합니다.
        # 실제 사용하는 프로그램에 따라 인쇄 명령이 다를 수 있습니다.
        subprocess.run(['C:\\Program Files (x86)\\HNC\\HOffice10\\Bin\\hwp.exe', '/p', filepath], check=True)
        print("파일이 인쇄되었습니다.")
    except subprocess.CalledProcessError as e:
        print("인쇄 중 오류가 발생했습니다:", e)
    except FileNotFoundError:
        print("한컴오피스가 설치되어 있지 않습니다.")


def outputdialog(filepath):
    rt_otd = tk.Tk()
    rt_otd.title("단어창 출력 또는 시험지 출력 선택창")
    rt_otd.geometry("200x50")
    
    btn_exam = tk.Button(rt_otd, text="시험지 출력", command=lambda : create_exam_output_window(filepath))
    btn_exam.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  

    btn_word = tk.Button(rt_otd, text="단어장 출력", command=lambda : create_word_output_window(filepath))
    btn_word.grid(row=0, column=1, padx=10, pady=10, sticky="ew")  

    rt_otd.mainloop()

outputdialog()
